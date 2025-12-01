#any method 
nums=[-1, -2, -3, 4, -5]
is_positive=all(map(lambda x:x>0,nums))
print(is_positive)

#all method, find if any number is even
nums2=[1, 3, 5, 7, 8]
any_even=any(map(lambda x:x%2==0,nums2))
print(any_even);

div_five=any(map(lambda x:x%5==0,nums2))
print(div_five)




