import pandas as pd

df = pd.DataFrame({
    'Algoritma dan struktur data 2': [90, 80, 65],
    'Matematika numerik': [80, 60, 70]
}, index = ['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3'])
print('tabell nilai mahasiswa')
print(df)

df['Rata-rata'] = df.mean(axis=1)
print('Rata-rata nilai mahasiswa')
print(df)

print('Rata-rata nilai matkul')
Rata_rata_matkul = df.mean(axis=0)
print(Rata_rata_matkul)