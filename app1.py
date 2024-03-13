import datetime
import streamlit as st

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

st.title('Age Calculator')

birth_input = st.text_input('Enter your birth date (YYYY-MM-DD):')

if birth_input:
    try:
        birthdate = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
        age = calculate_age(birthdate)
        st.write(f'You are {age} years old.')
    except ValueError:
        st.write('Please enter a valid date in the format YYYY-MM-DD.')
