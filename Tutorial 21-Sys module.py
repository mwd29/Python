import sys

sys.stderr.write('stderr text\n')
sys.stderr.flush()
sys.stdout.write('stdout text\n')

print(sys.argv)

#if len(sys.argv)>1:
    #print(sys.argv[1])

if len(sys.argv)>1:
    print(float(sys.argv[1])+5)


