health_insurance=input('Have you paid health insurance?:')
donations=input('Have you made charitable donations?:')
income=int(input('Enter your income:'))
tax=0
if health_insurance=='yes':
    income=income*0.95
if donations=='yes':
    income=income*0.9
if income<=10000:
    tax=0
elif income>=10001 and income<=50000:
    tax=0.1*income
else:
    tax=0.2*income
print('Your tax is',tax)
    
