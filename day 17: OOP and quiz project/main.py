from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for index, (key, value) in enumerate(question_data):
    new_question = Question(question_data[index][key], question_data[index][value])
    question_bank.append(new_question)

QuizBrain = QuizBrain(question_bank)
 

while QuizBrain.still_have_questions():
    QuizBrain.next_question()


print('You have completed the quiz!!')
print(f'Your final score is: {QuizBrain.score}/{len(QuizBrain.question_list)}')