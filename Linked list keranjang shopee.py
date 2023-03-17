import os
import time
from prettytable import PrettyTable

def login():
    print('✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿'.center(80))
    print("Please login to Shopee".center(80))
    print('✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿'.center(80))
    usern_ame = input("Masukkan Username Anda: ")
    passw_ord = input("Masukkan Password Anda: ")
    if usern_ame == "halo" and passw_ord == "anakayam":
        return True
    else:
        print("Username atau password yang anda masukkan salah!")
        print("Anda akan diarahkan keluar program...")
        raise SystemExit

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found
            
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data tidak tersedia!")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def show_data(self):
        os.system("cls")
        table = PrettyTable()
        table.field_names = ["No", "Data"]
        i = 1
        current_node = self.head
        while current_node is not None:
            table.add_row([i, current_node.data])
            current_node = current_node.next_node
            i += 1
        print(table)

    def menu_utama(self):
        pilih = "y"
        data_masuk = []
        data_hapus = []
        while pilih == "y":
            os.system("cls")
            print('✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿'.center(80))
            print("Welcome to Shopee".center(80))
            print('✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿'.center(80))
            print("Pilih menu yang anda inginkan:")
            print("[1]. Tampil Keranjang")
            print("[2]. Insert Keranjang")
            print("[3]. Delete Keranjang")
            print("[4]. Banyak Isi Keranjang")
            print("[5]. Riwayat Isi Keranjang")
            print("[6]. Log Out")
            x = input("Pilih menu (1/2/3/4/5/6): ")
            if x == "1":
                os.system("cls")
                self.show_data()
                a = input("")
            elif x == "2":
                os.system("cls")
                ker = str(input("Masukkan pesanan yang ingin anda tambahkan: "))
                self.insert(ker)
                data_masuk.append(ker)
            elif x == "3":
                    os.system("cls")
                    ker = str(input("Masukkan pesanan yang ingin anda hapuskan: "))
                    self.delete(ker)
                    data_hapus.append(ker)
                    a = input("")
            elif x == "4":
                os.system("cls")
                ker = str(input("Masukkan pesanan yang ingin anda cari: "))
                status = self.search(ker)
                if status == True:
                    print("Barang terdapat di dalam keranjang!")
                else:
                    print("Barang tidak terdapat di dalam keranjang!")
                a = input("")
            elif x == "5":
                pil = input("Ingin menampilkan riwayat pesanan yang dihapus/ditambah? (-/+) ")
                if pil == "-":
                    print("\nHistory data hapus:")
                    table_hapus = PrettyTable()
                    table_hapus.field_names = ["No", "Data"]
                    for i, data in enumerate(data_hapus):
                        table_hapus.add_row([i+1, data])
                    print(table_hapus)
                    time.sleep(3)
                elif pil == "+":
                    os.system("cls")
                    print("History data masuk:")
                    table_masuk = PrettyTable()
                    table_masuk.field_names = ["No", "Data"]
                    for i, data in enumerate(data_masuk):
                        table_masuk.add_row([i+1, data])
                    print(table_masuk)
                    time.sleep(3)
                else:
                    print("Pastikan anda memasukkan tanda -/+!")
            elif x == "6":
                login()
            else:
                pilih = "n"

if __name__ == "__main__":
    l = LinkedList()
    login()
    l.menu_utama()