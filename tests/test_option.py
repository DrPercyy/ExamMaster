import sys
sys.path.append('.')
from src.models.option import Option

def test_option():
    # Test case 1: Create an option object
    option = Option(1, "Option A", 1, 1)
    assert option.id == 1
    assert option.option_text == "Option A"
    assert option.correct_answer == 1
    assert option.question_id == 1

    # Test case 2: Set a new option
    option.set_option(2, "Option B", 0, 1)
    assert option.id == 2
    assert option.option_text == "Option B"
    assert option.correct_answer == 0
    assert option.question_id == 1

    # Test case 3: Get option as tuple
    assert option.get_option() == (2, "Option B", 0, 1)

    # Test case 4: Get option text
    assert option.get_option_text() == "Option B"

    # Test case 5: Get correct answer
    assert option.get_correct_answer() == 0

    # Test case 6: Get option ID
    assert option.get_id() == 2

    # Test case 7: Get question ID
    assert option.get_question_id() == 1

    # Test case 8: Convert option to string
    #assert option.to_string() == "1 ,'2', 'Option B', 0"

    # Test case 9: Convert option text to custom string format
    #assert option.text_to_string() == "Opção: Option B"

# Run the tests
test_option()