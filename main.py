from random import *

edge = 0


def valid_granica(num):
    return num.isdigit() and int(num) / float(num) == 1.0


def is_valid(num):
    global edge
    flag = True
    if not num.isdigit() or int(num) / float(num) != 1.0:
        flag = False
    return flag and 0 < int(num) <= edge


def more():
    sv = input("Не хочешь ли еще раз?      ")
    if sv.lower() in ["да", "ага", "конечно", "хочу"]:
        igra()
    elif sv.lower() in ["нет", "неа", "не хочу"]:
        pass
    else:
        sv = input("Не понял, так ты хочешь? Ответь понятнее..    ")
        more()


def igra():
    global edge
    print("Добро пожаловать в числовую угадайку! ")
    edge = input("Давайте придумаем, от 1 до какого числа будет число, которое я загадаю, а ты отгадаешь!   ")
    while not valid_granica(edge):
        edge = input("А может быть всё-таки введём целое положительное число?")
    edge = int(edge)
    chislo = randint(1, edge)
    n = 1
    while True:
        vvod = input("Какое число я загадал?   ")
        if not is_valid(vvod):
            print("А может быть всё-таки введём целое число от 1 до 100 ?")
        else:
            if int(vvod) < chislo:
                print(vvod, " - Ваше число меньше загаданного, попробуйте еще разок")
                n += 1
            elif int(vvod) > chislo:
                print(vvod, " - Ваше число больше загаданного, попробуйте еще разок")
                n += 1
            else:
                print("Вы угадали, поздравляем!")
                break
    print("Спасибо что играли в числовую угадайку! Вы пытались угадать", n, "раз! Еще увидимся..")
    more()


igra()
