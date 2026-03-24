class Dog(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def glow(self):
        self.size += 1

    def __str__(self): # __str__()可以做到print一个object的时候输出想要的内容
        return (f"{self.name} the size {self.size} dog")

    def __repr__(self): # __repr__()可以做到程序员在控制台直接输入一个<object>的时候输出想要的内容
        return (f"{self.name} the size {self.size} dog")
    # __str__和__repr__的区别是：打印对象 vs 控制台反馈对象

# 实例化
dog_king = Dog("Knight",9999)
# 实例化数组
dogs = [Dog("maya",1000),Dog("yipster",5),Dog("scott",25)]
# 调用__str__方法打印第一只狗的内容
print(dogs[0])