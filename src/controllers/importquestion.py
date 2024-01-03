from src.models.filemanager import FileManager
from src.models.question import Question
from src.models.statement import Statement
from src.models.option import Option

class ImportQuestion:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_manager = FileManager(self.file_name)
        self.question = None
        self.statement = None
        self.options = []
        self.questions = None
        self.questionList = []

    def import_question(self):
        self.questions = self.file_manager.read_file_to_string(self.file_name)
        self.questions = self.questions.split("--")
        question_id = 0
        
        for question in self.questions:
            lines = question.split("\n")
            while '' in lines:
                lines.remove('')
            
            correct_option = lines[-1][-1].upper()
            lines[-1] = lines[-1][:-1]
            lines.pop()

            text_lines = []
            options_lines = []

            for line in lines:
                if not line[0].isupper() or not line[1:3] == ') ':
                    text_lines.append(line)
                else:
                    options_lines.append(line[3:])
            question_id += 1
            statement = Statement(question_id, text_lines[0])

            self.options = []

            option_id = 0
            for option in options_lines:
                optionIndex = options_lines.index(option)
                option_id += 1

                if optionIndex == ord(correct_option) - ord('A'):
                    correct_answer = True
                else:
                    correct_answer = False
                self.options.append(Option(option_id, option, correct_answer, question_id))
            self.questionList.append(Question(question_id, statement, self.options))

        return self.questionList



            

