
class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list

    def still_has_questions(self):
        """if the self.question_number is less than the length of self.question_list.
        In that case, we'll return true,but otherwise we'll return false."""
        return self.question_no < len(self.question_list)

    def next_question(self):
        """Here first tracks the current question number as it starts out being zero and this question number gets 
        increased every time we show the user the next question to display the correct question number"""
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        input(f"Q.{self.question_no}:{current_question.question} (True/False): ")
