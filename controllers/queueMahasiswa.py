from prettytable import PrettyTable
from controllers.controllerMahasiswa import ControllerMahasiswa
from queue import Queue

class Queue(ControllerMahasiswa):
    def __init__(self):
        ControllerMahasiswa.__init__(self)
        self.data = Queue()
    
    def InsertQueue(self, data):
        sql = "SELECT * FROM mahasiswa"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        self.data.enqueue(data)

    def DeleteQueue(self):
        self.data.dequeue()

    def PrintQueue(self):
        data = self.data.getQueue()
        tables = PrettyTable(["NIM", "Nama", "Tahun", "Semester", "Prodi", "Kelas"])
        for i in data:
            tables.add_row(i)
        print(tables)