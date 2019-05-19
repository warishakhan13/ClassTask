num=int(input("Enter number:"))
if num ==1 or num <=0:
    print(num,"is not prime")
elif num==2:
   print(num, 'is prime')
else:
    iter = 1
    for i in range(2,num):
        iter += 1
        if num % i ==0:
         break
    if iter == (num-1):
        print(num,'is prime')
    else:
        print(num,'is not prime')