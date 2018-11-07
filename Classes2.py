class Cat:
    family='Feline'                 #class attribute(data attribute)
    def __init__(self,name):        #class attribute(class method)   ALSO CALLED CONSTRUCTOR!!!
        self.name=name

c1=Cat('Patches')
c2=Cat('Tiger')

#class variable
print('c1.family = ',c1.family) #shared by all instance objects of the Cat class
print('c2.family =',c2.family)  #shared by all instance objects of the Cat class



print(c1.name)
c2.skill='catch mice'
print(c2.skill)

c2.nista='nista'
print(c2.nista)