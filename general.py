#Файлы.py
print('Привет мир!') #выводим надпись,помни кавычки
print('Привет, Программист!')
print(2+2)
print(10/3)
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
#Переменные
a=2; print(a+3)
name="ANHEN"; print(name)
# Списки
phones=['Za','Ds','Ar']
print(phones)
phones_count=len(phones) # считаем позиции
print(phones_count)
phones.append('Kg') # добавляем в список
print(phones)
print(phones.count('Kg'))# считаем количество 
print(phones.count('максим')) #нет в списке
print(phones[1])
print(phones[2:4]) # покажи с 2по4 не включительно
print(phones[:3])# покажи с 2п3 не включительно
print(phones[-1])# покажи последний
print( phones.index('Ar'))# узнаем индекс
phones.sort()# сортируем
print(phones)
print('Za'in phones) # оператор 
print('W'in phones)
phones=['Za','Ds','Ar','Ar']
print(phones)
del phones[1]#удалить из списка
print(phones)
phones.remove('Ar')# схлопнуть двойные
print(phones)
#Словари
product={'name':'Самсунг 5','stock':24,'prise':65432.1}
print(product)
print(len(product))
product['memory']=64 #Добавить элемент в словарь
print(product)
product['name']='Lenovo 6' #Замена существующего элемента
print(product)
print(product['prise'])
print(product['stock'])
print(product.get('name')) #если не известен ключ, можно обратитьсч через get
print(product.get('discount')) #такого ключа нет
print(product.get('discount',0)) #нон неудобно, если так то возвращает 0
print(product.get('counrty','US'))
del product['stock']
print(product)

#Сложение словарей и списков (список в соловарь)
phones=['Самсунг5','Леново7','Хуавей12']#Список
product['рекомендация']=phones
product["рекомендация"].append('Ксиоми8') # добавляем в список
print(len(product['рекомендация']))
print((product['рекомендация'][1]))

#Сложение словарей и списков (список словарей)
stock=[
    {'name':'Самсунг 5','stock':24,'prise':65432.1},
    {'name':'Самсунг 8','stock':15,'prise':65000.00},
    {'name':'Самсунг 9','stock':5,'prise':55000.00},
 ]
stock[0]['memory']=64 #добавила к 0 
stock[1]['name']='SSSS12'
phones=['Самсунг5','Леново7','Хуавей12']
stock[2]['рекомендация']=phones
del stock[1]['name']
print(stock)
print(type(stock))
print(type(stock[1]))

#Функции
price=100 #сложный путь
discount=5
price_with_discount=price-price*discount/100
print(price_with_discount)

def discounted(price, discount): # пишем функцию
    price_with_discount=price-(price*discount/100)
    print(price_with_discount)
discounnted(100,5) #вводим значения, считается само
discounnted(100,10)
discounnted(200,5)

def discounted(price, discount): #добавляем условие, что чкидка не большецены
    if discount>=100:
        price_with_discount=price
    else:
        price_with_discount=price-(price*discount/100)
    print(price_with_discount)

def discounted(price, discount): #добавляем условиу - цена положительная, вещественное
    price=abs(float(price))
    discount=abs(float(discount))
    if discount>=100:
        price_with_discount=price
    else:
        price_with_discount=price-(price*discount/100)
    print(price_with_discount)
discounnted(100,5)
discounnted(100,110)
discounnted(200,5)

def discounted(price, discount): 
    price=abs(float(price))
    discount=abs(float(discount))
    if discount>=100:
        price_with_discount=price
    else:
        price_with_discount=price-(price*discount/100)
    return(price_with_discount) # изменили - нужно возвращить значение и дальше с ним работать
p= discounted(100,5) #положили результат в переменную
print(p)

product={'name':'Самсунг 5','stock':24,'price':50000.00,'discount':5}
product['price_discounted']=discounted(product['price'],product['discount'])#передает нон разобраться
print(product)

def discounted(price, discount, max_discount=20 ):
    price=abs(float(price))
    discount=abs(float(discount))
    max_discount=abs(float(max_discount))
    if max_discount>99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount>=max_discount:
        return price
    else:
        return price-(price*discount/100)
p= discounted(19,21)
print(p)
