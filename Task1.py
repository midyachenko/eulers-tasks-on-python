#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

n=1000
sum_x=0
for x in range (n):
    if x%3==0 or x%5==0:
        sum_x+=x
print(sum_x)