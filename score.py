'''
Оценки
Создать список из словарей с оценками учеников разных классов школы вида
[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

school_score = [{"school_class": "4a", "scores": [3,4,4,5,2]}, 
				{"school_class": "4б", "scores": [2,3,4,4,5]},
				{"school_class": "4в", "scores": [3,2,3,4,4]},
				{"school_class": "4г", "scores": [4,3,2,3,4]},
				{"school_class": "4д", "scores": [5,4,3,2,3]}]

# GPA - grade point average

gpa_school = 0
count = 0
for i in school_score:
	gpa_school += sum(i.get("scores"))/len(i.get("scores"))
	count += 1

print(gpa_school/count) # Средняя по школе

for i in school_score:
	print(i.get("school_class") + " " + str(sum(i.get("scores"))/len(i.get("scores")))) # Средняя по ученикам в школе



