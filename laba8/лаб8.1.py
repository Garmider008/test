#1.Напишіть програми, що виконують такі операції з масивами (використовувати
#вбудовані методи по роботі з масивами заборонено):
#виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотному порядку;

#Модуль для масивів
import numpy
#Стрічка
a=int(input('Введіть кількість стрічок:'))
#Стовпчик
b=int(input("Введіть кількість стовпчиків:"))
#Створюємо масив з нулів, типу цілих чисел
c=numpy.zeros((a,b),dtype=numpy.int_)
#проходимось по кожному елементу стрічки почитаючи з останього в зворотньому порядку, з кроком -1, а-1 потому ранж не проходить останню ітерацію
for d in range(a-1,-1,-1):
    #аналогічно і тут для стовпців
    for e in range(b-1,-1,-1):
        #програма проходить по кожній ітерації з значень, які вводить користувач, і так як в задані вказано що потрібно у зворотньому порядку, то ми міняємо порядок е та д
        c[d,e]=int(input('A['+str(e+1)+','+str(d+1)+']='))
print(c)#Ввиводимо нашу матрицю