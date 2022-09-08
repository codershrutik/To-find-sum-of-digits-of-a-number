n = int(input("Enter a number: "))
tot = 0

while(n>0):
    dig = n%10
    tot = dig+tot
    n = n//10
print("The total sum of the digits of the number is: ",tot)