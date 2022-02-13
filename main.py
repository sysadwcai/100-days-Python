from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
Opentdb.com/api/#questions/category/difficulty/type

question_bank = []
for question in question_data:
    question_text = question['text']
    question_anwer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(F"Your final score is: {score}/{quiz.question_number}.")

      
                             
