# import streamlit as st
# from PIL import Image


# img = Image.open('logo1.png')
# st.set_page_config(page_title='HR Bot', page_icon=img)

# hide_st_style="""
#             <style>
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True) 

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://t3.ftcdn.net/jpg/03/91/46/10/360_F_391461057_5P0BOWl4lY442Zoo9rzEeJU0S2c1WDZR.jpg");
# background-size: cover;
# background-position: right bottom;
# background-repeat: no-repeat;
# background-attachment: local;
# }}

# [data-testid = "stAppViewContainer"] {{
# background-image: url("https://media.licdn.com/dms/image/C4D0BAQFY5Ris2r7Wig/company-logo_200_200/0/1587124216937?e=2147483647&v=beta&t=ODjNI4e2HbNgWXI3rJtC7D0L5NHw_0eRrqBTs1Ge1GQ");
# background-size: 6%;
# background-position: top right;
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}



# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}



# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)





import streamlit as st
from PIL import Image
import json

# Load the JSON file with questions
with open('questions.json', 'r') as file:
    questions_data = json.load(file)

# Initialize an empty list to store the answers
answers = []

# Streamlit app configuration
img = Image.open('logo1.png')
st.set_page_config(page_title='HR Bot', page_icon=img)

hide_st_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background-image: url("https://t3.ftcdn.net/jpg/03/91/46/10/360_F_391461057_5P0BOWl4lY442Zoo9rzEeJU0S2c1WDZR.jpg");
background-size: cover;
background-position: right bottom;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Using st.form to display questions and collect answers
with st.form("question_form"):
    for index, question_data in enumerate(questions_data):
        st.write(question_data["question"])
        user_response = st.text_input(f"Your Answer {index + 1}")
        answers.append(user_response)

    submit_button = st.form_submit_button("Submit")

# After all questions have been answered, display a thank you message
if submit_button:
    st.write("Thanks for answering!")

# You can access the collected answers from the 'answers' list
st.write("Collected Answers:", answers)

