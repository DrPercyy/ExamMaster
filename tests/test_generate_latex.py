import sys
sys.path.append('.')
import unittest
from unittest.mock import patch
from src.models.generate_latex import ParseLatex

class ParseLatexTests(unittest.TestCase):
    def setUp(self):
        self.questoes = ["Question 1", "Question 2", "Question 3"]
        self.gabarito = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        self.nome_prova = "Test Prova"
        self.nome_disciplina = "Test Disciplina"
        self.data_prova = "2022-01-01"
        self.nome_aluno = "Test Aluno"
        self.numero_questoes = 3
        self.parse_latex = ParseLatex(self.questoes, self.gabarito, self.nome_prova, self.nome_disciplina, self.data_prova, self.nome_aluno, self.numero_questoes)

    def test_generate_latex(self):
        with patch('src.models.generate_latex.Document') as mock_document:
            mock_document.return_value.generate_tex.return_value = None

            self.parse_latex.generate_latex()

            mock_document.assert_called_once_with(documentclass='exam', document_options=['addpoints', 'answers'])
            mock_document.return_value.packages.append.assert_called_once_with(Package('graphicx'))
            mock_document.return_value.append.assert_called_with(Command('ID Prova: ', str(000)))
            mock_document.return_value.append.assert_called_with(Command('centering'))
            mock_document.return_value.append.assert_called_with(Section("Questionário", numbering=False))
            mock_document.return_value.append.assert_called_with(Section("Gabarito", numbering=False))
            mock_document.return_value.append.assert_called_with(Command('end', 'document'))
            mock_document.return_value.generate_tex.assert_called_once_with(self.nome_prova)

    def test_generate_header(self):
        with patch('src.models.generate_latex.Figure') as mock_figure:
            mock_figure.return_value.__enter__.return_value.append.return_value = None

            self.parse_latex.generate_header()

            mock_figure.assert_called_once_with(position='htbp')
            mock_figure.return_value.__enter__.return_value.append.assert_called_with(Command('centering'))
            mock_figure.return_value.__enter__.return_value.__enter__.return_value.add_row.assert_called_with([bold(self.nome_aluno + ' - ' + self.data_prova)])
            mock_figure.return_value.__enter__.return_value.__enter__.return_value.add_hline.assert_called_once()
            mock_figure.return_value.__enter__.return_value.__enter__.return_value.add_row.assert_called_with([bold(self.nome_prova + ' - ' + self.nome_disciplina)])
            mock_figure.return_value.__enter__.return_value.__exit__.assert_called_once()
            mock_figure.return_value.__enter__.return_value.append.assert_called_with(MiniPage(width=r'1\textwidth'))
            mock_figure.return_value.__enter__.return_value.__enter__.return_value.append.assert_called_with(Command('includegraphics[width=0.2\\textwidth]{qrcode.png}'))
            mock_figure.return_value.__enter__.return_value.__enter__.return_value.append.assert_called_with(Command('label{fig:qrcode}'))

    def test_generate_gabarito(self):
        with patch('src.models.generate_latex.Tabular') as mock_tabular:
            mock_tabular.return_value.__enter__.return_value.add_hline.return_value = None

            self.parse_latex.generate_gabarito()

            mock_tabular.assert_called_once_with("|c|c|")
            mock_tabular.return_value.__enter__.return_value.add_hline.assert_called_once()
            mock_tabular.return_value.__enter__.return_value.add_row.assert_called_with(["Questão", "Resposta"])
            mock_tabular.return_value.__enter__.return_value.add_hline.assert_called_once()
            mock_tabular.return_value.__enter__.return_value.add_row.assert_called_with([str(1), ""])
            mock_tabular.return_value.__enter__.return_value.add_hline.assert_called_once()
            mock_tabular.return_value.__enter__.return_value.add_row.assert_called_with([str(2), ""])
            mock_tabular.return_value.__enter__.return_value.add_hline.assert_called_once()
            mock_tabular.return_value.__enter__.return_value.add_row.assert_called_with([str(3), ""])
            mock_tabular.return_value.__enter__.return_value.add_hline.assert_called_once()

    def test_generate_questions(self):
        with patch('src.models.generate_latex.Command') as mock_command:
            mock_command.return_value = None

            self.parse_latex.generate_questions()

            mock_command.assert_called_with('begin', 'questions')
            mock_command.assert_called_with('question', self.questoes[0])
            mock_command.assert_called_with('begin', 'choices')
            mock_command.assert_called_with('choice', self.gabarito[0][0])
            mock_command.assert_called_with('choice', self.gabarito[0][1])
            mock_command.assert_called_with('choice', self.gabarito[0][2])
            mock_command.assert_called_with('end', 'choices')
            mock_command.assert_called_with('question', self.questoes[1])
            mock_command.assert_called_with('begin', 'choices')
            mock_command.assert_called_with('choice', self.gabarito[1][0])
            mock_command.assert_called_with('choice', self.gabarito[1][1])
            mock_command.assert_called_with('choice', self.gabarito[1][2])
            mock_command.assert_called_with('end', 'choices')
            mock_command.assert_called_with('question', self.questoes[2])
            mock_command.assert_called_with('begin', 'choices')
            mock_command.assert_called_with('choice', self.gabarito[2][0])
            mock_command.assert_called_with('choice', self.gabarito[2][1])
            mock_command.assert_called_with('choice', self.gabarito[2][2])
            mock_command.assert_called_with('end', 'choices')
            mock_command.assert_called_with('end', 'questions')

    def test_generate_footer(self):
        with patch('src.models.generate_latex.Command') as mock_command:
            mock_command.return_value = None

            self.parse_latex.generate_footer()

            mock_command.assert_called_with('end', 'document')

    def test_generate_pdf(self):
        with patch('src.models.generate_latex.Document') as mock_document:
            mock_document.return_value.generate_pdf.return_value = None

            self.parse_latex.generate_pdf()

            mock_document.assert_called_once_with(documentclass='exam', document_options=['addpoints', 'answers'])
            mock_document.return_value.packages.append.assert_called_once_with(Package('graphicx'))
            mock_document.return_value.generate_pdf.assert_called_once_with(self.nome_prova+".tex", clean_tex=False, compiler='pdflatex')

if __name__ == "__main__":
    unittest.main()