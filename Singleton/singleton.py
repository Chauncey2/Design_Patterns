class singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(singleton,cls).__new__(cls)
        return cls.instance

s=singleton() #实例化
print(s)
a=singleton() #再次实例化
print(a)
