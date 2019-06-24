while True:
    print ("hi")

for v in range(5):
    print('hi')

for v in range(5):
    print("hi",v)


dem=0
while True:
    print ('hi',dem)
    dem+=1
    if dem>=3:
        break

dem=0
while dem<3:
    print("hi",dem)
    dem+=1#hi0->2

loop =True
dem=0
while loop:
    print("hi",dem)
    dem+=1
    if dem>=3:
        loop=False

for i in range (1000):
    print("hi",i)
    if i>=2:
        break
    

ex1 # print("mời bạn nhập password")
n= str (input("password: "))
while len(n)>8:
    print("password của bạn là:",n)
    break

ex2:Lãi suất ngân hàng acb đang là 6.5% một năm. Hnay anh sẽ đi gửi 21 triệu. Viết chương trình để tính:
Sau 9 năm thì a có bao nhiêu tiền trong tài khoản?
Muốn mua một căn nhà giá 1.2 tỷ thì a cần gửi ngân hàng ít nhất là bao nhiêu năm?

ls= float(input("Mời bạn nhập vào số lãi ngân hàng trong 1 năm="))
goc=float(input("số tiền anh A gửi="))
print("sau 9 năm thì a có số tiền trong tài khoản là:",float(goc*1.065*9)


While True:
    print("muốn mua căn nhà 1,2 tỉ thì ít nhất là: "+(float)(1200000000/(goc*(1+ls))+"năm")
    break

a=list(range(3))
print("a",a)# a[0,1,2]

arr = [x * x for x in range(100)]
print(arr)

Nhập n số nguyên từ bàn phím. 
- In ra dãy vừa nhập
- In ra trung bình cộng các số chẵn


n=int (input("nhập số phần tử"))
ds=[]
for v in range(n):
    so= input("nhập phần tử "+str(v)+":")
    so=int(so)
    ds.append(so)

print("dãy số vừa nhập là",ds)

tong_chan=0
so_so_chan=0
for v in ds:
    if v%2==0:
        tong_chan+=v
        so_so_chan+=1
print("trung bình cộng số số chẵn là",tong_chan/so_so_chan)







    

