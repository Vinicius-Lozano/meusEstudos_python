# Calculus!
    # exercise 5

print('I know before and after')

n = int(input('give me a number: '))
nb= n-1
na= n+1

print(f'before {n} comes {nb} and after that goes {na}')
 
    # exercise 6

print('i can give you double, triple even square root')

n2 = int(input('give me a number again '))

nd  =  n2*2
nt  =  n2*3
nsr =  n2**(1/2) 

print('double of {} is {}, triple {}, square root {:.3f}'.format(n2, nd, nt, nsr))

    # exercise 7 

print('for a dummy like you i can give even a average between two tests')

n3 = int(input('first test result: '))
n4 = int(input('second test result: '))

nm = (n3+n4)/2

print('your avarage is: {:.1f}'.format(nm))

    # exercise 8 

print('i will just convert Meters to cm an mm now')

n5 = int(input('how much meters? '))

ncm = n5*100
nmm = n5*1000

print('{} meters is {} centimeters or {} millimeters'.format(n5, ncm, nmm))

    # exercise 10

print('i will convert  R$ to US$ ')
n6 = int(input('how much R$ do you have: '))
nus = n6/4.99

print('you can buy {:.2f} US dollars'.format(nus))

    # exercise 11

print("let's paint your wall. give me the dimensions! (in meters)")

n7 = int(input('width: '))
n8 = int(input('height: '))
np = (n7*n8)/2

print('you will need {:.1f} liters of paint'.format(np))






