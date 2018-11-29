'''
Сравнение строк
Написать функцию, которая принимает на вход две строки
Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
Если строки одинаковые, вернуть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты
'''

def comparison_string(string1, string2):
	if type(string1) != str or type(string2) != str:
		return 0
	elif string1 == string2:
		return 1
	elif string1 != string2 and len(string1) > len(string2):
		return 2
	elif string1 != string2 and string2 == "learn":
		return 3
	else:
		return "Условия не выполнены для: " + string1 + " " + string2

print(comparison_string("str", 123)) # 0
print(comparison_string("str","str")) #1
print(comparison_string("str_large","str")) #2
print(comparison_string("str", "learn")) #3
print(comparison_string("str", "learn23")) # Условия не выполнены для: str learn23