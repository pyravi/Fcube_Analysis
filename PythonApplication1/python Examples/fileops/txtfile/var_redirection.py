print('Using the file reading function \n __________________________________________')
text='Something is put on file \nThis is for new Line'
Saveinfile=open('text.txt','w')
Saveinfile.write(text)
Saveinfile.close()

ReadFile=open('text.txt','r').read()
print(ReadFile)
ReadFilein_listwise=open('text.txt','r').readlines()
print(ReadFilein_listwise)

appendtext='\nThis is append test'
append=open('text.txt','a')
append.write('\n')
append.write(appendtext)
append.close()
append=open('text.txt','r').read()
print(append)
