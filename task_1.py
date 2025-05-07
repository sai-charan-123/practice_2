n=int(input("Enter the number :"))
sum_even=0
for n in range(n+1):
	if n%2==0:
		sum_even=sum_even+n
print("sum of {} numbers is : {} ".format(n,sum_even))