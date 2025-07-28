
try:
    print(x)
except NameError:
    print("variable x is not defined")
else:
    print("everything went fine")

        
x = -1  
    
if x < 0:
    raise Exception("sorry, no numbers below zero")