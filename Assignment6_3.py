print("Arithmetic...........")
class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0
        #Accept(), Addition(), Subtraction(),
#Multiplication(), Division().
    def Accept(self):
        self.value1=int(input("Enter val1:::"))
        self.value2=int(input("Enter val2:::"))
    def Addition(self):
        ans=self.value1+self.value2
        return ans
    def Subtraction(self):
        ans=self.value1-self.value2
        return ans
    def Multiplication(self):
        ans = self.value1 * self.value2
        return ans
    def Division(self):
        ans = self.value1 / self.value2
        return ans

    def Display(self):
        print (self.value1,self.value2)

def main():
    obj1=Arithmetic()
    obj1.Accept()
    #obj1.Display()
    print("Addition::::",obj1.Addition())
    print("Subtraction::::", obj1.Subtraction())
    print("Multiplication::::", obj1.Multiplication())
    print("Division::::", obj1.Division())

if __name__ == '__main__':
    main()
