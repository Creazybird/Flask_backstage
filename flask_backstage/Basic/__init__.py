#Python中的类
class Person(object):
    def __init__(self,name,gender):
        self.__age=12
        self.name=name
        self.gender=gender
    def getage(self):
        return self.__age
if __name__=='__main__':
    person=Person('光中','男')
    #类中的__dict__结果：
    #{'__module__': '__main__', '__init__': <function Person.__init__ at 0x000001EB51A071F8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
    print(Person.__dict__)
    #实例中__dict__结果：
    #{'name': '光中', 'gender': '男'}
    print(person.__dict__)
    print(person.name)
    print(person.getage())
    print(person.__age)
