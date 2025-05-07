n=int(input("Enter the number :"))
sum_odd=0
for x in range(n+1):
	if x%2==1:
		sum_odd=sum_odd+x
print("sum of {} numbers is : {} ".format(x,sum_odd))