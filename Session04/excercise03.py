print("Answer the following algelbra question")
print("If x=8, then what is the value of 4(X+3)")
key={1:35,2:36,3:40,4:44}
answer=int(input("Your choice:"))
for i in key:
    print(i,".",key[i])
if answer==4:
     print("Bingo")
else:
   
     print(":(")