#Практика Числа
a,c=(2,2.5); b=c-a; print(a,b,c)

#Практика Строки
a="Привет"; name="АНЯ"; c=" "; d="!"; e=",";print(a+e+c+name+d) #сложение строк
a="Привет"; name="АНЯ";print(a+" "+","+name+"!") #или так
name="АНЯ"; b=f"Привет, {name}!"; print(b) #Форматирование

#Практика числа
v=int(input("Введите число от 1 до 10: "))
v+=10
print(v)

#Практика Строки
name=str(input('Введите Ваше имя: '))
print(f"Привет, {name}! Как дела?")

#Практика Приведение типов
print(float("1")); print(type(float("1")))
#print(int('2,5')); print(type(int('2,5'))) ошибка????
print(bool("1")); print(type(bool("1")))
print(bool("")); print(type(bool("")))ы
print(bool(0)); print(type(bool(0)))