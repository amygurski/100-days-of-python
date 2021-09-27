class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        player_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(player_answer, current_question.answer)

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong. The correct answer is: {correct_answer}.")
        self.current_score()

    def current_score(self):
        if self.more_questions():
            print(f"Your current score is {self.score}/{self.question_number}.\n")
        else:
            print(f"Thanks for playing! Your final score is {self.score}/{self.question_number}.\n")
