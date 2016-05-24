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

#def mergeList(s):
    
def from_json_toList(s):
    s = s.split(", ")
    k = []
    flagList = False
    temp = []
    for i in s:
        if i[0] == "[":
            temp.append(i)
            temp.append(', ')
            flagList = True
            continue
        if i[-1] == "]":
            temp.append(i)
            t = "".join(temp)
            k.append(from_json_toList(t[1: -1]))
            flagList = False
            continue
        if flagList == False:
            if isType(i) == str:
                k.append(str(i[1:-1]))
                continue
            else:
                k.append(int(i))
                continue
        temp.append(i)
        temp.append(", ")
    return k

def from_json_toDict(s):
    s = s.split(", ")
    k = []
    d = {}
    temp = []
    count = 0
    for i in s:
        if "[" in i:
            flagList = True
            count += 1
        if flagList:
            temp.append(i)
            if "]" in i:
                count -= 1
                if count == 0:
                    flagList = False
                    break

    for i in s:
        k.append(i.split(" : "))
    for j in k:
        k = j[0]
        v = j[1]
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
  #  print from_json('{"w" : [1, 2, 3], "q" : {"a" : 1} }')
    print from_json('{"w" : 1, "1" : 2}')
    print from_json('["er", 3, "43", ["ew", [2, 3, 3]], "e", 4]')

if __name__ == "__main__":
    main()
