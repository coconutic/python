#-*- coding: utf-8 -*- 

class MyDefaultDict(dict):

    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key in self.d.keys():
            return self.d[key]
        else:
            self.d[key] = MyDefaultDict()
            return self.d[key]

    def __setitem__(self, key, item):
        self.d[key] = item
        
    def __str__(self):
        s = ['{']
        for i in self.d.keys():
            s.append(str(i))
            s.append(": ")
            s.append(str(self.d[i]))
            s.append(',')
        if len(s) > 2 :
            del s[-1]
        s.append('}')
        return "".join(s)

def main():
    a = MyDefaultDict()
    print a["e"]["q"]
    print a

if __name__ == "__main__":
    main()
