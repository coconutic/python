#-*- coding: utf-8 -*-

def from_json_toList(s):
    s = s.split(", ")
    k = []
    flagList = False
    temp = []
    for i in s:
        if i[0] == "[":
            temp.append(i)
            flagList = True
            continue
        if i[-1] == "]":
            temp.append(", ")
            temp.append(i)
            t = "".join(temp)
            k.append(from_json_toList(t[1: -1]))
            flagList = False
            continue
        if flagList == False:
            if i[0] == "\"" and i[-1] == "\"":
                k.append(str(i[1:-1]))
                continue
            else:
                k.append(int(i))
                continue
        temp.append(", ")
        temp.append(i)
    return k

def from_json_toDict(s):


def from_json(s):
    if s[0] == "[" and s[-1] == "]":
        return from_json_toList(s[1:-1])
    if s[0] == "{" and s[-1] == "}":
        return from_json_toDict(s[1:-1])
def main():
    from_json('["er", 3, "43", ["ew", 2], "e", 4]')

if __name__ == "__main__":
    main()
