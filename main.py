import streamlit as st

# Function to find the largest number
def find_largest(num1, num2, num3, num4):
        largest = max(num1, num2, num3, num4)
        return largest

# Streamlit app
st.title(" Largest Number Finder!")

# Background image
def set_bg_hack_url():

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://cdn.vectorstock.com/i/1000x1000/04/80/background-with-numbers-copy-space-vector-23950480.webp");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()


# Input fields with custom labels
num1 = st.number_input(" **First Number:**", key="num1", step=1, value=None, placeholder="Type a number...")
num2 = st.number_input(" **Second Number:**", key="num2", step=1, value=None, placeholder="Type a number...")
num3 = st.number_input(" **Third Number:**", key="num3", step=1, value=None, placeholder="Type a number...")
num4 = st.number_input(" **Fourth Number:**", key="num4", step=1, value=None, placeholder="Type a number...")
# Button to find the largest number and display result
if st.button("Find the Largest!", type="primary"):
    # Call the function and store the result
    try:
        largest_num = find_largest(num1, num2, num3, num4)
    except TypeError:
        st.write('⚠️All fields required!')
    else:

    # Display results with dynamic text and emoji
        if largest_num == num1:
            message = f" First number (:blue[**{num1}**]) is the largest number!"
        elif largest_num == num2:
            message = f" Second number (:blue[**{num2}**]) is the largest number!"
        elif largest_num == num3:
            message = f" Third number (:blue[**{num3}**]) is the largest number!"
        else:
            message = f" Fourth number (:blue[**{num4}**]) is the largest number!"

        st.success(message, icon="🧑‍🎓")
