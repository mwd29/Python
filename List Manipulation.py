x=[1,2,3,4,5,6,7,'aca']
x.append(2)
#x.count(7)
x.insert(1,55)

print(x)

x.remove(2)
print(x)

x.remove(2)
print(x)

x.remove(x[3])
print(x)


print(x[5:7])
print(x[-1])

print('Index broja 6 u listi je: ', x.index(6))

print("x.count('aca')= ",x.count('aca'))


y=[2,5,6,11,1,2,8]
y.sort()
print(y)

z=['Milica','Nesa','Luka','Aleksa','Mina','Marko','Lav','A']
z.sort()
print(z)