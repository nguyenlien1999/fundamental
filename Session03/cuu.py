n=int(input("number of sheep you have "))
size=[]
for i in range(n):
    a=int(input("size of  sheep"+ str(i+1) + ":"))
    size.append(a)
print("Hello, My name is Lien and these are the ship sizes:",size)

print("Now my biggest sheep has size ",max(size),"let's shear it")

size[size.index(max(size))] = 8
print("After shearing, here is my flock",size)

moth =int(input("Number of months of sheep, month="))
for i in range(1,moth+1):
    print("after the number of months",i)
    for i in range(n):
        new_size=size[i]+50
        size[i]=new_size
    print("One month has passed, now here is my flock")
    print(size)
    print("Now my biggestbiggest sheepsheep has size", max(size), "let's shear it")


    for j in range(n):
        size[j]+=50
    print("after the sheep grow ",size[i])

    S = 0
    for i in range(n):
        S = S + size[i]

    print("My flock has sizesize in total: ", S)
    print("I would get ", S, "* 2$ = ",S*2)














