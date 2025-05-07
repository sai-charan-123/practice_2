n=int(input("Enter the number :"))
mul_even=1
for n in range(2,n+1,2):
		mul_even*=n
print("mul of {} numbers is : {} ".format(n,mul_even))