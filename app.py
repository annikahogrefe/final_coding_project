import streamlit as st

# Page Configuration
st.set_page_config(page_title="PyFit", page_icon="💪")

# App Headers
st.title("PyFit 🏋️‍♂️ Your Personal Workout Planner")
st.write("Welcome! Answer the questions below, and we will build a custom routine for you.")

# Browser Tab Display
st.set_page_config(
    page_title="PyFit",
    page_icon="💪")

# visual divider line to keep things clean
st.divider()

# Question 1: Fitness Goals
st.header("1. What is your goal?")
goal = st.selectbox(
    "Select your primary fitness objective:",
    ["Build Muscle", "Increase Strength", "Lose Body Fat / Toning", "Improve Endurance"]
)

# Question 2: Frequency
st.header("2. Availability")
days = st.slider(
    "How many days per week do you want to go to the gym?",
    min_value=1,
    max_value=7,
    value=3  # default starting position of the slider
)

# Question 3: Muscle Prioritization
st.header("3. Muscle Focus")
priorities = st.multiselect(
    "Are there specific muscle groups you want to prioritize? (Select all that apply)",
    ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"]
)

st.divider()

# The Action Button
# For now, it just prints a confirmation message when clicked
if st.button("Generate My Plan", type="primary"):
    st.success("Inputs received successfully! Ready for the next step.")