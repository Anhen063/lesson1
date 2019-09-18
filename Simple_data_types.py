#Простые типы данных
a=2; b=3; c=a+b;print(c)
a=2; b=3; c=a-b; print(c)
a=2; b=3; c=a*b; print(c)
a=2; b=3; c=a**b; print(c)
a=2; b=3; c=a/b; print(c)
a=2.5; b=3.1; c=a-b; print(c)
a=2.5; b=0.5; c=a-b; print(c)
a=3; b=0; c=a>b; print(c)#логические значения
a=3; b=0; c=a<b; print(c) #логические значения
a=3; b=0; c=a==b; print(c)  # равно
a=3; b=0; c=a!=b; print(c) #неравно
a='Привет'; b="Привет"; a==b
#Сложение строк
a="Привет"; b=" "; c="мир";print(a+b+c) #Можно так
a="Привет"; c="мир";print(a+" "+c+"!")
#Форматирование строк
a="Привет"; b="мир"; c= "{} {}!".format(a,b);print(c)
a="Привет"; b="мир";c=2; d="{} {}{}".format(a,b,c); print(d)
user="Миша"; b="Привет {name}!".format(name=user); print(b)
# или проще
user="Миша"; b=f"Привет {user}!"; print(b)
a="Привет"; b="мир";c=f"{a} {b}!"; print(len(c)) #считаем символы длина строки
a="Привет" .upper(); print(a) #делаем заглавные
a="Привет".lower(); print(a) #делаем строчные
a=" Привет ";print(a.strip()) #убираем пробелы
a="Привет".replace('е','3'); print(a) #меняем символы
a="ПриветS".replace('s',' '); print(a) #учитывай регистр
a="ПриветS".lower().replace('s','').capitalize(); print(a) #можно два условия, делаем строчную С и убираем
a="Привет мир!".replace('мир','python'); print(a) #Замена
a="learn.python.ru"; print(a.split(".")) #разбивам строку в список
a="learn python ru"; print(a.split(" ")) #тоже, разделитель пробел
a="learn python ru"; print(len(a.split())) #считаем слова в предложении
#NONE
a=None; b=0; print(a is None); print(b is None) #проверим на отсутсвие значения
a=2; print(type(a)) # узнать тип переменной
b="2.0"; print(type(b))
c=2.5222; print(type(a)) #уточнить, в мануале float, у меня int???
# Ввод от пользователя
name=input('Введите Ваше имя: '); print(f"Привет, {name}") #ввод от пользователя
age=int(input("Сколько Вам лет? ")); birth_year=2019-age; print(f"Вы родились в {birth_year} году")
#Приведение типов
a="2.0";b=float(a);print(type(b))