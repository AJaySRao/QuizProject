
class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """if the self.question_number is less than the length of self.question_list.
        In that case, we'll return true,but otherwise we'll return false."""
        return self.question_no < len(self.question_list)

    def next_question(self):
        """Here first tracks the current question number as it starts out being zero and this question number gets 
        increased every time we show the user the next question to display the correct question number"""
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        u_ans = input(f"Q.{self.question_no}:{current_question.question} (True/False): ")
        self.check_answer(u_ans, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        """Compares user entered answer with the correct answer"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got that right!")
        else:
            print("That's wrong.!")
        print(f"Your current score:{self.score}/{self.question_no}")
        print(f"The correct answer was: {correct_answer}")
        print("\n")
