import random

print('who is gonna clean the floor')

student_list = ['Fulano', 'Ciclano', 'Beltrano', 'Urano']
cleaner_student = random.choice(student_list)

print(f'{cleaner_student}, is gonna clean the floor')

random.shuffle(student_list)

print(student_list)