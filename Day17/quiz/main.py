from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques['text']
    question_answer = ques['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank)

quiz_start = QuizBrain(question_bank)
while quiz_start.still_has_question():
    quiz_start.next_question()
print(f"Final Score {quiz_start.score}/{quiz_start.question_number}")
