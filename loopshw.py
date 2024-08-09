while True:
    distance=int(input('What is your destination distance?'))
    age=int(input('How old are you?'))
    price=0

    if distance<1000:
        if age>=65:
            price=250
        elif age>=12 and age<=64:
            price=300
        else:
            price=200
    else:
        if age>=65:
            price=450
        elif age>=12 and age<=64:
            price=500
        else:
            price=400
    print('The price of your ticket is', price)