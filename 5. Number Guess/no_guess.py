import random
n=random.randint(1,100)
tries=0
while True:
    try:
        print('Enter No Between 1 - 100')
        guess=int(input('Enter No : '))
        tries+=1
        if n<guess:
            print('Go Lower')    
        elif n>guess:
            print('Go Higher')
        else :
            print(f'Congrats You Win 🎊🎉 in {tries} Trial')
            break 
    except ValueError:
        print('Invalid No :')