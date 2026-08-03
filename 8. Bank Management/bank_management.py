import json
import random
import string
from pathlib import Path


class Bank:
    database='data.json'   #path name
    data=[]         #dummy data file
    try:
        if Path(database).exists():  #file exist ho toh
            with open(database) as fs:          #data.json open kiya jo database variable store hai
                data=json.loads(fs.read())      #ab us json ko rad kiya then load kiya in that data(dummy data)
        else:
            print('no file exist')
    except Exception as e:
        print(e)


    @classmethod       #call through class
    def __update(cls):
        with open(cls.database,'w') as fs:          #data.json(Bank.database) main write hoga
            fs.write(json.dumps(cls.data,indent=4))     
            #jo dummy data=[](Bank.data) # banaya usko dump kro data.json file main


    @classmethod        #ac generate
    def __acgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        special=random.choices("!@#$%&",k=1)
        id=alpha+num+special
        random.shuffle(id)
        return "".join(id)
    
        

    def create_ac(self):
        info={
            "name":input("please tell your name :"),
            "age":int(input("tell your age : ")),
            "pin":int(input("tell your pin : ")),
            "acno":Bank.__acgenerate(),
            "balance":0
        }

        if info['age']<18 or len(str(info['pin']))!=4:  
            #info ke pin convert into str because for not greater and less than 4
            print("You can't create your ac")
        else:
            print('ac has been created')
            for i in info:
                print(f"{i} : {info[i]}")
            print('note down your ac no...')


            Bank.data.append(info)          
            #Bank.data(data=[]) us info ko add kr do
            Bank.__update()       
            #staticmethod : call directly through class

    def deposit_m(self):
        ACNO=input("please tell your ac no : ")
        PIN=int(input("please tell your pin no : "))

        userdata=[i for i in Bank.data if i['acno']==ACNO and i['pin']==PIN]

        if userdata==False:
            print('No data found')
        else:
            amount=int(input('how much you want to deposit : '))
            if amount>10000 or amount<0:
                print('sorry you can not deposite money greater than 10000')
            else:
                print(userdata)
                userdata[0]['balance']+=amount
                Bank.__update()
                print('amount deposited successfully')



    def withdraw_m(self):
        ACNO=input("please tell your ac no : ")
        PIN=int(input("please tell your pin no : "))

        userdata=[i for i in Bank.data if i['acno']==ACNO and i['pin']==PIN]

        if userdata==False:
            print('No data found')
        else:
            amount=int(input('how much you want to withdraw : '))
            if userdata[0]['balance'] < amount:
                print("sorry you don't hava that much money")
            else:
                print(userdata)
                userdata[0]['balance']-=amount
                Bank.__update()
                print('amount withdrew successfully')
    

    def show_detail(self):
        ACNO=input("please tell your ac no : ")
        PIN=int(input("please tell your pin no : "))
        userdata=[i for i in Bank.data if i['acno']==ACNO and i['pin']==PIN]

        print('Your Info....\n')
        # print(userdata)
        for i in userdata[0]:
            print(f'{i} : {userdata[0][i]}')

    def update_detail(self):
        ACNO=input("please tell your ac no : ")
        PIN=int(input("please tell your pin no : "))

        userdata=[i for i in Bank.data if i['acno']==ACNO and i['pin']==PIN]

        if userdata==False:
            print('no such user found')
        else:
            print(" you can't change age, balance, Acount No")
            print("fill the details for change or leave it empty if it's not change")

            newdata={
                'name':input('please tell your new name : '),
                'pin':int(input('please tell your new pin : '))
            }

            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['pin']=="":
                newdata['pin']=userdata[0]['pin']

            newdata['age']=userdata[0]['age']
            newdata['acno']=userdata[0]['acno']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print('details updated')

    def delete_ac():
        ACNO=input("please tell your ac no : ")
        PIN=int(input("please tell your pin no : "))

        userdata=[i for i in Bank.data if i['acno']==ACNO and i['pin']==PIN]

        if userdata==False:
            print("Sorry no such data exist")
        else:
            check=input("press y/n :").lower()
            if check=='n':
                print('By passed')
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print('ac deleted ')
                
                Bank.__update()






b=Bank()

print("press 1 for create an Account : ")
print("press 2 for Deposite an Account : ")
print("press 3 for withdraw an Account : ")
print("press 4 for Details an Account : ")
print("press 5 for Update an Account : ")
print("press 6 for Delete an Account : ")



ask_user=int(input("What Do Want to do : "))

if ask_user==1:
    b.create_ac()
if ask_user==2:
    b.deposit_m()
if ask_user==3:
    b.withdraw_m()
if ask_user==4:
    b.show_detail()
if ask_user==5:
    b.update_detail()
if ask_user==6:
    b.delete_ac()