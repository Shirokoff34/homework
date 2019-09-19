age = input("Сколько вам лет?")
age = int(age)

def occupation(age):
    if age <= 0 or age > 120:
        return "Введите корректный возраст"
    elif 0 < age <= 7:
        return "Привет, детский сад!"
    elif 7 < age <= 17:
        return "Здравствуй, школа!"
    elif 18 < age <= 23:
        return "Здорово студент!"
    else:
        return "Завод ждет тебя инженер!"

result = occupation(age)

print(result)



