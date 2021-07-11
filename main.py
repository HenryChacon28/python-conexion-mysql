import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip
            user='root', # tu mombre de usuario DB
            password='sasa',# en mi caso
            db='demo'# nombre de tu DB
        )

        self.cursor = self.connection.cursor()

        print("Conexión establecida exitosamente!")

    # Función que selecciona el primer usuario de nuestra de DB
    def select_user(self, id):
        sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])

        except Exception as e:
            raise

    # Función que selecciona todos los usuarios de nuestra DB
    def select_all_users(self):
        sql = 'SELECT id, username, email FROM users'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("Id:", user[0])
                print("Username:", user[1])
                print("Email:", user[2])
                print("____________\n")

        except Exception as e:
            raise

    # Función que actualiza los datos de uno de nuestros usuarios DB
    def update_user(self, id, username):
        sql = "UPDATE users SET username='{}' WHERE id = {}".format(username, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    # Función que cierra la conexión de nuestra DB
    def close(self):
        self.connection.close

# Conecta nuestra nuestra DB
database = DataBase()

# Invoca nuestros usuarios
database.select_all_users()

# Actualiza un usuario
# database.update_user(1, 'cambio de nombre')
 
# Cierra la conección
database.close()