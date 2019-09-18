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