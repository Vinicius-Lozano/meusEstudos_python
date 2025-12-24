# Calculus 2 !
import math, random 

print("hypotenuse")

x_coordinate = int(input('x coordinate '))
y_coordinare = int(input('y coordinate '))

print('hypotenuse is {:.2g}'.format(math.hypot(x_coordinate, y_coordinare)))

# exercise 18

print('sin, cos, tan')

angle = float(input('give me a angle: '))
radian =  math.radians(angle)

print('on {:g}° sin is {:.2g} cos is {:.2g} tan is {:.2g}.'.format( angle, math.sin(radian), math.cos(radian), math.tan(radian) ) )

# exercise 19

print('who is gonna clean the floor')

student_list = ['Fulano', 'Ciclano', 'Beltrano', 'Urano']
cleaner_student = random.choice(student_list)

print(f'{cleaner_student}, is gonna clean the floor')

# exercise 20

print('presentarion order')

random.shuffle(student_list)

print('order of presentation is:', student_list)