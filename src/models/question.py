class Question:
    def __init__(self, id, statement, options):
        self.id = id
        self.statement = statement
        self.options = options

    
    def set_question(self, id, statement, options):
        self.id = id
        self.statement = statement
        self.options = options
        return Question(self.id, self.statement, self.options)

    def get_question(self):
        return self.id, self.statement, self.options
    
    def get_statement(self):
        return self.statement
    
    def get_options(self):
        return self.options
    
    def get_id(self):
        return self.id
    
    def to_string(self):
        options_string = "\n"
        for option in self.options:
            options_string += option.to_string() + "\n"
            
        return f"{self.id}, {self.statement.to_string()}, {options_string}"
    