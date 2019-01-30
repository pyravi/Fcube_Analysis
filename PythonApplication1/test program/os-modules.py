import os
from datetime import datetime
#print(dir(os))     #print all options
#print(os.getcwd())  #print current directory path
#os.chdir('E:/Devops/PythonApplication1/')# change the path
"""
os.mkdir()
os.makedirs('ravi')
os.rmdir()
os.removedirs('ravi')
os.rename('original.txt','renaming.txt')
os.stat('renaming.txt')
print(os.listdir())
"""
#print(os.listdir())    #list number of directorys
"""print(os.stat('E:/Devops/PythonApplication1/test program/camera.py'))
print(os.stat('E:/Devops/PythonApplication1/test program/camera.py').st_mtime)

var=os.stat('E:/Devops/PythonApplication1/test program/camera.py').st_mtime
print(datetime.fromtimestamp(var))

for dirpath,dirnames, filenames in os.walk('E:/Devops/PythonApplication1/'):    #Access hirareiy tree of F/D
    print('current Path:',dirpath)
    print('Directorys:',dirnames)
    print('Files',filenames)
"""
print(os.environ.get('Path')) #Access Path
#file_file= os.path.join(os.environ.get('Path'), 'file.txt')                    #Create a Path
