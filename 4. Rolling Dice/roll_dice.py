import random
tries=0
while True:
    choice=input("Roll the Dice (y/n) : ").lower()
    if choice=='y':
        how_often=int(input('How many Dices Do You Want To Roll :'))
        tries+=1    
        rolls=[random.randint(1,6) for _ in range(how_often)]
        print(','.join(map(str,rolls)))
           
    elif choice=='n':
            print(f'You Roll Dice in {tries}...\nThanks For Playing 😍🤩🎉')
            break
    else:
            print('Invalid Choice ⚠')