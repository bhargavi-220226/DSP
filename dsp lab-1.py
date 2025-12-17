import datetime
import math

#1.current date and time
date=datetime.datetime.now()
print("year:",date.year)
print("month:",date.month)
print("day:",date.day)
print("hour:",date.hour)
print("minute:",date.minute)
print("second:",date.second)

#2.user's first name,lastname and print them in reverse
first_name=input("enter first name:")
last_name=input("enter last name:")
revf=""
for ch in first_name:
    revf=ch+revf
revl=""
for ch in last_name:
    revl=ch+revl
print(revl+""+revf)

#3.compute the value of n+nn+nn for a integer n
n=int(input("enter n:"))
output=n+(n*n)+(n*n*n)
print("n+nn+nnn:",output)

#4.sum of 3 given numbers,when equal values-return three times their sum

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
sum=a+b+c
if a==b and b==c:
    sum=sum*3
print("sum:",sum)

#5.to solve (x+y)*(x+y)
x=int(input("enter x:"))
y=int(input("enter y:"))
result=((x+y)**2)
print(f"(( {x} + {y} )^2):",result)

#6.future compund interest
amount=int(input("enter amount:"))
rate=float(input("enter rate:"))
year=float(input("enter no of years:"))
t=int(input("enter no of times the interest at compound:"))
result=amount*((1+(rate/100))**(year*t))
print("future value:",round(result,2))

#7.parse a string to float or integer
num=input("enter number:")
print("float:",int(num))
print("integer:",float(num))

#8.sum the first n numbers
n=int(input("enter n value:"))
total=0
i=1
while i<=n:
    total=total+i
    i=i+1
print("sum the first n numbers:",total)

#9.sum of digits of a no.
n=int(input("enter n value:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum of digits of a no.:",sum)

#10.ASCII value of a ch
ch=input("enter a character:")
print("ASCII value of a ch:",ord(ch))

#11.check string is numeric
s=input("enter a string:")
if s.isnumeric():
    print("the given string is numeric")
else:
    print("the given string is a string")

#12.rectangular number pattern
rows=5
cols=3
print("rectangular pattern:")
for i in range(rows):
    j=0
    line=""
    while j<cols:
        line=line+"*"
        j=j+1
    print(line)

#13.finding numbers -divisble by 7 but not multiple by 5 between 2000-3200
print("finding numbers -divisble by 7 but not multiple by 5 between 2000-3200")
for n in range(2000,3201):
    if n%7==0 and n%5!=0:
        print(n)

#14.square root of[(2*C*D)/H]
import math
C=50
H=30
D=input("enter separated values by comma:").split(",")
res=[]
for i in D:
    Q=math.sqrt((2*C*int(i))/H)
    res.append(str(round(Q)))
print(",".join(res))

#15.alphabet right angle triangle
n=int(input("enter range number:"))
print("alphabet inverted(down) right angle triangle:")
for i in range(n,0,-1):
      for j in range(i):
          print(chr(j+65),end='')
      print()
      





