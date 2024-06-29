import random
import time

def startGame():

    userLife = 4
    botLife = 4
    userMove = True
    botMove = False

    
    while userLife > 0 and botLife > 0:
        global bullets

        if not bullets:
            singleNum = random.randint(1, 4)
            combatNum = random.randint(1, 4)

            single = ['Single' for i in range(singleNum)]
            combat = ['Combat' for i in range(combatNum)]


            bullets = single + combat

            random.shuffle(bullets)

            print("Киллер Джен: Я вставляю патроны в случайном порядке.")
            time.sleep(2)
            print(str(len(combat)) + " Боевой(-ых). " + str(len(single)) + " Холостой(-ых)")
            time.sleep(2)
            print("Всё готово. Игра началась.")
        if userMove == True and botMove == False:
            time.sleep(1)
            print("Ваш ход.")
            time.sleep(1)
            choiseTarget = input("В кого выстрелить? Он/Вы: ")

            if choiseTarget == 'Вы':
                if bullets[0] == "Combat":
                    userMove = False
                    botMove = True
                    userLife -= 1
                    bullets.pop(0)
                    time.sleep(2)
                    print("Вы выстрелили в себя боевым. Теперь у вас осталась " + str(userLife) + " жизнь")
                else:
                    bullets.pop(0)
                    time.sleep(2)
                    print("Вам повезло. Это был холостой.")
            elif choiseTarget == 'Он':
                if bullets[0] == 'Combat':
                    botLife -= 1
                    bullets.pop(0)
                    time.sleep(2)
                    print("Вам повезло. Вы выстрелили в Джена боевым, оставя ему " + str(botLife) + " жизнь")
                else:
                    userMove = False
                    botMove = True
                    bullets.pop(0)
                    time.sleep(2)
                    print("Вы выстрелили холостым. Готовьтесь")
        

        if botMove == True and userMove == False:
            choiceBot = random.randint(0, 1)

            if len(bullets) > 1:
                if choiceBot == 0: # В себя
                    if bullets[0] == 'Combat':
                        userMove = True
                        botMove = False
                        bullets.pop(0)
                        botLife -= 1
                        time.sleep(2)
                        print("Вам повезло. Киллер Джен выстрелил в себя боевым, оставя себе " + str(botLife) + " жизнь")
                    else:
                        bullets.pop(0)
                        time.sleep(2)
                        print("Киллер Джен выстрелил в себя холостым. Готовьтесь")
                else: # В игрока
                    if bullets[0] == 'Combat':
                        userMove = True
                        botMove = False
                        userLife -= 1
                        bullets.pop(0)
                        time.sleep(2)
                        print("Киллер Джен выстрелил в вас боевым. У вас осталась " + str(userLife) + " жизнь")
                    else:
                        userMove = True
                        botMove = False
                        bullets.pop(0)
                        time.sleep(2)
                        print("Киллер Джен выстрелил в вас холостым. Вам повезло")
            elif bullets[0] == 'Single':
                bullets.pop(0)
                time.sleep(2)
                print("Киллер Джен выстрелил в себя холостым. Готовьтесь")
            elif bullets[0] == 'Combat':
                userLife -= 1
                bullets.pop(0)
                time.sleep(2)
                print("Киллер Джен выстрелил в вас боевым. У вас осталась " + str(userLife) + " жизнь")
        if userLife <= 0:
            return print("Вы проиграли!")
        elif botLife <= 0:
            return print("Вы выиграли!")

bullets = []

userName = input("Добро пожаловать. Я Киллер Джен. Подпиши отказ от претензий (Введи имя): ")
time.sleep(1)
print("Отлично! Желаете начать игру? Да/Нет")
choiceUser = input()
time.sleep(1)

if choiceUser == 'Нет':
    time.sleep(1)
    print("Как хотите. Можете покинуть зону исполнения кода.")
elif choiceUser == 'Да':
    print("ПОМЕТКА. Киллер Джен ПРОПУСТИТ ХОД, ЕСЛИ ВЫ ВЫСТРЕЛИТЕ В СЕБЯ ХОЛОСТЫМ. Для вызова помощи пишите @t.help")
    time.sleep(1)
    print("Чудесно! Начнём же...")
    
    startGame()
else:
    time.sleep(1)
    print("Такие ответы не принимаются.")

