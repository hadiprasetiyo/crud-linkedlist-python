class Mahasiswa:
    def __init__(self, data):
        self.data = {
            "nim"       : data[0],
            "nama"      : data[1],
            "tahun"     : data[2],
            "semester"  : data[3],
            "prodi"     : data[4],
            "kelas"     : data[5]
        }
        self.next = None