import sys
sys.path.append('.')
from src.models.statement import Statement

def test_statement():
    # Test case 1: Create a statement object
    statement = Statement(1, "This is a statement")
    assert statement.question_id == 1
    assert statement.text == "This is a statement"

    # Test case 2: Set a new statement
    statement.set_statement(2, "This is another statement")
    assert statement.question_id == 2
    assert statement.text == "This is another statement"

    # Test case 3: Get statement as tuple
    assert statement.get_statement() == (2, "This is another statement")

    # Test case 4: Convert statement to string
    assert statement.to_string() == "'This is another statement'"

    # Test case 5: Convert statement to custom string format
    assert statement.to_string2() == "Enun.: This is another statement"

# Run the tests
test_statement()