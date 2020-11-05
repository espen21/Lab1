import sys
import os 
try:
    f = os.open("test.txt",os.O_WRONLY|os.O_CREAT)
    line = input("Write some stuff \n")
    line = str.encode(line)
    os.write(f,line)
    os.close(f)

    

except Exception as e:
    print("error =>",e)
    
