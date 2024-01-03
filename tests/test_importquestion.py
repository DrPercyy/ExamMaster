import sys
sys.path.append('.')
from src.controllers.importquestion import ImportQuestion

def test_import_question():
    # Test case 1: Import a single question
    import_question = ImportQuestion("QUESTOES\Habilidades de estudo e comunicacao\Questoes teste.txt")
    question_list = import_question.import_question()
    assert len(question_list) == 1
    assert question_list[0].id == 1
    assert question_list[0].statement.text == "Qual é um componente essencial da comunicação eficaz?"
    assert len(question_list[0].options) == 5
    assert question_list[0].options[0].option_text == "Falar rapidamente para transmitir mais informações."
    assert question_list[0].options[0].correct_answer == False
    assert question_list[0].options[1].option_text == "Usar terminologia técnica e jargões para impressionar o público."
    assert question_list[0].options[1].correct_answer == False
    assert question_list[0].options[2].option_text == "Ignorar as reações e o feedback do interlocutor."
    assert question_list[0].options[2].correct_answer == False
    assert question_list[0].options[3].option_text == "Ser claro e ouvir atentamente o interlocutor."
    assert question_list[0].options[3].correct_answer == True
    assert question_list[0].options[4].option_text == "Falar apenas sobre tópicos pessoais durante a conversa."
    assert question_list[0].options[4].correct_answer == False

    # Test case 2: Import multiple questions
   # import_question = ImportQuestion("questions.txt")
   # question_list = import_question.import_question()
   # assert len(question_list) == 3
   # assert question_list[0].question_id == 1
   # assert question_list[1].question_id == 2
   # assert question_list[2].question_id == 3

    # Add more test cases as needed

# Run the tests
test_import_question()