def get_even_list(ls):   
    ls_even=[]
    for v in ls:       
            if v%2 == 0:
                ls_even.append(v)
        
            if v==0:
                ls_even.append('')
    return ls_even
print(get_even_list([1,4,5,-1,10,9,0,99,100]))
# 10
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")






