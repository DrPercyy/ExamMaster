from src.controllers.importquestion import ImportQuestion

list = ImportQuestion("QUESTOES\Laboratorio de Programacao I\Questoes Arranjos.txt").import_question()
for question in list:
    print(question.to_string())