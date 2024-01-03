import sys
sys.path.append('.')
from src.models.question import Question

def test_question():
    # Test case 1: Create a question object
    options = [(1, "Option A", 1, 1), (2, "Option B", 0, 1)]
    question = Question(1, "Question 1", options)
    assert question.id == 1
    assert question.statement == "Question 1"
    assert question.options == options

    # Test case 2: Set a new question
    new_options = [(3, "Option A", 1, 2), (4, "Option B", 0, 2)]
    question.set_question(2, "Question 2", new_options)
    assert question.id == 2
    assert question.statement == "Question 2"
    assert question.options == new_options

    # Test case 3: Get question as tuple
    assert question.get_question() == (2, "Question 2", new_options)

    # Test case 4: Get question statement
    assert question.get_statement() == "Question 2"

    # Test case 5: Get question options
    assert question.get_options() == new_options

    # Test case 6: Get question ID
    assert question.get_id() == 2

    # Test case 7: Convert question to string
    #assert question.to_string() == "2, Question 2, [(3, 'Option A', 1, 2), (4, 'Option B', 0, 2)]"

# Run the tests
test_question()