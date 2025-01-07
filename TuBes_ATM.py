import json

# Nama file untuk menyimpan data pengguna
DATA_FILE = 'atm_data.json'

# Fungsi untuk membaca data dari file
def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Fungsi untuk menulis data ke file
def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Fungsi untuk menampilkan menu
def display_menu():
    print("=== ATM ===")
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")

# Fungsi untuk cek saldo
def check_balance(account):
    print(f"Saldo Anda: {account['balance']}")

# Fungsi untuk setor uang
def deposit(account):
    amount = float(input("Masukkan jumlah uang yang ingin disetor: "))
    account['balance'] += amount
    print(f"Anda telah menyetor: {amount}")
    print(f"Saldo Anda sekarang: {account['balance']}")

# Fungsi untuk tarik uang
def withdraw(account):
    amount = float(input("Masukkan jumlah uang yang ingin ditarik: "))
    if amount > account['balance']:
        print("Saldo tidak cukup!")
    else:
        account['balance'] -= amount
        print(f"Anda telah menarik: {amount}")
        print(f"Saldo Anda sekarang: {account['balance']}")

# Fungsi utama untuk menjalankan sistem ATM
def atm_system():
    # Membaca data pengguna
    accounts = read_data()
    
    # Meminta pengguna untuk memasukkan ID akun
    account_id = input("Masukkan ID Akun Anda: ")
    
    # Jika akun tidak ada, buat akun baru
    if account_id not in accounts:
        accounts[account_id] = {'balance': 0}
        print("Akun baru telah dibuat.")
    
    account = accounts[account_id]

    while True:
        display_menu()
        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            check_balance(account)
        elif choice == '2':
            deposit(account)
        elif choice == '3':
            withdraw(account)
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid!")

    # Menyimpan data kembali ke file
    write_data(accounts)
    print("Terima kasih telah menggunakan ATM!")

# Menjalankan sistem ATM
if __name__ == "__main__":
    atm_system()