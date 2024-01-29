import streamlit as st 
from historyQuiz import HistoryQuiz

st.set_page_config(
    page_title="Historic Quiz App",
    page_icon="❓"
)

background_image = ''' <style>
        [data-testid="stAppViewContainer"]{
            background-image: url('https://pbs.twimg.com/media/GE_nf5xaYAAw-Mz?format=png&name=360x360');
            background-size: cover;
            background-repeat: no-repeat;
            color: white;
        }
    </style>'''

st.markdown(background_image, unsafe_allow_html=True)



st.write("Genre Chosen : Ancient Civilisation")



def main():
    quiz = HistoryQuiz()
    
    question = quiz.user_genre("Ancient Civilisation")    
    
    st.subheader(question)
    user_answer = st.text_input("Your Answer (DD/MM/YYYY format):")
    llm_answer = quiz.llm_answer(question)

    col1, col2, col3, col4 = st.columns(4)

    with col2:
        button1 = st.button("Check Answer")
    with col3:
        button2 = st.button("Reveal Answer")

    if button2:    
        st.write("The correct answer is : ", llm_answer)
        
        
    if button1:
        if user_answer == llm_answer:
            st.success("Congratulations! Your answer is correct.")
        else:
            st.error("Incorrect Answer! Try again.")
            age = quiz.calculate_age(llm_answer,user_answer)
            age= str(age)
            st.write("The difference between the days between your answer and actual answer is " + age + " days.")

if __name__ == "__main__":
    main()

