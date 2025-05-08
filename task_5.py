n=int(input("Enter the number :"))
mul_odd=1
for n in range(1,n+1):
	if n%2==1:
		mul_odd=mul_odd*n
print("mul of {} numbers is : {} ".format(n,mul_odd))