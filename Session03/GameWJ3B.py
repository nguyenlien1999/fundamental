# suy nghĩ???? câu a quá dài, không tối ưu!
import random
print("Mời bạn chơi game WORD JUMBL")
print("Quy tắc chơi là đưa ra 1 dãy các kí tự bạn đoán và sắp xếp thành 1 từ có ý nghĩa ")
ds= ["meticulous", "champion", "hexagon"]
a=random.choice(ds)
b=list(a)
random.shuffle(b)

for i in range(len(b)):
    print(b[i])
ps= str (input ("câu trả lời của bạn là : " ) )
if a == ps: 
    print("Hura")
else:
    print(":(")

