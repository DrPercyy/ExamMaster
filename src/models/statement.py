class Statement:
    def __init__(self, question_id, text):
        self.question_id = question_id
        self.text =  text

    def set_statement(self, question_id, text):
        self.question_id = question_id
        self.text = text
        return Statement(self.question_id, self.text) 
    
    def get_statement(self):
        return self.question_id, self.text
    
    def to_string(self):
        return f"'{self.text}'"
    
    def to_string2(self):
        return f"Enun.: {self.text}"