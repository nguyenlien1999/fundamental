def is_inside(x,y):
    if y[0]<x[0]<y[0]+y[2] and y[1]<x[1]<y[1]+y[3]: 
        return True
    else: 
        return False
#Test
test=is_inside([200,120],[140,60,100,200])
if test == True:
   print("Your function is correct")
else:
   print("Ooops, bugs detected")