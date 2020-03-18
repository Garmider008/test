#виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран;

import random
import numpy
#аналогічно робимо 2 масива з нулів, типу цілих чисел
a=numpy.zeros((3,3),dtype=numpy.int_)
for d in range(3):
    for e in range(3):
        a[d,e]=random.randint(-10,10)
b=numpy.zeros((3,3),dtype=numpy.int_)
for k in range(3):
    for l in range(3):
        b[k,l]=random.randint(-10,10)
#наперед створюємо масив з нулів для подільшої роботи з ним
C=numpy.zeros((3,3),dtype=numpy.int_)
print('Матриця А:   \n', a)# виводимо для наглядності наші матриці
print('Матриця В:  \n', b)
for d in range(3):
    for e in range(3):
        C[d,e]=a[d,e]*b[d,e]#потім через цикл перемножуємо намі матриці по елементно
print('Матриця С:  \n', C)# виводимо нову матрицю