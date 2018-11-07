try:
    f=open('Numbers.txt')
    i=0
    for line in f.readlines():
        print(int(line)/10)
        i+=1
    f.close()

except FileNotFoundError:
    print("Enter the correct file name")
except:
    print("Some other error")
else:
    print('Found',i,'integers sucessfully')