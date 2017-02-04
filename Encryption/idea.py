key_table = []
key_table2 = []

def generate_keys(key):
    all_keys = []
    for i in xrange(7):
        for j in xrange(1, 9):
            all_keys.append((key >> (128 - 16 * j)) & 0xFFFF)
        temp = (key >> 103) & 0b1111111111111111111111111
        key <<= 25
        key = key & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        key += temp
    for i in xrange(0, 52, 6):
        key_table.append(all_keys[i:i + 6])

mod = 65537

def binPow(a, n):
    r = 1
    while n:        
        if n & 1: 
            r = (r * a) % mod
        n >>= 1
        a = (a * a) % mod                                                          
    return int(r)


def multi(k):
    return binPow(k, mod - 2)    


def make_keys():
    t = 2 ** 16
    key_table2.append([multi(key_table[8][0]), 
                       t - key_table[8][1],
                       t - key_table[8][2],
                       multi(key_table[8][3]),
                       key_table[7][4], key_table[7][5]])
    for i in xrange(7, 0, -1):
        temp = []
        temp.append(multi(key_table[i][0]))
        temp.append(t - key_table[i][2])
        temp.append(t - key_table[i][1])
        temp.append(multi(key_table[i][3]))
        temp.append(key_table[i - 1][4])
        temp.append(key_table[i - 1][5])
        key_table2.append(temp)
    key_table2.append([multi(key_table[0][0]), 
                       t - key_table[0][1],
                       t - key_table[0][2],
                       multi(key_table[0][3])])
    for i in key_table2:
        print i

def div_block(b):
    cur_blocks = []
    cur_blocks.append(b >> 48)   #first 16bits
    cur_blocks.append((b >> 32) & 0xFFFF)  #second 16bits and zero_one
    cur_blocks.append((b >> 16) & 0xFFFF)
    cur_blocks.append(b & 0xFFFF)
    return cur_blocks

def m(a, b):
    return ((a * b) % (2 ** 16 + 1)) & 0xFFFF

def p(a, b):
    t = 2 ** 16
    return (a + b) % t

def get_symbols(d):
    ans = []
    for i in d:
        ans.append(i >> 8)
        ans.append(i & 0xFF)
    return ans

def f(b):
    d = div_block(b)
    global key_table
    for i in xrange(8):
        a = m(d[0], key_table[i][0])
        b = p(d[1], key_table[i][1])
        c = p(d[2], key_table[i][2]) 
        dk = m(d[3], key_table[i][3]) 
        e = a ^ c
        f = b ^ dk
        t1 = m(p(f, m(e, key_table[i][4])), key_table[i][5]) 
        d[0] = a ^ t1
        d[1] = c ^ t1
        t2 = p(m(e, key_table[i][4]), m(p(f, m(e, key_table[i][4])), key_table[i][5]))
        d[2] = b ^ t2      
        d[3] = dk ^ t2
        print map(hex, d)
    d[0] = m(d[0], key_table[8][0])
    temp = d[1]
    d[1] = p(d[2], key_table[8][1])
    d[2] = p(temp, key_table[8][2])
    d[3] = m(d[3], key_table[8][3])
    return get_symbols(d)


def do(input_file, output_file):
    f_r = open(input_file, 'r')
    f_w = open(output_file, 'w')
    while True:
        block = f_r.read(8)
        if block == '':
            break
        current = 0
        for l in xrange(len(block)):
            current += ord(block[l])
            if len(block) - 1 != l:
                current <<= 8
        encrypt_text = f(current)
        for i in encrypt_text:
            f_w.write(chr(i))
    f_r.close()
    f_w.close()

def encrypt(i, o):
    do(i, o)

def decrypt(i, o):
    make_keys()
    global key_table
    key_table = key_table2[:]
    do(i, o)


def main():
#    operation = raw_input('Write descrypt or encrypt file, please: ')
#    input_file = raw_input('Write input file name :')
#    output_file = raw_input('Write output file name: ')
    
#    while True:
#        key = bin(int(raw_input('Write key: ')))
#        key = key[0] + key[2:]
#        if len(key) <= 128:
#            break
    operation = 'decrypt'
    input_file = 'input.txt'
    output_file = 'output.txt'
    key = 5192455318486707404433266433261576L
    generate_keys(key)
    if operation == 'encrypt':
        encrypt(input_file, output_file)
    else:
        decrypt(output_file, input_file)


if __name__ == "__main__":
    main()
