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

#Практика к Список
spisok=['3','5','7','9','10.5']
print(spisok)
spisok.append('Python')
spisok_count=len(spisok)
print(spisok_count)
print(spisok[0])
print(spisok[-1])
print(spisok[1:5])
print(spisok.index('Python'))
del spisok[5]
print(spisok)

#Практика Словари
distion={'city':'Москва','temperature':20,}
print(distion['city'])
distion['temperature']=distion['temperature']-5
print(distion)
print(distion.get('country'))
print(distion.get('country','Москва'))
distion['date']='27.05.2019'
print(len(distion))
print(distion)

#Практика к Переменные
name="ANHEN"; print(name)
user_info={
    'first_name': 'АННА',
    'last_name':'Елхимова'
    }
print(user_info['first_name'])

#Практика к функция
def get_summ(one, two, delimited='&'):
    one=str(one)
    two=str(two)
    return one+delimited+two
p=get_summ('Learn', 'python').upper()
print(p)

def format_price(price):
    price=int(price)
    return f'Цена {price} руб.'
a=format_price(56.24)
print(a)
