enc_keys = []
dec_keys = []

inputFile = ''
outputFile = ''
operation = ''

mod = 65537
ones25 = 0b1111111111111111111111111
ones64 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def generate_keys(key):
    keys = []
    for i in xrange(7):
        for j in xrange(1, 9):
            keys.append((key >> (128 - 16 * j)) & 0xFFFF)
        temp = (key >> 103) & ones25
        key <<= 25
        key = key & ones64
        key += temp
    for i in xrange(0, 52, 6):
        enc_keys.append(keys[i:i + 6])


def binPow(a, n):
    r = 1
    while n:
        if n & 1:
            r = (r * a) % mod
        n >>= 1
        a = (a * a) % mod
    return int(r)


def multi(x):
    if x <= 1:
	return x
    y = 0x10001;
    t0 = 1;
    t1 = 0;
    while True:
	t1 += y / x * t0;
	y %= x;
	if y == 1:
	    return 0x10001 - t1

	t0 += x / y * t1;
	x %= y;

	if x == 1:
	    return t0


def addInv(x):
    return (0x10000 - x) & 0xFFFF;

def generate_rev_keys():
    dec_keys.append([multi(enc_keys[8][0]),
                    addInv(enc_keys[8][1]), addInv(enc_keys[8][2]),
                    multi(enc_keys[8][3]),
                    enc_keys[7][4], enc_keys[7][5]])
    for i in xrange(7, 0, -1):
        dec_keys.append([multi(enc_keys[i][0]),
                        addInv(enc_keys[i][2]), addInv(enc_keys[i][1]),
                        multi(enc_keys[i][3]),
                        enc_keys[i - 1][4], enc_keys[i - 1][5]])
    dec_keys.append([multi(enc_keys[0][0]),
                     addInv(enc_keys[0][1]), addInv(enc_keys[0][2]),
                     multi(enc_keys[0][3])])


def div_block(b):
    cur_blocks = []
    cur_blocks.append(b >> 48)   #first 16bits
    cur_blocks.append((b >> 32) & 0xFFFF)  #second 16bits and zero_one
    cur_blocks.append((b >> 16) & 0xFFFF)
    cur_blocks.append(b & 0xFFFF)
    return cur_blocks


def m(a, b):
    result = a * b
    if result != 0:
        return (result % 0x10001) & 0xFFFF
    else:
        return (1 - a - b) & 0xFFFF


def p(a, b):
    return (a + b) & 0xFFFF


def get_symbols(d):
    ans = []
    for i in d:
        ans.append(i >> 8)
        ans.append(i & 0xFF)
    return ans



def convert(b):
    global enc_keys
    d = div_block(b)

    for i in xrange(8):
        a = m(d[0], enc_keys[i][0])
        b = p(d[1], enc_keys[i][1])
        c = p(d[2], enc_keys[i][2])
        dk = m(d[3], enc_keys[i][3])
        e = a ^ c
        f = b ^ dk
        t1 = m(p(f, m(e, enc_keys[i][4])), enc_keys[i][5])
        d[0] = a ^ t1
        d[1] = c ^ t1
        t2 = p(m(e, enc_keys[i][4]), m(p(f, m(e, enc_keys[i][4])), enc_keys[i][5]))
        d[2] = b ^ t2
        d[3] = dk ^ t2
    d[0] = m(d[0], enc_keys[8][0])
    temp = d[1]
    d[1] = p(d[2], enc_keys[8][1])
    d[2] = p(temp, enc_keys[8][2])
    d[3] = m(d[3], enc_keys[8][3])
    return get_symbols(d)


def encodeIDEA():
    fr = open(inputFile, 'r')
    fw = open(outputFile, 'w')

    flag = True
    while flag:
        count = 0
        chunk = 0
        for i in xrange(8):
            new_symbol = fr.read(1)
            if new_symbol == '':
                if count != 8:
                    for b in xrange(8 - count):
                        chunk = (chunk << 8) + 0b0100000
                flag = False
                break
            else:
                count += 1
                chunk = (chunk << 8) + ord(new_symbol)
        if count == 0:
            break

        for i in convert(chunk):
            fw.write(chr(i))
    fr.close()
    fw.close()


def main():
    global inputFile
    global outputFile
    global operation

    operation = raw_input('Write descrypt or encrypt file, please: ')
    inputFile = raw_input('Write input file name :')
    outputFile = raw_input('Write output file name: ')

    key = long(raw_input())
    generate_keys(key)
    if operation == 'encrypt':
        encodeIDEA()
    else:
        global enc_keys
        global dec_keys

        generate_rev_keys()
        enc_keys = dec_keys[:]
        encodeIDEA()


if __name__ == "__main__":
    main()
