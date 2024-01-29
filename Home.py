import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Historic Quiz App",
    page_icon="❓"
)

# Title and sidebar
st.title("Welcome To Historic Quiz App!")
st.sidebar.success("Select any genre you like to take historic questions from 😄")

# Rules for the quiz
st.markdown("### Rules:")
st.write("1. Answer all questions to the best of your knowledge.")
st.write("2. Please provide your answers in DD/MM/YYYY format.")
st.write("3. You can pick any genre of your interest.")
st.write("4. Enjoy the quiz and have fun learning about history!")
st.write("5. Head to general category if the existing genre doesn't excites you.")


participant_name = st.text_input("Enter your name to continue:")

col1, col2, col3, col4, col5 = st.columns(5)

with col3:
    button1 = st.button("Play Game")
    
if button1:
    st.title("Hello " + participant_name + "! 🙋‍♂️")
    st.subheader("Welcome to the history quiz game! Best of Luck 🤞")
    st.subheader("Please choose in which genre you would love to answer the historical question.")
    