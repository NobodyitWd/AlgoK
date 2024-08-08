def InpValue(a,b,c):
    file = open(r"memory.txt","a",encoding="UTF-8")
    file.write(a+b+c+"\n") # Откроем файл памяти, запишем туда данные.
    file.close()
def Memory():
    i = 0
    list = [] # Список
    list1 = ""
    file = open(r"memory.txt","r",encoding="UTF-8")
    reader = file.read()
    while i != len(reader): # Пока все символы не в списке.
        if reader[i] == "\n": # Если символ равен переводу строки.
            list.append([list1]) # Добавь в список наши символы в временном списке.
            list1 = "" # Оставь временный список пустым.
        else:
            list1 += (reader[i]) # Иначе добавь в временный список текущий символ.
        i+=1
    file.close()
    return list
def MaximumOrder(far,maximum,id):
    MaximumOrders = []
    j = 0
    k = 0
    sort = sorted(far,reverse=True) # Отсортируй список расстояния.

    while sort[0] - sort[k] <= 2: # Если максимальное расстояние отличается от текущего на 2.
        k += 1 # Количество максимальных объектов +1.

    while j != k:
        maximum.append(sort[j]) # Добавь текущий максимальный объект в список.
        j += 1
    j = 0

    while j != len(far):
        if far[j] in maximum: # Если текущее расстояние является одним из максимальных.
            id.append(j) # Добавь его айди.
        j += 1

    j = 0
    while j != len(id):
        MaximumOrders.append(c[id[j]]) # Добавь заказы с максимальным расстоянием.
        j += 1

    return MaximumOrders

def Sr(MaximumOrders):
    sr = 0
    for i in MaximumOrders:
        sr += int(i) # Получаем сумму заказов с максимальным расстоянием.
    return sr/len(MaximumOrders) # Верни сумму деленную на количество заказов с максимальным значением.

print("Вписать данные - 1.\nОбработать данные - 2.")
options = input("Input value:   ")

if options == "1":
    a = input("Погода от 1 до 10:   ")
    b = input("Выходной - 1, рабочий день 0:   ")
    c = input("Количество заказов:   ")
    InpValue(a,b,c)

if options == "2":
    a = input("Погода от 1 до 10:   ")
    b = input("Выходной - 1, рабочий день 0:   ")
    now = a+b # Получаем текущее значение.
    far = []
    a = []
    b = []
    c = []
    j = 0
    maximum = []
    id = []

    for i in Memory(): # Считываем все значения.
        i = str(i)
        i = i[2:-2] # Избавляемся от скобок.
        a.append((i)[0]) # Распределим все по а,б,с.
        b.append((i)[1])
        c.append((i)[2:])

    while j != len(a):
        far.append(((int(now[0]) - int(a[j]))**2+(int(now[1]) - int(b[j]))**2)**0.5) # Формула Пифагора для вычисления расстояния в координатах.
        j += 1 # Запишем расстояние каждого значения из файла.

    vaiting = str(Sr(MaximumOrder(far,maximum,id))) # Получаем среднее значение среди максимальных координат.
    print("\nСегодня ожидаеться " + vaiting + " заказов.")
