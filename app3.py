import datetime
import streamlit as st

def calculate_detailed_age(birth_date):
    today = datetime.date.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_months = (today.month - birth_date.month) % 12
    age_days = (today - birth_date.replace(year=today.year)).days % 30  # Approximation
    return age_years, age_months, age_days

def get_historical_fact(year):
    # This is a mock function. In a real app, you might query a historical database or API.
    facts = {
        1990: "Hubble Space Telescope was launched.",
        2000: "The Y2K bug turned out to be less severe than expected.",
        2010: "Instagram was launched.",
    }
    return facts.get(year, "No significant event recorded.")

st.title('Advanced Age Calculator')

st.write('Enter your birth date:')

birth_date = st.date_input("Birth Date")

if st.button('Calculate Age'):
    age_years, age_months, age_days = calculate_detailed_age(birth_date)
    historical_fact = get_historical_fact(birth_date.year)

    st.write(f'You are **{age_years} years, {age_months} months, and {age_days} days** old.')
    st.write(f'Did you know? In your birth year, {historical_fact}')
