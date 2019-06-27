    
questions={"If x=8, then what is the value of 4(x+3)?":[35,36,40,44,4],
    "Jack scored these marks in 5 math tests : 49, 81, 72, 66 and 52. What is the mean?":[55,65,75,85,2]}
correct=0
for key in questions:
    print(key)
    for i in range(5):
        print(str(i),questions[key][i])
    answer=int(input("Your choice:"))
    if answer==questions[key][5]:
        print("Bingo ")
        correct+=1
    else:
        print(":(")
print("You correctly answer "+str(correct)+"out of 2 questions")