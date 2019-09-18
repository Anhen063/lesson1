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