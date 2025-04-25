import streamlit as st
from PIL import Image
import json

# Load the JSON file with questions
with open('questions.json', 'r') as file:
    questions_data = json.load(file)

# Create a session state to keep track of the current question
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Initialize an empty list to store the answers or retrieve the existing list
answers = getattr(st.session_state, 'answers', [])

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

[data-testid="stAppViewContainer"] {
background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAulBMVEUAAAD///8pKSm/v78SEhIEBwf6+vr39/fu7u4HCgr19fXx8fHX19cPEhKCg4Pm5ubd3d2JiopSVFQwMTE8Pz8YGhri4uJCRES2trZ+f393eHjDxMTscSQ4OjrZ2dlaXFyio6POzs6Zmpq4ubliZGQgIiKRkpJKTExqbGysra398Of0rH7teS/uh0bscCJUVlb507ryn2v74dD86Nzyp3j4xqf1t47ugDz4zrLwjUz74tP2vZnxmF/+7+WjTf1oAAAJ7UlEQVR4nO2aCXebOhbHDRSxbyZgEDEgFoHctO722re03/9rzZXAjtMkTfrezLTTub/T4wghCf2luwhONxsEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQf6/0X8RNtovAgr52UAhPxso5GcDhfxs/LpCDuRHTOOf87WQw4fffsg8/jFfCTm8vH715mJPCLlzcb+/XRn5c55DyGmo29K3mvtVVTFrbS5r4qoyKvvxHneFHF7eXF8q8apejaaIDSO6179K9e4ZxugVQohKNiRMiLZ3n2hvD3Cg3caalhuGeqyVQMW+eqYQ2I/rm5vXr96cKvIhm9hatuiYGvf69y/M5BlC6n2QZY1cE3t+kQVT/ZSQremY+1gjLcw/FUSzysDcZMbjj7oUonR8/HihhCRO0K1lP93s4nv9jcx5jhA/NU1nETLAFHdPCjlC+ysQ0gWmmbUgJJSF5wlZdBDyUipZe1TpplkNs4MpKzMjdhS5RHM9Dy56JYR43mqBrr0WiBdF9tksvxYSLwP5FYvPVgZXvqdFvu/HZBVixUngmBn3c3cVYvssPo/6sBDwj9c3Hw9L4Y9VCTxWX+zJbpxRmajPh2maRdQO1D7tCKNzr1pFYdNJfVreztPUJJX1sJBaNRn2aTqVSxu3H67Sq5kl+6v91l6E5PUwOlDQ9zSXQkajgEa70P+WkJOOd19UcbUu2FontJa9MdXeGLtgYzpONm/NMT4JEVmQLBPeb44yIrBjBo1gCp17IURNeF6F+E1myndtJ+3kAzrd3ECb6Qqqxgh8RAphKdQBmylWQhpddgkm/76JnYQcPki7OpDfP709aIeP1yclMLNJ2gHhgQOmqvlXjrOn4aA7wYWQIgv40vxKmWI+mcEU8kE3x5achUzMZ6w6LkKiwTFXMgHjjEtZVeqPCHHWLk7pPSbki9TxUuq4vvlwWPdETsGj5lhIm2nMPSwjgfXcQhj1xB4WKH9MCHWcGW66Qt/s45MQ88Veki1C2gwmlDZTYDqbXW41cpJBqgd3hPhHZVpjOivTgg47XYrZ3486i5DDW6VD+/3V69evZUH5yW9SicicEsyj0jcU/tSjuWeqC0zkESGRFu9lgJOZjDuBOAtRlqSWeFd7ckNSEfvyb1AweT+jVT8EF0Jil5XS2UOIAkrIZMQidaSzPCLk/SflH3I//gBXWfbkGowM0uC0kVE/cTLpziIAWSqvxbvHTCvSitGcOkkL0Z+Ss5Azu7qe5IRnSrfgSU5XSMuCnlqcXgqR6+Uo01PhVy0KleGrf0QI+fgJtuG3T9fXb//86+b1tVLyh/ISEjqjIC7IkUcRHgTdEoPBxh8VArvlBArH3MwWWYWMAwD+Kk2L7c9bBHvE5XwhukMgH+4IIZ0UciePcOn1jwnRDm8W//j8J4i6Wfzk3RIaDN2hVj+aXMWWIODPEjJCZF0ITzsC4dey3DX8+ldywsdjI8UNvYAdcaTtWtunhHTfFAKAf1x/fqdBn1XJij1sdhF1dJVE+sycVYIkMJMLIaNTqsYQZkBIP26Gikng6JeffMRpVPRYhETyDDKxKK96w+htQ5cuXLmeyB4Q0nnW84UQyOuwH1/+egPRFzz9/blJG+jdpAwYgle6Jkg3CW6dnVS6qSyP8EwKiXabvUpaVhvy6FbIRUIkamJlz/d6qk91fiWj066k0pUvhQhpcxNto+fvyPsPb/+EdHIDCcT66/Ob2yZs7+jZ6hoaHBmuRG7XfLwMv3ljBjMsr9g7Uoh8WFPZbp5kzvSwEJlgwXtluHU2EBZDlSKCJVFcCKmkMsfZxs8Xoh2+aF+WY7xG3l+kTpfC+Ol6LMiPjjNuh12WjRc+QsToBFfDVg8ClUfs2XHSgW4DJ+1vE+IqxFFCrG5UuR/qt7Ag0aQynZONi5D10KjZkJKg2aWQF84TQlTwugE+v7/bRsD85lMu9eXxB6bJm0CPpdME8vTrdal8YDqnjrLBvNTldbATy4r4KYSwVQiUdrAsbrvLAmii0yVlNnAVjGEDt0HIBH+kEK2eRwh+27p8EQSjXBWeycK3hWjvfpe8O9xtE7VJws5bZItynjnz+qSDtY95ot6XrIpTmlR5mwh1uvKMZB5odzoU2V2ScCXKKhKetDJgkLoNKeXGukSRCGko7B5ug3OLJFlaabYBfYVtcBhBKmOnwreEPAKx7pycXXVoXysta52r5bqq9qTY8jyXXA6x3rktacRVfbTzlUwkcNu600qWz/XabeFvCPlf4BlCLPJ1DYkefLd5gPzOlwk5kBvdHc6L4EhG8vsv8d/5WeppIXUiA1YknxR5y48d1suELE/dIX7lataqzlIzjSzILszqC1DtypdBG9wIHI2wMJamby8/RKsST8RRWK36ZL1URnzwNXJ+quy/dJGhxL5/in+GkFbnhBQ0ZJpRloz0YRJHkDM6KjS/bK2C8jZKJua1tPWkL3Pa2VZbJm00NJC3vbbsbDspwzpqmhwSw5GGFalCGI/RkNd9ya5oPM9USM8waMkswSzD56nhtpTHlqBJDIOEMDCDVS0rwpIH3hGfFBJBLMmNoQ2FDz8dG0Q5xNTnc3Gsip1RbVu+Y90ct4OYObyoDFTA0akp5imnpd1x0RhlF++7ktoU3oeI7ECroWupPydiJ6ow3nb5kBQNnIHiue0aNrRe2Lc7JoaCi36AmFk3PNm1SRgNYdvU89zd/wrxpBBjyxuDU9f22tmzI2PH6bambGjarehLrxsgR7KC23TbDaELqbDQkq7stOqYJ8LqumRqYUmPUT97HE7hpJqjiopdyEEwc2dhlPbAorly5wLsjNpRI2bhJkY/eJxrds5LwuaKsmqI/ZDtKZ9YL83je4VYyZZvYVmL1mDHohWsacMwnlkytLNflK6x7ds9E3PcNdLYNHeg1SxgjuUuD8sIduQoQhFPUTF7idwRQwrph6TjNSzsJAxqN108Gx4IIf5ciIaVpTH1xo61A2t7MRs8ZDOr5tindUM7movueP8T1FNC7LZyKxEJWAQiyrJyizBhdpvDSrUWE8QDE+Z5nBh2R7tcHk7mkkduV4bcrWjNpI/wOOI2a8HPa5kF7VhE4COGVpUwxVqQovTb2mplKAA37IkfhqEfgZN1lPs2PNqP2rxu4SjnsaQsrB7m8d1CiAfDQ/zIIcBY5x/IdF4MtZYMUjbEZ4gjXixjiT33Msq4uSeDjgUtLIhScgT4J79zrcUoh6nI72PqQma85cUzguhFbPXdzNZcGeDggdCDyH/Q3YZ+qtH3Cvle7PIb32f/k/zbM7v/QIz/b7AxfhE2L34RftD/SUIQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQ5GfhX5IbHk6ZLRoXAAAAAElFTkSuQmCC");
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

# Check if there are more questions to display
if st.session_state.question_index < len(questions_data):
    st.write(questions_data[st.session_state.question_index]["question"])
    user_response = st.text_input("Your Answer")
    
    # Check if the "Submit" button is clicked
    if st.button("Submit"):
        answers.append(user_response)
        st.session_state.question_index += 1

# After all questions have been answered, display the answers
if st.session_state.question_index >= len(questions_data):
    st.write("Thanks for answering!")
    # st.write("Collected Answers:", answers)

# Store the answers list in a persistent session state

st.session_state.answers = answers
if st.session_state.question_index == len(questions_data):
    answers.pop(0)
    print(answers)
