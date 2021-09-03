
from database import CursorFromConnectionPool # pool para a database
#Uma pool abre várias conexões e trata a segurança do encadeamento ao fornecer conexões aos solicitantes.
#O pooling de conexões significa que as conexões são reutilizadas em vez de serem criadas sempre que solicitadas.

class User: #criando a classe o usuário.
    def __init__(self, email, first_name, last_name, id=None): #parametros.
        #propriedades o objeto.
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email) # retorna o email do usuario.

    def save_to_db(self) -> object:

        with CursorFromConnectionPool() as cursor: #crianco a conexao com a pool.
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',#define a tablea que irá uasr e formatos.
                            (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionPool() as cursor: #criando o cursor para selecionar no banco de dados.
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,)) #executando a acao do cursor.
            user_data = cursor.fetchone() #método que recupera a próxima linha de um conjunto de resultados de consulta e retorna uma única sequência.
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])# retornando os dados inseridos para as colunas apropriadas no PostgreSQL.
