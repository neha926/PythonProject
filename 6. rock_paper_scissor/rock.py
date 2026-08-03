import random


ROCK='r'
SCISSOR='s'
PAPER='P'
# dict for emoji
emoji={ROCK:'♟',SCISSOR:'✂',PAPER:'📰'} 

ch=tuple(emoji.keys())

def get_user_ch():
    while True:
        
        u_inp=input('Enter Rock/Paper/Scissor (r/p/s) : ').lower()
        if u_inp in ch:
            return u_inp
        else:
            print('Invalid Choice⚠')


def display_ch(u_inp,com_ch):

        print(f'You Choose {emoji[u_inp]}')
        print(f'Com Choose {emoji[com_ch]}')


def determine_win(u_inp,com_ch):
        if u_inp==com_ch:
            print('Tie Match')
            return 'tie'
            
        elif(
            (u_inp==ROCK and com_ch==SCISSOR)or
            (u_inp==PAPER and com_ch==ROCK)or
            (u_inp==SCISSOR and com_ch== PAPER)):
            print('You Win 🤩🎊')
            return 'user'
            
        else:
            print('You Lose ☹⭕')
            return 'comp'
            
     
def main():
    while True:
        u_tries=0
        c_tries=0
        tie=0
        tries=0
        while tries<3:
             u_inp=get_user_ch()
             com_ch=random.choice(ch)

             display_ch(u_inp,com_ch)
             
             result=determine_win(u_inp,com_ch)           
             if result=='user':
                  u_tries+=1
             elif result=='comp':
                  c_tries+=1
             else:
                  tie+=1
                  

             tries+=1
             if tries<3:
                play_again=input("Do you want to play Next Round. You Have 3 chances : (y/n) : ").lower()
                if play_again=='n':
                    print('Thanks For Playing Game❤')
                    break
        

        print("\n📊 Final Scoreboard 📊")
        print(f"You Won      : {u_tries}")
        print(f"Computer Won : {c_tries}")
        print(f"Tie Matches  : {tie}")
        if u_tries>=2:
             print('\nSo You are win 😍')
        else:
             print('\nSo Com is win 💻')


        restart = input("\nDo you want to restart the game? (y/n): ").lower()
        if restart == 'n':
            print("Goodbye 👋")
            break
main()
