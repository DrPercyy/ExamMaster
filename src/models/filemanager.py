class FileManager:
    def __init__(self, file = None):
        self.file = file

    def read_file_to_string(self, file):
        self.file = file
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            return file_contents
        except FileNotFoundError:
            return f"O arquivo '{self.file}' não foi encontrado."
        except Exception as e:
            return f"Ocorreu um erro ao ler o arquivo: {str(e)}"