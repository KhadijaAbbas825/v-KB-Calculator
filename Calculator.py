import streamlit as st

# Calculator Program

# Title
st.title("Khadija Calculator")

# Input Fields
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Operation Selection
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate Button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."

    # Display Result
    st.write("Result:", result)