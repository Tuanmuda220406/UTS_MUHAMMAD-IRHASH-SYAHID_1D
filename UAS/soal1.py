datamahasiswa = []

while True:
    print('''
          Welcome
          1. Tambah Mahasiswa
          2. Tampilkan Data Mahasiswa
          ''')
    print('')
    pilihan = input('Masukkan Pilihan Anda : ')
        
    if pilihan == '1':
        nama = int(input('Masukkan NIM: '))
        nim = input('Masukkan nama: ')
        
        tambah_mhs = {'nama': nama, 'nim': nim}
        datamahasiswa.append(tambah_mhs)
        
        
    elif pilihan == '2':
        print('DAFTAR MAHASISWA :')
        i = 1
        
        if  datamahasiswa == []:
            print('mahasiswa gaib')
        else:
            for mhs in datamahasiswa:
                print(f'{i}. {mhs["nama"]}, {mhs["nim"]}')
                i += 1
        break