n=int(input("Enter the number :"))
mul_even=1
for n in range(1,n+1):
	if n%2==0:
		mul_even=mul_even*n
print("mul of {} numbers is : {} ".format(n,mul_even))