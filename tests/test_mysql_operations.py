import sys
sys.path.append('.')
from src.models.mysql_operations import MysqlOperations

def test_mysql_operations():
    # Test case 1: Test connection
    mysql = MysqlOperations("localhost", "teste", "teste", "sakila")
    assert mysql.connect() == "Conexão realizada com sucesso!"

    # Test case 2: Test disconnection
    assert mysql.disconnect() == "Conexão encerrada com sucesso!"

    # Test case 3: Test execute_query
    query = "INSERT INTO language(`language_id`,`name`,`last_update`)VALUES(9,'Brazilian Portuguese','2006-02-15 05:02:19')"
    assert mysql.execute_query(query) == "Query executada com sucesso!"

    # Test case 4: Test execute_read_query
    query = "SELECT * FROM language"
    result = mysql.execute_query(query)
    assert isinstance(result, list)

# Run the tests
test_mysql_operations()