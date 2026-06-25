# LinkedList with CRUD Operations
from controllers.controllerMahasiswa import ControllerMahasiswa

def Menu(data):
    if data == 'admin':
        print("Menu Admin :")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Search Data")
        print("5. Print Data")
        print("6. Update Linkedlist")
        print("7. Search Linkedlist")
        print("8. Print Linkedlist")
        print("9. Reset Linkedlist")
        print("10. Exit")
    else:
        print("Menu User :")
        print("1. Search Data")
        print("2. Print Data")
        print("3. Update Linkedlist")
        print("4. Search Linkedlist")
        print("5. Print Linkedlist")
        print("6. Exit")
    
def Line():
    print("==========================================================")

while True:
    username = input("Username : ")
    password = input("Password : ")
    user = ControllerMahasiswa((username, password))

    if user.privilige == "admin":
        Line()
        print("Selamat datang, {}".format(username))
        while True:
            Menu(user.privilige)
            pilihan = int(input("Pilihan : "))
            if pilihan == 1:
                Line()
                data = []
                data.append(input("NIM : "))
                data.append(input("Nama : "))
                data.append(input("Tahun : "))
                data.append(input("Semester : "))
                data.append(input("Prodi : "))
                data.append(input("Kelas : "))
                user.InsertList(data)
                Line()
            elif pilihan == 2:
                Line()
                data = []
                data.append(input("NIM : "))
                data.append(input("Nama : "))
                data.append(input("Tahun : "))
                data.append(input("Semester : "))
                data.append(input("Prodi : "))
                data.append(input("Kelas : "))
                user.UpdateList(data)
                Line()
            elif pilihan == 3:
                Line()
                data = []
                data.append(input("NIM : "))
                user.DeleteList(data)
                Line()
            elif pilihan == 4:
                Line()
                data = []
                data.append(input("NIM : "))
                user.SearchList(data)
                Line()
            elif pilihan == 5:
                Line()
                user.PrintList()
                Line()
            elif pilihan == 6:
                Line()
                user.UpdateLinkedList()
                Line()
            elif pilihan == 7:
                Line()
                data = []
                data.append(input("NIM : "))
                user.SearchLinkedList(data)
                Line()
            elif pilihan == 8:
                Line()
                user.PrintLinkedList()
                Line()
            elif pilihan == 9:
                Line()
                user.ResetLinkedList()
                Line()
            elif pilihan == 10:
                Line()
                print("Terima kasih telah menggunakan program ini")
                Line()
                break
            else:
                Line()
                print("Pilihan tidak ada")
    elif user.privilige == "user":
        Line()
        print("Selamat datang, {}".format(username))
        while True:
            Menu(user.privilige)
            pilihan = int(input("Pilihan : "))
            if pilihan == 1:
                Line()
                data = []
                data.append(input("NIM : "))
                user.SearchList(data)
                Line()
            elif pilihan == 2:
                Line()
                user.PrintList()
                Line()
            elif pilihan == 3:
                Line()
                user.UpdateLinkedList()
                Line()
            elif pilihan == 4:
                Line()
                data = []
                data.append(input("NIM : "))
                user.SearchLinkedList(data)
                Line()
            elif pilihan == 5:
                Line()
                user.PrintLinkedList()
                Line()
            elif pilihan == 6:
                Line()
                print("Terima kasih telah menggunakan program ini")
                break
            else:
                print("Pilihan tidak ada")
    else:
        Line()
        print("Username atau Password salah")
        break
    
    Line()
    keluar = input("Keluar (y/n) : ")
    if keluar.lower() == 'y':
        break
    else:
        Line()
        continue