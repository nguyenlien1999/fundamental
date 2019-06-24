#a.in ra 20 lần dấu *
print("*"*20)

#b.in ra số lần (n) dấu * , với n được nhập từ bàn phím người dùng
n=int(input("n="))
print("Bạn muốn nhâp n= ",n ,end="")
print(" dấu sao")
print(" *"*n)

# #c.9 stars and xs in total
# print(" X * X * X * X * X ")
for i in range(1):
    print(" X * "*4,end="")
print(" X")
 

#d.n stars and xs in total (n is entered by users)
n=int(input("mời bạn nhập vào số : X * mong muốn n="))
for i in range(1):
    print(" X *"*int(n/2),end="")
print(" X")

#e.You can use print(), (yes, print with nothing inside the parentheses ()) to move to a new line, try it
print()

#f. 7 x 3 stars

for i in range(3):
     print(" *"*7)

#g.n x m stars (n, m are entered by users)
n=int(input("mời bạn nhập số hàng mong muốn n= "))
m=int(input("mời bạn nhập số cột mong muốn m= "))

for i in range(m):
    print(" * "*n)


