x = 5,6,2,6   #Tuple
y = (5,6,2,6) #Tuple
z=[1,2,3,4]   #List
print(x[0])
print(y)
print(z)

def exFunc():    #TYPE : Tuple!!!
    return 15,24

m,n=exFunc()
#print(type(exFunc()))  -> Tuple
print(m,n)


def exFunc2():
    return [1,2]

p,q=exFunc2()
print(type(exFunc2()))