# ========================= Streamlit App =========================
import streamlit as st
from banking import Bank

st.title("🏦 Simple Bank Management System")

banking = Bank()

menu = st.sidebar.selectbox(
    "Select Action",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
)

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1, step=1)
    pin = st.text_input("Enter 4-digit PIN", type="password")

    if st.button("Create"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be 4 digits")
        else:
            info, msg = banking.create_ac(name, int(age), int(pin))
            if info:
                st.success(msg)
                st.json(info)
            else:
                st.error(msg)

elif menu == "Deposit":
    st.subheader("Deposit Money")
    acno = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1, step=1)

    if st.button("Deposit"):
        st.info(banking.deposit_m(acno, int(pin), int(amount)))

elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    acno = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1, step=1)

    if st.button("Withdraw"):
        st.info(banking.withdraw_m(acno, int(pin), int(amount)))

elif menu == "Show Details":
    st.subheader("Show Account Details")
    acno = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Show"):
        details = banking.show_detail(acno, int(pin))
        if details:
            st.json(details)
        else:
            st.error("No data found")

elif menu == "Update Details":
    st.subheader("Update Account Details")
    acno = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")
    new_name = st.text_input("New Name (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        msg = banking.update_detail(acno, int(pin), new_name, int(new_pin) if new_pin else None)
        st.info(msg)

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acno = st.text_input("Enter Account No")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Delete"):
        st.warning(banking.delete_ac(acno, int(pin)))
