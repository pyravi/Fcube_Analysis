print('Using the print function \n __________________________________________')
a=100
ab=print('papu pass ho gya')
word='Hello World'
print("print value of a:", a*a-1 )
print( "print value of word:", word)
print('aaaaa',a,'word',word)
print(word +str(5)) #or 
print(word,5) 
print(a+6)
print('a '+str(6))
print(int(100/3))
print(float(100)/3)
print('__________________________________________')
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
print('__________________________________________')
x,y=(444,7777777777777777777777)
print(x)
print(y)
