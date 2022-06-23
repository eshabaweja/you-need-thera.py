class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        curr_ques = self.question_list[self.question_number]
        print(f"\nQ.{self.question_number+1}. {curr_ques.question} (True/False)")
        self.question_number+=1
        user_ans = input()
        self.check_answer(user_ans, curr_ques.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

        