# init table karyawan
table_karyawan = [
    ['A12', 'KATIA EVELYN', 'FEMALE', '21', 'DATA ANALYST'],
    ['A17', 'SRIYANDA AFRIDA', 'MALE', '22', 'DATA ANALYST'],
    ['B02', 'ERICO LIEM', 'MALE', '29', 'WEB DEVELOPER'],
    ['A50', 'BAGAS YUDA', 'MALE', '23', 'BUSINESS INTELLIGENCE'],
    ['A19', 'FRANSISKA KRISTIN', 'FEMALE', '25', 'DATA SCIENTIST'],
]


# init main_menu
main_menu = 0


# function show menu
def show_menu():
    print("===== Data Record Karyawan Perusahaan =====\n")
    print("1. Report Data Karyawan\n2. Menambahkan Data Karyawan\n3. Mengubah Data Karyawan\n4. Menghapus Data Karyawan\n5. Exit")


# function read
def read():
    sub_menu = 0

    while(True):
        print("+++++ Report Data Karyawan +++++\n")
        print("1. Report Seluruh Data")
        print("2. Report Data Tertentu")
        print("3. Kembali Ke Menu Utama")
        sub_menu = int(input("Silakan Pilih Sub Menu Read Data [1-3] : "))

        if sub_menu == 1:
            print("Daftar Karyawan :")
            for row in table_karyawan:
                print("ID : {}, Nama : {}, Gender : {}, Age : {}, Job_Position : {}".format(row[0], row[1], row[2], row[3], row[4]))
        elif sub_menu == 2:
            id = input("Masukkan ID : ")
            exists = False
            data = []
            
            for row in table_karyawan:
                if row[0] == id:
                    exists = True
                    data = row
            
            if exists:
                print("Data Karyawan dg ID : {}".format(id))
                print("ID : {}, Nama : {}, Gender : {}, Age : {}, Job_Position : {}".format(data[0], data[1], data[2], data[3], data[4]))
            else:
                print("***** Tidak ada Data Karyawan *****")
        elif sub_menu == 3:
            break
        else:
            pass
        print()


# function create
def create():
    sub_menu = 0

    while(True):
        print("+++++ Menambahkan Data Karyawan +++++\n")
        print("1. Tambah Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        sub_menu = int(input("Silakan Pilih Sub Menu Create Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False

            for row in table_karyawan:
                if row[0] == id:
                    exists = True
            
            if exists:
                print("Data Sudah Ada")
            else:
                nama = input("Masukkan Nama : ")
                gender = input("Masukkan Gender : ")
                age = input("Masukkan Age : ")
                job_position = input("Masukkan Job Position : ")

                while(True):
                    konfirmasi = input("Apakah Data akan disimpan? (Y/N) : ")

                    if konfirmasi == "Y":
                        row = [id, nama, gender, age, job_position]
                        table_karyawan.append(row)
                        print("Data Tersimpan")
                        break
                    
                    if konfirmasi == "N":
                        break
                print()
                                        
        elif sub_menu == 2:
            break
        else:
            pass


# function update
def update():
    sub_menu = 0

    while(True):
        print("+++++ Mengubah Data Karyawan +++++\n")
        print("1. Ubah Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        sub_menu = int(input("Silakan Pilih Sub Menu Update Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False
            index = 0

            i = 0
            for row in table_karyawan:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1
            
            if exists:
                data = table_karyawan[index]
                print("ID : {}, Nama : {}, Gender : {}, Age : {}, Job_Position : {}".format(data[0], data[1], data[2], data[3], data[4]))
                while(True):
                    konfirmasi = input("Tekan Y jika ingin update data atau N jika ingin cancel update (Y/N) : ")

                    if konfirmasi == "Y":
                        kolom = input("Masukkan Kolom/Keterangan yang ingin di edit : ")

                        if kolom == "nama":
                            nama_baru = input("Masukkan Nama Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    table_karyawan[index][1] = nama_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "gender":
                            gender_baru = input("Masukkan Gender Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    table_karyawan[index][2] = gender_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "age":
                            age_baru = input("Masukkan Age Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    table_karyawan[index][3] = age_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "job":
                            job_baru = input("Masukkan Job Baru : ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    table_karyawan[index][4] = job_baru
                                    print("Data Updated")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass

                        break
                    
                    if konfirmasi == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass


# function delete
def delete():
    sub_menu = 0

    while(True):
        print("+++++ Menghapus Data Karyawan +++++\n")
        print("1. Hapus Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        sub_menu = int(input("Silakan Pilih Sub Menu Hapus Data [1-2] : "))

        if sub_menu == 1:
            id = input("Masukkan ID : ")
            exists = False
            index = 0

            i = 0
            for row in table_karyawan:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1
            
            if exists:
                while(True):
                    konfirmasi = input("Apakah Data akan dihapus? (Y/N) : ")

                    if konfirmasi == "Y":
                        table_karyawan.pop(index)
                        print("Data Deleted")
                        break
                    
                    if konfirmasi == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass
        

# driver code
while(True):
    show_menu()
    main_menu = int(input("Silakan Pilih Main_Menu [1-5] : "))
    print()

    if main_menu == 1:
        read()
    elif main_menu == 2:
        create()
    elif main_menu == 3:
        update()
    elif main_menu == 4:
        delete()
    elif main_menu == 5:
        print("Thank you and Good Bye!!!")
        break
    else:
        print("***** Pilihan Yang Anda Masukkan Salah *****")
    print()