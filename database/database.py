import mysql.connector
import mysql.connector.errors

class Database:
    def __init__(self):
        self._db = mysql.connector.connect(
            host        = "localhost",
            user        = "root",
            passwd      = "",
            database    = "python_db"
        )
        try:
            self._cursor = self._db.cursor()
            self.Migration()
        except mysql.connector.errors.ProgrammingError as err:
            self.CreateDatabase()
            self.Migration()
            self._cursor = self._db.cursor()
    
    def CreateDatabase(self):
        sql = "CREATE DATABASE python_db"
        self._cursor.execute(sql)
    
    def Migration(self):
        sql = "CREATE TABLE IF NOT EXISTS mahasiswa (nim INT(10) PRIMARY KEY, nama VARCHAR(50), tahun INT(4), semester INT(1), prodi VARCHAR(50), kelas VARCHAR(50))"
        self._cursor.execute(sql)
