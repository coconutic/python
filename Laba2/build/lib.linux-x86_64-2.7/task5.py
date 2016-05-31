class Logger(object):
    d = {}

    def memor(self, func):
        def input(*args, **kwargs):
            temp = func(*args)
            self.d[func.func_name] = (temp, args)
            return temp
        return input


    def __init__(self):
        methods = dir(self)
        for i in xrange(len(methods)):
            try:
                if callable(getattr(self, methods[i])):
                    setattr(self, methods[i], self.memor(getattr(self, methods[i])))
            except BaseException:
                print methods[i]
        

    def __str__(self):
        sep = ""
        k = []
        keys = Logger.d.keys()
        val = Logger.d.values()
        for i in xrange(len(Logger.d.items())):
            par = []
            k.append("_______________\n")
            for j in val[i][1]:
                par.append(j)
            if len(par) == 0:
                k.append("Function name: \"{0}\" \nno parameters \nresult: {1} \n".format(keys[i], val[i][0]))
            else:
                k.append("Function name: \"{0}\" \nparameters: {1} \nresult: {2} \n".format(keys[i], par, val[i][0]))
            k.append("_______________\n")
        return sep.join(k)

class Ex(Logger):
    def a(self, a):
        return a ** a

    def b(self):
        return  1

o = Ex()
o.a(2)
o.b()
print o
