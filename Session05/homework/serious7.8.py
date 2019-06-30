def remove_dollar_sign(s):
   return s.replace("$", " ")
s=str(input("nhập 1 chuỗi cần loại bỏ dollar: "))
print(remove_dollar_sign(s))
# serious 8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

