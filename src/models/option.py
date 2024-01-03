class Option:
    def __init__(self, id, option_text, correct_answer, question_id):
        self.id = id
        self.option_text = option_text
        self.correct_answer = correct_answer
        self.question_id = question_id
    
    def set_option(self, id, option_text, correct_answer, question_id):
        self.id = id
        self.option_text = option_text
        self.correct_answer = correct_answer
        self.question_id = question_id
        return Option(self.id, self.option_text, self.correct_answer, self.question_id)
    
    def get_option(self):
        return self.id, self.option_text, self.correct_answer, self.question_id
    
    def get_option_text(self):
        return self.option_text
    
    def get_correct_answer(self):
        return self.correct_answer
    
    def get_id(self):
        return self.id
    
    def get_question_id(self):
        return self.question_id
    
    def to_string(self):
        return f"{self.id} ,{self.question_id}, '{self.option_text}', {self.correct_answer}"
    
    def text_to_string(self):
        return f"Opção: {self.option_text}"
    
    
