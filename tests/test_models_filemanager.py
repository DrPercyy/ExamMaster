import sys
sys.path.append('.')
from src.models.filemanager import FileManager

def test_filemanager_read_file_to_string():
    # Create an instance of FileManager
    filemanager = FileManager()

    # Test case 1: File exists
    file_contents = filemanager.read_file_to_string('QUESTOES\Habilidades de estudo e comunicacao\Questoes teste.txt')
    assert file_contents == 'Qual é um componente essencial da comunicação eficaz?\nA) Falar rapidamente para transmitir mais informações.\nB) Usar terminologia técnica e jargões para impressionar o público.\nC) Ignorar as reações e o feedback do interlocutor.\nD) Ser claro e ouvir atentamente o interlocutor.\nE) Falar apenas sobre tópicos pessoais durante a conversa.\nResposta: D'

    # Test case 2: File does not exist
    error_message = filemanager.read_file_to_string('path/to/non_existing_file.txt')
    assert error_message == "O arquivo 'path/to/non_existing_file.txt' não foi encontrado."

    # Test case 3: Error reading file
    error_message = filemanager.read_file_to_string('24-01012023.pdf')
    assert error_message == "Ocorreu um erro ao ler o arquivo: 'utf-8' codec can't decode byte 0xd0 in position 10: invalid continuation byte"

# Run the tests
test_filemanager_read_file_to_string()