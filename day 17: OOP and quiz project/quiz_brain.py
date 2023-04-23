# asking questions
# chcking if the answer was correct
# checking if we're at the endo f the quiz


class QuizBrain:
    def __init__(self,question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self) -> str:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        new_question = input(f'Q.{self.question_number} {current_question.text} (True/False)?: ')
        self.check_answer(new_question,current_question.answer)
        return new_question


    def still_have_questions(self) -> bool:
        return self.question_number < len(self.question_list)
        

    def check_answer(self,user_answer,correct_answer) -> str:
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('You are wrong.')
        print(f'The answer was {correct_answer}')
        print(f'Your corrent score is {self.score}/{self.question_number}')
        print('\n')
