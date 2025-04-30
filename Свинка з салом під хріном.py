list = ["Порося","Свинка","Сало","Кабанчик"]

while True:
    x = input("Введи індекс ходяче сало - ")

    try:
        res = list[int(x)]
        break
    except:
        print("Порося тупе")
        continue

print(res)

