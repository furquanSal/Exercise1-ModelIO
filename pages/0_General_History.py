import streamlit as st
from historyQuiz import HistoryQuiz


st.set_page_config(
    page_title="Historic Quiz App",
    page_icon="❓"
)

background_image = ''' <style>
        [data-testid="stAppViewContainer"]{
            background-image: url('https://pbs.twimg.com/media/GFAgZcqagAEX9k-?format=png&name=small');
            background-size: cover;
            background-repeat: no-repeat;
        }
    </style>'''

st.markdown(background_image, unsafe_allow_html=True)

st.write("General History Questions")

def main():
    quiz = HistoryQuiz()
    
    st.subheader("Enter a Genre in which you would like to answer historical questions : ")
    given_genre = st.text_input("Eg. Mars, Moon, Egypt, Japan etc..")
    
    question = quiz.user_genre(given_genre)

    co1, co2, co3 = st.columns(3)

    with co2:
        button0 = st.button("Generate Question")


    if button0:
        st.subheader(question)
        user_answer = st.text_input("Your Answer Should Be In DD/MM/YYYY Format Only:")
        llm_answer = quiz.llm_answer(question)

        col1, col2, col3, col4 = st.columns(4)

        with col2:
            button1 = st.button("Check Answer")
        with col3:
            button2 = st.button("Reveal Answer")
                
        if button1:
            if user_answer == llm_answer:
                st.success("Congratulations! Your answer is correct.")
            else:
                st.error("Incorrect Answer! Try again.")
                age = quiz.calculate_age(llm_answer,user_answer)
                age = str(age)
                st.write("The difference between the days between your answer and actual answer is " + age + " days.")
         
        if button2:
            st.write("The correct answer is : ", llm_answer)
        
                
if __name__ == "__main__":
    main()
