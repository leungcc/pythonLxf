import os

print( [d for d in os.listdir('../')] )


#证明 os.listdir()可以获得一个list
print( isinstance(os.listdir('../'), (list)) ) 