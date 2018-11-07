class Tree:
    """A class to represent a tree"""
    #Species is a class attribute
    species='Oak'
    #describe_me is a class attribute
    def describe_me(self):
        return 'I am a tree'


#y=Tree.species='BBBBirch'

y=Tree()
y.species='BBB'
x=Tree()

print(x.species)
print(y.species)
isinstance(x,Tree)