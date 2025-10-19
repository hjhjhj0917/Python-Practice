import random

dice = ['하나', '둘', '셋', '넷', '다섯', '여섯']

while True :
    choice = input("주사위 던지기를 진행하시겠습니까? (Yes or No) : ")

    if choice.lower() == 'yes' :
        print(random.choice(dice))
    elif choice.lower() == 'no' :
        break