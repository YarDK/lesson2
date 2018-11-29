'''
Задание
Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
писала пользователю "Пока!" и завершала работу при помощи оператора break
'''
def ask_user_v():
	ask = ""		
	while ask != "Хорошо":
		try:
			ask = input("Как дела? ")
		except KeyboardInterrupt:
			print("\n\n" + "Пока!\n")
			break
	return None

ask_user_v() # Останавливается, если ответить "Хорошо" или нажать ctrl + c


