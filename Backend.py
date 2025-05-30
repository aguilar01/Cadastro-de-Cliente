import sqlite3 as sql

class TransactionObject():  # Operações e conexão com o banco de dados
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    # Conexão com o banco de dados
    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    # Encerra a conexão com o banco de dados e pronto
    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    # Executa as funções de um comando no banco de dados recebendo parâmetros
    def execute(self, sql_query, parms=None):
        if TransactionObject.connected:
            if parms is None:  # Vetor que contém os parâmetros do comando SQL
                TransactionObject.cur.execute(sql_query)
            else:
                TransactionObject.cur.execute(sql_query, parms)
            return True
        else:
            return False

    # Obtém os valores de entrada do comando SELECT
    def fetchall(self):
        return TransactionObject.cur.fetchall()

    # Realiza o commit das operações
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

    @staticmethod
    def initDB():
        trans = TransactionObject()
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()

    @staticmethod
    def insert(nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    @staticmethod
    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    @staticmethod
    def search(nome="", sobrenome="", email="", cpf=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    @staticmethod
    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
        trans.persist()
        trans.disconnect()

    @staticmethod
    def update(id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()

# ✅ Agora chamamos initDB() após a definição da classe
TransactionObject.initDB()