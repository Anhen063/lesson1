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
print(product.get('discount',0)) #нон неудобно, если так то возвращает 0 добавить по умолчанию
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

#Задание Словари
distion={'city':'Москва','temperature':20,}
print(distion['city'])
distion['temperature']=distion['temperature']-5
print(distion)
print(distion.get('country'))
print(distion.get('country','Москва'))
distion['date']='27.05.2019'
print(len(distion))
print(distion)