from pathlib import Path
import os
import shutil
import csv
import json

def folder():
    p=Path('.')
    items=list(p.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfold():
    folder()
    name=input("Enter Folder Name : ")
    p=Path(name)

    if not p.exists():
        os.mkdir(name)
        print("Folder Created")
    else:
        print("Folder Already exist")


def readfold():
    folder()
    name=input("Enter Folder Name : ")
    p=Path(name)

    if p.exists() and p.is_dir():
        files=os.listdir(p)
        print(f"Contents of {p}:")
        for f in files:
            print(" ", f)
    else:
        print("Folder Not Found")


def updatefold():
    try:
        folder()
        name=input("Enter Folder Name which do you want to update  : ")
        p=Path(name)

        if p.exists() and p.is_dir():
            print("Prss 1 for Rename Folder : ")
            print("Prss 2 for Listing the Folder : ")
            print("Prss 3 for Moving Files From the Folder : ")
            print("Prss 4 for copying Files From the Folder : ")
            print("Prss 5 for Adding New Files In the Folder : ")
            print("Prss 6 for Deleting Files : ")

            res=int(input("Which operation do you Want to perform : "))
            if res==1:
                name2=input("Enter New Folder Name")
                p2=Path(name2)
                p.rename(p2)
        
            if res==2:
            
                if p.exists() and p.is_dir():
                    files=os.listdir(p)
                    print(f"Contents of {p} :")
                    for f in files:
                        print(" ", f)
                else:
                    print("Folder Not Found")
        
            if res==3:
                if p.exists() and p.is_dir():
                    file_to_move = input("Enter file path you want to move: ")
                    dest_folder = input("Enter destination folder path: ")
                    shutil.move(file_to_move, dest_folder)
                    print("File Moved")
                else:
                    print("File already Moved") 
        
            if res==4:
                if p.exists() and p.is_dir():
                    file_to_move = input("Enter file path you want to copy: ")
                    dest_folder = input("Enter destination folder path: ")
                    shutil.copy(file_to_move, dest_folder)
                    print("File Copied")
                else:
                    print("File already Copied") 
        

            if res==5:
                file_obj=input("Enter File :")
                if file_obj.suffix.lower()==".csv":    
                    w=csv.writer(f)
                data = [["Name","Course","Fee"],     
                    ["Yunsu","DS","20000"],
                    ["Neha","DA","15000"]]
                for i in data:
                    w.writerow(i)
            else:
                    data1={"Name":"Yunsu",
                        "Age":23,
                        "is_adult":True}
                    json.dump(data1,f)

                    
                    
            if res==6:
                file_name = input("Enter Name : ")
                file_path = p / file_name   # folder ke andar ka file

                if os.path.exists(file_path):
                    os.remove(file_path)
                    print("File deleted successfully!")
                else:
                    print("File does not exist.")
             
    except  Exception as e:
        print(e)                      
                
        
def deletefold():
    try:
        folder()
        name=input("Enter New Folder Name")
        p=Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder Deleted")  
        else:
            print("Folder Not Deleted")   
    except Exception as e:
        print(e)        
              
    
          




print("Prss 1 for Creating Folder : ")
print("Prss 2 for listing the Folders : ")
print("Prss 3 for Updating Folder : ")
print("Prss 4 for Deleting Folder : ")


check=int(input("Enter yor choice : "))

if check==1:
    createfold()


if check==2:
    readfold()

if check==3:
    updatefold()

if check==4:
    deletefold()
