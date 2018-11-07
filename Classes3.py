class Calculator:

    def addition(x,y):
        added = x + y
        print(added)

    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print(mult)

    def division(x,y):
        div = x / y
        print(div)

    #return
    def add(x,y):
        added = x + y
        return added


Calculator.multiplication(3,5)

x=Calculator.addition(1,2)


#z=Calculator()
#z.add(3,4) NE MOZE!!!
z=Calculator.add(5,4) #OVAKO MOZE!!!
print(z)

#k=input("What's your name? ")
#print("Hello,", k)