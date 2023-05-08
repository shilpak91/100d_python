from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank  = []

for question in question_data:
    que_text = question["text"]
    # print(que)
    que_ans = question["answer"]
    # print(ans)
    new_question = Question(que_text,que_ans)
    question_bank.append(new_question)


# print(question_bank)
# que = question_bank[0]
# print (que.text)

quiz = QuizBrain(question_bank)
quiz.next_question()

