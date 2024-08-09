email=input('Enter your email address:')
result=''
for i in email:
    if i=='@':
        print(result)
        break
    else:
        result+=i
