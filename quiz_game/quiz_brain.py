class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        for q in self.questions_list:
            print(q["text"])
