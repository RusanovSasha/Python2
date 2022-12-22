# ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
#10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

def printElements(elem):
    lengthElem = len(elem)-1
    print('[', sep='', end='')
    for i in range(len(elem)):
        print(elem[i], sep='', end='')
        if i!=lengthElem:
            print(',', sep='', end='')
    print(']')
    return

def shuflyShufly(elemSuf):
    lengthElem = len(elemSuf)
    for i in range(len(elemSuf)):
        randomJumpTo = random.randint(0, lengthElem-1)
        boxElem = elemSuf[randomJumpTo]
        elemSuf[randomJumpTo] = elemSuf[i]
        elemSuf[i] = boxElem
    return elemSuf

print('Привет, введите целое число N, а я выдам список из n чисел, а затем перемешаю его!')
n = int(input())

elements = list(range(n+1))

print()
print('Получившийся список:')
printElements(elements)

print()
print('Перемешанный список:')

newElements = shuflyShufly(elements)

printElements(newElements)