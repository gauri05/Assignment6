print("Assignment6")


class Demo:
    value = 5  # class variable

    def __init__(self, val1, val2):
        self.no1 = val1  # no1,no2 =instance variable
        self.no2 = val2

    def Fun(self):  #instance method
        print ("Inside fun")
        print (self.no1, self.no2)

    def Gun(self):   #instance method
        print ("Inside gun")
        print (self.no1, self.no2)


def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()


if __name__ == '__main__':
    main()
