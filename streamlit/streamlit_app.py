import streamlit as st
import requests

st.title("User Authentication with Streamlit")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Button to submit the login request
login_button = st.button("Login")

if login_button:
    # Define the request payload as a dictionary
    payload = {
        "username": username,
        "password": password
    }
    
    # Define the headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Send the POST request
    response = requests.post("http://fastapi:8000/login", json=payload, headers=headers)

    # Display the response status code
    st.write(f"Response status code: {response.status_code}")

    # Check the response status code and display a message accordingly
    if response.status_code == 200:
        st.success("Login successful")
    else:
        #st.error("Login failed")
        st.write(f"Response status code: {response.status_code}")
