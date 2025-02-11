import streamlit as st

# Streamlit Calculator App
st.title("🧮 Simple Calculator")

# Operation Selection
operation = st.selectbox("Choose an operation:", 
                         ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

# Number Inputs
num1 = st.number_input("Enter first number", step=0.01)
num2 = st.number_input("Enter second number", step=0.01)

# Perform Calculation
result = None
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error! Division by zero is not allowed.")

# Display Result
if result is not None:
    st.success(f"Result: {result}")
