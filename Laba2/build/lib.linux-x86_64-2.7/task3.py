def check(obj, s):

    if isinstance(obj, (tuple, list)):
        s.append("[")
        for i in obj:
            s = check(i, s)
            s.append(", ")
        del s[-1]
        s.append("]")
        return s
    if isinstance(obj, dict):
        s.append("{")
        for k,v in obj.items():
            temp = v
            temp2 = k
            s.append("\"{0}\" : ".format(temp2))
            s = check(temp, s)
            s.append(", ")
        del s[-1]
        s.append("}")
        return s
    if isinstance(obj, (int, long)):
        s.append(str(obj))
        return s
    if isinstance(obj, str):
        index = 0
        symbols = ["\"", "\'", "\n", "\a", "\b", "\t"]
        symbols_change = ["\\\"", "\\\'", "\\n", "\\a", "\\b", "\\t"]
        for i in symbols:
            if i in obj:
                obj =  obj.replace(i, symbols_change[index])
            index += 1
        s.append("\"" + obj + "\"")
        return s
 
  

def to_json(obj, raise_unknown = False):
    if raise_unknown:
        raise TypeError(type(obj))
    separator = ""
    s = []
    s = check(obj, s)
    return separator.join(s)
 
