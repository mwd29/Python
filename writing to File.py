text = 'Sample Text to Save\nNew line!'

saveFile=open('exampleFile.txt','w')
newFile=open('Second file.txt','w')

newFile.write('aca')
saveFile.write(text)
saveFile.close()
