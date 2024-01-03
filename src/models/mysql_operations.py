import mysql.connector

class MysqlOperations:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.cursor = self.connection.cursor()
            return "Conexão realizada com sucesso!"
        except mysql.connector.Error as err:
            return f"Erro ao conectar ao banco de dados: {err}"
        
    
    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            return "Conexão encerrada com sucesso!"
        else:
            return "Não há conexão para ser encerrada!"
    

    def execute_query(self, query):
        cursor = MysqlOperations.connect(self)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return "Query executada com sucesso!"
        except mysql.connector.Error as err:
            return f"Erro ao executar a query: {err}"
    
    def execute_read_query(self, query):
        cursor = MysqlOperations.connect(self)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Erro ao executar a query: {err}"
        

    def next_id(self, table):
        query = f"SELECT MAX(id) FROM {table}"
        result = MysqlOperations.execute_read_query(self, query)
        return result[0][0] + 1