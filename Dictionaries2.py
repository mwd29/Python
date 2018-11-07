exDict = {'Jack':[15,'blonde'], 'Bob':[22,'black'], 'Alice':[12,'red'], 'Kevin':[17,'green']}

print(exDict['Jack'])
print(exDict['Jack'][1])


exDict['Tim']=[14,'white'] #adding new one
print(exDict)

exDict['Tim']=15
print(exDict)

del exDict['Tim']
print(exDict)



