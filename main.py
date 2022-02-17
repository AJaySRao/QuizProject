from questions import Question
from data import question_data


# created the question bank.
question_bank = []
#it should contain a list of question objects each being initialized with a question and an answer
for quest in question_data:
    new_question = Question(quest["text"], quest["answer"])
    question_bank.append(new_question)

print(question_bank[0].question)