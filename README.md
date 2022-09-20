# Iterators-Generators-Yield
Домашнее задание к лекции 2.«Iterators. Generators. Yield»
Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Например
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item) #  
Должен отпечататься каждый элемент каждого вложенного списка

'a' 
'b' 
'c' 
'd'
'e'
'f'
'h'
False
1
2
None
а комперхеншн, выражение вернет плоский список flat_list = [item for item in FlatIterator(nested_list)]

во flat_list должен быть такой список: ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

Написать генератор, который принимает список списков, и возвращает их плоское представление. Например
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for item in  flat_generator(nested_list):
	print(item)
Должен отпечататься каждый элемент каждого вложенного списка
