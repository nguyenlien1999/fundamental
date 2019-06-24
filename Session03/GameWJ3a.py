import random
print("Mời bạn chơi game WORD JUMBL")
a=['c','r','e','a' ,'t','e']
random.shuffle(a)
# random.sample(a)
print("mời bạn đoán từ sau : ", a)
doan=str(input("Từ bạn đoán mà có ý nghĩa là:"))
print("bạn có chắc chắn là từ này không?",doan)
if doan=='create':
    print("hura")
else:
    print(":(")
#normal- làm theo cách ngây thơ :))


