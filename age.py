'''
Возраст
Попросить пользователя ввести возраст при помощи input и положить результат в переменную
Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
учиться в детском саду, школе, ВУЗе или работать
Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
Вывести содержимое переменной на экран
'''

user_age = int(input("Enter yor age - "))
def age_detect_work(age):
	if age <= 0:
		return "Imposible age"
	elif age < 7:
		return "Kindergarten"	
	elif age < 19:
		return "School"
	elif age < 25:
		return "University"
	else:
		return "Job"

detected_work = age_detect_work(user_age)
print(detected_work)

