a = input("Введите строку: ") #Вводим строку
count = 0 #Счетчик
for i in a: #Перебор
    if "и" == i.lower(): #Условие
        count += 1
print("Буква и встречается: " + str(count) + " раз") #Вывод
