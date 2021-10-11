from decorator_def import FuncDecoratorOne, FuncDecoratorListProperties, ClassDecoratorOne

class FuncDecoratorUse:

    def __init__(_self_):
        _self_.var1 = "test"
        _self_.var2 = "abc"
        _self_.var3 = 12345

    @FuncDecoratorListProperties
    def FunctionOne(_self_, v):
        print("FunctionOne: ", v)


t = FuncDecoratorUse()
t.FunctionOne("Test")

@ClassDecoratorOne
class ClassDecoratorUser:
    def __init__(_self_):
        print("Hello, World !")

t = ClassDecoratorUser()