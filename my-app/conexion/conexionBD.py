

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    print("ENTRO A LA CONEXION")
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="34.82.189.17",
                #host="viaduct.proxy.rlwy.net",
            port=3306,
            user="root",
            passwd="Sistemas2002",
                #passwd="-D2eD6aDb5Bg6dEbhAAeBB6gd3EheaBg",
            database="proyectodata",
                #database="crud_python",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True

        )
        if connection.is_connected():
            print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
