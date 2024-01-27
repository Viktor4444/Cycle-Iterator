# Cycle-iterator
## Двунаправеленный (цикличный) итератор списка

**Репозиторий для выполнения тествого задания*

### Задача 2.1
#### Дано:
Стандартная библиотека Python 3.10+


Произвольный одномерный массив типа [1, 2, 3, 4].
#### Нужно:
Создать класс, который примет данный массив в качестве аргумента и построит из него зацикленный итерируемый объект.


Реализовать 2 метода в этом классе, next() и prev() которые будут запоминать положение итерации по массиву и выдавать следующий или предыдущий элемент соответственно.

#### Результат:

Результат работы программы:

```
>>> a = CycleIterator([1, 2, 3])
>>> a.next()
1
>>> a.next()
2
>>> a.next()
3
>>> a.next()
1
>>> a.prev()
3
>>> a.prev()
2
```