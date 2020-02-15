#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

max=4000000
summa=2
x1=1
x2=2
x=0
list_fibo=[x1,x2]
i=0
while x < max:
    x=x1+x2
    list_fibo.append(x)
    x1 = x2
    x2 = x
    if x%2==0:
        summa+=x


print(summa)
print(list_fibo)
s2=0
for x in list_fibo:
     s2+=x
print(s2)
print(len(list_fibo))