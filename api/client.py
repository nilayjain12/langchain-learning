# importing the required libraries
import streamlit as st
import requests

# creating the function to call the api using post
def get_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"topic": input_text}  # Corrected JSON structure
    )
    json_response = response.json()
    print("API Response:", json_response)  # Debugging
    return json_response.get('output', "Error: Invalid response from API")  # Avoid KeyError


# create streamlit framework
st.title("Poem Generator")
# create a text input for the user to input the topic
input_topic = st.text_input("Enter a topic for which you want a poem to be generated...")

if input_topic:
    # call the function to get the response from the api
    st.write(
        get_response(input_topic)
    )