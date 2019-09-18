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
