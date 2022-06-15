# filename: matrik.py


def buatmatrik(nilaiseed=1, row=7, col=9):
    #"membuat matrik"
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1, 100)
    return MA


def akses(m1, m2):
    #b
    p = int(input("Matriks [1/2] : "))
    r = int(input("Row[0-7]: "))
    c = int(input("Column[0-9]: "))
    if (p == 1):
        print("Isi dari Row ke-%d dan column %d adalah %d" % (r, c, m1[r][c]))
    elif (p == 2):
        print("Isi dari Row ke-%d dan column %d adalah %d" % (r, c, m2[r][c]))


def jumlahBaris(m1, m2):
    #c
    p = int(input("Matriks [1/2] : "))
    baris = int(input("Baris yang ingin dijumlah [0-7]: "))
    total = 0
    if p == 1:
        for i in range(9):
            total = total + m1[baris][i]
        print("Hasil dari baris ke-%d adalah %d" % (baris, total))
    elif (p == 2):
        for i in range(9):
            total = total + m2[baris][i]
        print("Hasil dari baris ke-%d adalah %d" % (baris, total))


def jumlahKolom(m1, m2):
    #c
    p = int(input("Matriks [1/2] : "))
    kolom = int(input("Kolom yang ingin dijumlah [0-9]: "))
    total = 0
    if p == 1:
        for i in range(7):
            total = total + m1[i][kolom]
        print("Hasil dari baris ke-%d adalah %d" % (kolom, total))
    elif (p == 2):
        for i in range(7):
            total = total + m2[i][kolom]
        print("Hasil dari baris ke-%d adalah %d" % (kolom, total))

def jumlahMatriks(m1,m2):

	m3 = [0] * 7
	for baris in range(7):
		m3[baris] = [0] * 9
		for j in range(9):
			m3[baris][j] = m1[baris][j] + m2[baris][j]
    
	
	print("Matrix Jumlah")
	for line in m3:
		print('  '.join(map(str, line)))
	return m3

def cetakMatriks():
    #a
    m1 = buatmatrik(2021)
    print("Matrix pertama")
    for line in m1:
        print('  '.join(map(str, line)))

    print("\nMatrix Kedua")
    m2 = buatmatrik(66)
    for line in m2:
        print('  '.join(map(str, line)))
    akses(m1, m2)

    jumlahBaris(m1, m2)
    jumlahKolom(m1, m2)
    jumlahMatriks(m1,m2)

def main():
    cetakMatriks()
    return


if __name__ == "__main__":
    main()