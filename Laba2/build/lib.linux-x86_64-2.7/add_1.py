#-*- coding: utf-8 -*-

def isType(s):
    if s[0] == "[" and s[-1] == "]":
        return list
    if s[0] == "{" and s[-1] == "}":
        return dict
    if s[0] == "\"" and s[-1] == "\"":
        return str
    else:
        return int


def div(s):
    ans = []
    temp = []
    squer = 0
    curly = 0
    strl = False
    last = s[0]
    for i in s:
        if " " == i and "," == last:
            continue
        if "," == i and curly == 0 and squer == 0 and strl == False:
            ans.append(''.join(temp))
            temp = []
            last = i
            continue  
        temp.append(i)
        if "[" == i and strl == False:
            squer += 1
            continue
        if "]" == i and strl == False:
            squer -= 1
        if "{" == i and strl == False:
            curly += 1
        if "}" == i and strl == False:
            curly -= 1
        if "\"" == i:
            if strl == False:
                strl = True
            else:
                strl = False
    if len(temp) != 0:
        ans.append(''.join(temp))
    return ans
        

def from_json_toList(s):
    temp = div(s)
    k = []
    for i in temp:
        if i[0] == "[":
            k.append(from_json_toList(i[1:-1]))
            continue
        if i[0] == "{":
            k.append(from_json_toDict(i[1:-1]))
            continue
        if isType(i) == str:
            k.append(str(i[1:-1]))
            continue
        else:
            k.append(int(i))
            continue
    return k


def check(s):
    if s[0] == " ":
        s = s[1:]
    if s[-1] == " ":
        s = s[:-1]
    return s


def from_json_toDict(s):
    s = div(s)
    d = {}
    temp = []
    for i in s:
        temp.append(i.split(":"))
    for j in temp:
        k = j[0]
        v = j[1]
        k = check(k)
        v = check(v)
        if isType(v) == dict:
            value = from_json_toDict(v[1:-1])
        elif isType(v) == list:
            value = from_json_toList(v[1:-1])
        elif isType(v) == int :
            value = int(v)
        else:
            value = v[1:-1]
        if isType(k) == int:
            key = int(k)
        else:
            key = k[1:-1]
        d[key] = value
    return d

def from_json(s):
    if isType(s) == list:
        return from_json_toList(s[1:-1])
    if isType(s) == dict:
        return from_json_toDict(s[1:-1])
    if isType(s) == str:
        return s[1:-1]
    else:
        return int(s)

def main():
    print from_json('"w"')
    print from_json('1')
    print from_json('{"w" : [1, 2, 3], "q" : 2}')
    print from_json('["abac[ava", [1, 2, 3] ]')
    print from_json('["er", 3, "43", ["ew", [2, 3, 3]], "e", 4]')

if __name__ == "__main__":
    main()
