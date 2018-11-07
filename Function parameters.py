def simple_addition(num1,num2):
    answer=num1+num2
    print('num1 is',num1)
    print(answer)

simple_addition(5,3)

def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print(num1,num2)


def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc)


simple(1) #simple(1,2)
basic_window(500,350,bgc='b')

