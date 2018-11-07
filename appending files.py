appendMe='\nNew bit of information'

appendFile=open('appendFile.txt','a')
appendFile.write(appendMe)
appendFile.close()