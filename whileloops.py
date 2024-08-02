ecounter=0
ocounter=0
while True:
    num=int(input('Enter a number:'))
    if num!=0:
        if num%2==0:
            ecounter+=1
        else:
            ocounter+=1
    else:
        break
print('The number of odd numbers is',ocounter)
print('The number of even numbers is',ecounter)