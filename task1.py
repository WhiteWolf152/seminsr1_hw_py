#1- Напишите программу, которая принимает на вход
#  цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

num_day = int(input('Введите день недели: '))
if num_day == 1:
    print('нет, рабочий день')
elif num_day == 2:
    print('нет, рабочий день')
elif num_day == 3:
    print('нет, рабочий день') 
elif num_day == 4:
    print('нет, рабочий день') 
elif num_day == 5:
    print('нет, рабочий день')
elif num_day == 6:
    print('Да, выходной день')
elif num_day == 7:
    print('Да, выходной день')
else:
    print('такого дня нет')
