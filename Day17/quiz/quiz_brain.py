class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_input = input(f"Q.{self.question_number + 1} : {current_question.text} (true/false) :")
        self.check_answer(user_input, current_question.answer)
        print("\n")

    def check_answer(self, u_input, current_answer):
        user_input = u_input
        current_answer = current_answer
        if user_input.lower() == current_answer.lower():
            self.score += 1
            print("Correct !")
            self.question_number += 1
            print(f"Current Score : {self.score}/{self.question_number}")
        else:
            print("Incorrect !")
            self.question_number += 1
            print(f"Current Score : {self.score}/{self.question_number}")

