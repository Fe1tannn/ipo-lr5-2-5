a = input("Введите строку: ")
count = 0
for i in a:
    if "и" == i.lower():
        count += 1
print("Буква и встречается: " + str(count) + " раз")
