<<<<<<< HEAD
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
=======
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
>>>>>>> 60a4b3d8eb97b3b96b630f63b8774d5df49c560f
            print('Invalid Choice ⚠')