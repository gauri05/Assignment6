print ("Circle.....")


class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumferance = 0.0

    def Accept(self):
        # print("Accept");   self.value1=input("Enter val1:::")
        self.radius = int(input("Enter value(Radius)::::"))

    def CalculateArea(self):
        # print (self.radius)
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumferance = 2 * Circle.PI * self.radius

    def Display(self):
        print ("Radius::::", self.radius)
        print ("Area:::", self.area)
        print ("circumference", self.circumferance)


def main():
    obj1 = Circle()
    obj1.Accept();
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()


if __name__ == '__main__':
    main()
