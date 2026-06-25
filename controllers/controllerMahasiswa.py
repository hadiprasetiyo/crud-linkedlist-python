from prettytable import PrettyTable
from models.mahasiswa import Mahasiswa
from database.database import Database
import mysql.connector

def Line():
    print("==========================================================")

class ControllerMahasiswa(Database):
    def __init__(self, data):
        Database.__init__(self)
        self.head = None
        self.data = {
            "username"  : data[0],
            "password"  : data[1],
        }
        self.privilige = self.Privilige(self.data)
    
    def Privilige(self, data):
        sql = "SELECT privilege FROM account WHERE username = '{}' AND password = '{}'".format(self.data["username"], self.data["password"])
        self._cursor.execute(sql)
        result = self._cursor.fetchone()
        if result:
            finalResult = result[0].replace("'", "")
            return finalResult
        else:
            return False
    
    def PrintList(self):
            sql = "SELECT * FROM mahasiswa"
            self._cursor.execute(sql)

            tables = PrettyTable(["NIM", "Nama", "Tahun", "Semester", "Prodi", "Kelas"])
            for data in self._cursor:
                tables.add_row(data)
                
            print(tables)
    
    def SearchList(self, data):
        if self.Validation(data) == False:
            Line()
            print("NIM tidak ada")
        else:
            sql = "SELECT * FROM mahasiswa WHERE nim = {}".format(data[0])
            self._cursor.execute(sql)
            data = self._cursor.fetchone()

            Line()
            print("NIM :", data[0])
            print("Nama :", data[1])
            print("Tahun :", data[2])
            print("Semester :", data[3])
            print("Prodi :", data[4])
            print("Kelas :", data[5])
    
    # Insert ke Database dengan Linked List
    def InsertList(self, data):
        try:
            if self.Validation(data) == False:
                sql = "INSERT INTO mahasiswa (nim, nama, tahun, semester, prodi, kelas) VALUES ({}, {}, {}, {}, {}, {})".format(data[0], data[1], data[2], data[3], data[4], data[5])
                self._cursor.execute(sql)
                self._db.commit()

                new_Mahasiswa = Mahasiswa(data)
                new_Mahasiswa.next = self.head
                self.head = new_Mahasiswa
            else:
                Line()
                print("NIM sudah ada")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def UpdateList(self, data):
        try:
            if self.Validation(data) == False:
                Line()
                print("NIM tidak ada")
            else:
                sql = "UPDATE mahasiswa SET nama = %s, tahun = %s, semester = %s, prodi = %s, kelas = %s WHERE nim = %s"
                val = (data[1], data[2], data[3], data[4], data[5], data[0])
                self._cursor.execute(sql, val)
                self._db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
    
    # Delete Database dengan Linked List
    def DeleteList(self, data):
        if self.Validation(data) == False:
            Line()
            print("NIM tidak ada")
        else:
            sql = "DELETE FROM mahasiswa WHERE nim = {}".format(data[0])
            self._cursor.execute(sql)
            self._db.commit()

            current = self.head
            previous = None
            while current is not None:
                if current.data["nim"] == data[0]:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                    return True
                previous = current
                current = current.next
            return False

    # Update Linked List dengan Database
    def UpdateLinkedList(self):
        self.ResetLinkedList()
        sql = "SELECT * FROM mahasiswa"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()

        for i in range(len(data)):
            new_Mahasiswa = Mahasiswa(data[i])
            new_Mahasiswa.next = self.head
            self.head = new_Mahasiswa

    def SearchLinkedList(self, data):
        current = self.head
        while current is not None:
            if current.data["nim"] == data[0]:
                Line()
                print("NIM :", current.data["nim"])
                print("Nama :", current.data["nama"])
                print("Tahun :", current.data["tahun"])
                print("Semester :", current.data["semester"])
                print("Prodi :", current.data["prodi"])
                print("Kelas :", current.data["kelas"])
                return True
            current = current.next
        return False

    def PrintLinkedList(self):
        current = self.head
        tables = PrettyTable(["NIM", "Nama", "Tahun", "Semester", "Prodi", "Kelas"])

        while current is not None:
            Line()
            tables.add_row(current.data)
            current = current.next
        
        print(tables)

    def ResetLinkedList(self):
        self.head = None

    def Validation(self, data):
        sql = "SELECT * FROM mahasiswa WHERE nim = {}".format(data[0])
        self._cursor.execute(sql)
        data = self._cursor.fetchone()

        if data is None:
            return False
        else:
            return True
    