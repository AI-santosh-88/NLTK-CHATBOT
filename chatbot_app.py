
import streamlit as st
from nltk.chat.util import Chat, reflections
import base64

# Define pairs for the chatbot
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today ?"]],
    [r"(.*)help(.*)", ["I can help you"]],
    [r"(.*) your name ?", ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot."]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind that"]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great!"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there"]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse"]],
    [r"(.*)created(.*)", ["Santosh created me using Python's NLTK library.", "Top secret ;)"]],
    [r"(.*) (location|city) ?", ['Hyderabad, India']],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain"]],
    [r"how (.*) health (.*)", ["Health is very important, but I am a computer, so I don't need to worry about my health"]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket"]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli"]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ['Our customer service will reach you']]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Set the background image using custom CSS
def set_background(image_file):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{image_file});
        background-size: cover;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Convert the image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to set text colors
def set_text_styles():
    text_styles = """
    <style>
    .title {
        color: #0000ff;  /* Change title color to blue */
    }
    .chatbot-response {
        color: #0000ff;  /* Change bot response color to blue */
    }
    .user-input {
        color: #0000ff;  /* Change user input color to blue */
    }
    </style>
    """
    st.markdown(text_styles, unsafe_allow_html=True)



# Set the background image
image_base64 = get_base64_of_image("background.jpg")  # Specify your image path here
set_background(image_base64)

# Set text styles
set_text_styles()

# Streamlit UI
st.markdown("<h1 class='title'>Chatbot with NLTK </h1>", unsafe_allow_html=True)
st.write("Type 'quit' to end the conversation.")

# User input text box
user_input = st.text_input("You:", "")

# Display bot response if user has entered text
if user_input:
    if user_input.lower() == "quit":
        st.write("<div class='chatbot-response'>Bot: Bye for now. See you soon :)</div>", unsafe_allow_html=True)
    else:
        response = chatbot.respond(user_input)
        st.write(f"<div class='chatbot-response'>Bot: {response}</div>", unsafe_allow_html=True)
        
        
            
# Footer
st.markdown("---")
st.write("Created with ❤️ by Santosh")
