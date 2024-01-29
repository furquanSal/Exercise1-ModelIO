from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from datetime import datetime
import os


set_llm_cache(InMemoryCache())

OPENAI_API_KEY_MITI = os.getenv("OPENAI_API_KEY_MITI")
model = OpenAI(openai_api_key = OPENAI_API_KEY_MITI)

class HistoryQuiz:
    
    @staticmethod
    def user_genre(genre):
        templ = PromptTemplate(
            input_variables=["genre"],
            template="Ask me ONE simple historic question in {genre} history genre. Ask me that question only whose answer will be in DD/MM/YYYY format."
        )
        prompt = templ.format(genre=genre)
        question = model.invoke(prompt)
        return question
    
    
    def get_new_question(self, genre):
        return HistoryQuiz.user_genre(genre)
        
    @staticmethod
    def user_answer(question):
        user_answer = input(f"{question} Please answer in DD/MM/YYYY format only :: ")
        return user_answer
    

    @staticmethod
    def llm_answer(question):
        example_questions = [
            {"Question" : "What was the Battle of Hastings?", "Answer" : "14/10/1066"},
            {"Question" : "When was the Declaration of Independence signed?", "Answer" : "04/07/1776"},
            {"Question" : "What year did World War II end?", "Answer" : "02/09/1945"},
            {"Question" : "When was the Great Fire of London?", "Answer" : "02/09/1666"},
            {"Question" : "Who discovered penicillin and in what year?", "Answer" : "03/09/1928"},
        ]
        example_prompt = PromptTemplate(input_variables=["Question, Answer"], template="Question: {Question} Answer:{Answer}")
        dynamic_prompt = FewShotPromptTemplate(
            input_variables=['Question'],
            examples=example_questions,
            example_prompt=example_prompt,
            prefix="Give response in DD/MM/YYYY format. No other words required.",
            suffix = "Question: {question}, Result:"
        )
        prompt = dynamic_prompt.format(question=question)
        result = model.invoke(prompt)
        return result.lstrip()
    
    
    def calculate_age(self, llm_answer, user_answer):
        llm_answer = datetime.strptime(llm_answer, '%d/%m/%Y')
        user_answer = datetime.strptime(user_answer, '%d/%m/%Y')

        age_difference = abs((user_answer - llm_answer).days)

        return age_difference

    
    
    
    