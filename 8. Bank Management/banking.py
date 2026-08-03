import json
import random
import string
from pathlib import Path
import streamlit as st




class Bank:
    database = 'data.json'
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            with open(database, 'w') as fs:
                json.dump([], fs)
    except Exception as e:
        st.error(e)

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data, indent=4))

    @classmethod
    def __acgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        special = random.choices("!@#$%&", k=1)
        ac_id = alpha + num + special
        random.shuffle(ac_id)
        return "".join(ac_id)

    def create_ac(self, name, age, pin):
        info = {
            "name": name,
            "age": age,
            "pin": pin,
            "acno": Bank.__acgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            return None, "You can't create your account"
        else:
            Bank.data.append(info)
            Bank.__update()
            return info, "Account has been created successfully"

    def deposit_m(self, acno, pin, amount):
        userdata = [i for i in Bank.data if i['acno'] == acno and i['pin'] == pin]

        if not userdata:
            return "No data found"
        if amount > 10000 or amount <= 0:
            return "You can deposit only between 1 and 10000"
        userdata[0]['balance'] += amount
        Bank.__update()
        return "Amount deposited successfully"

    def withdraw_m(self, acno, pin, amount):
        userdata = [i for i in Bank.data if i['acno'] == acno and i['pin'] == pin]

        if not userdata:
            return "No data found"
        if userdata[0]['balance'] < amount:
            return "Insufficient balance"
        userdata[0]['balance'] -= amount
        Bank.__update()
        return "Amount withdrawn successfully"

    def show_detail(self, acno, pin):
        userdata = [i for i in Bank.data if i['acno'] == acno and i['pin'] == pin]
        if not userdata:
            return None
        return userdata[0]

    def update_detail(self, acno, pin, new_name=None, new_pin=None):
        userdata = [i for i in Bank.data if i['acno'] == acno and i['pin'] == pin]
        if not userdata:
            return "No such user found"

        if new_name:
            userdata[0]['name'] = new_name
        if new_pin:
            userdata[0]['pin'] = new_pin

        Bank.__update()
        return "Details updated"

    def delete_ac(self, acno, pin):
        userdata = [i for i in Bank.data if i['acno'] == acno and i['pin'] == pin]
        if not userdata:
            return "Sorry no such data exist"
        Bank.data.remove(userdata[0])
        Bank.__update()
        return "Account deleted successfully"


