try:
    f=open('Numbers.txt')
    for line in f.readlines():
        print(int(line)/10)
    f.close()

except FileNotFoundError:
    print("Enter the correct file name")
except ValueError:
    print("Please provide an int value")
except:
    print("Some other error")