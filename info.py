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

#Задание к слайдам
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
