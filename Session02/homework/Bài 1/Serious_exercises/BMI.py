print("tính chỉ số BMI (Chỉ số khối cơ thể)")
h =float(input("height"))
print("Mời bạn nhập vào chiều cao theo đơn vị cm",h)
print("Đây là chiều cao tính theo đơn vị chuẩn m",h/100)
w=float(input("weight"))
print("Mời bạn nhập vào cân nặng theo đơn vị chuẩn kg",w)
BMI=0
BMI=(float)(w/(h*h))
print("Kết quả chỉ số BMI của người này là:",BMI)

if BMI<16 : 
    print("Thiếu cân nặng")
elif 16<= BMI <18,5:
    print("Thiếu cân")
elif  BMI<25:
    print("Bình thường")
elif BMI<30:
    print("Thừa cân")
else:
     print("Béo phì")
return
