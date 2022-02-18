from questions import Question
from data import question_data
from quizbrain import QuizBrain

# created the question bank.
question_bank = []
#it should contain a list of question objects each being initialized with a question and an answer
for quest in question_data:
    question_text = quest['text']
    answer = quest['answer']
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

#print(question_bank[0].question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
