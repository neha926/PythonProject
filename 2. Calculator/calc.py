His_file="history.txt"


def show_his():
    file=open(His_file,'r')
    lines=file.readlines()
    if len(lines)==0:
        print('No History Found!!!')
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
print(show_his())
def clear_his():
    file=open(His_file,'w')
    file.close()
    print('History Cleared!')


def save_his(equation,result):
    file=open(His_file,'a')
    file.write(equation+ " = " +str(result)+ "\n")
    file.close()
    



def calc(u_inp):

    temp="" 
    for ch in u_inp:
        if ch.isdigit() or ch in "+-/*":
            temp+=ch
        elif ch==" ":
            temp+=" "

    parts=temp.split()
    if len(parts)!=3:
        print("Invalid input, Use Format 1 + 1")
        return
    n1=float(parts[0])
    op=parts[1] 
    n2=float(parts[2])

    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    elif op=='/':
        if n2==0:
            print("Can't Divide By Zero")
            return
        result=n1/n2
    else:
        print('Invalid Operator, Use Only + - * /')
        return
    
    if int(result)==result:
        result=int(result)
    print('Result : ',result)
    save_his(u_inp,result)



def main():
    print('-----Simple Calculatoe----')
    while True:
        u_inp=input("Enter No for Calculations, Use Format 1+1 : ")

        if u_inp=='exit':
            print('GoodBye')
            break
        elif u_inp=='history':
            show_his()
        elif u_inp=='clear':
            clear_his()
        else:
            calc(u_inp)

main()
        
