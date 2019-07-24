import time

point = 0
form_jawaban_benar = (".> Jawaban Benar, Kamu mendapatkan 10 Point")
form_jawaban_salah = (".> Jawaban Salah, Jawaban yang benar adalah ")
form_point = ("Point kamu sekarang: ")

# [ Soal Pertama ]
def soal1():
    jawabanBenar = str("e")
    jawabanLengkap = ("[ e. Linus Torvalds ]")
    print('+'*50)
    print("[1]. Linux dibuat oleh ...")
    print("   a. Mark Zuckerberg")
    print("   b. Bill Gates")
    print("   c. Tim Berners Lee")
    print("   d. Atta Halilintar")
    print("   e. Linus Torvalds")
    print()
    jawaban1 = str(input("Jawaban > "))

    global point
    if jawaban1 == str(jawabanBenar):
        time.sleep(1)
        print(form_jawaban_benar)
        point += 10

    else:
        time.sleep(1)
        print(form_jawaban_salah, jawabanLengkap)

    time.sleep(1)
    print(form_point, point)
    print()
    time.sleep(1)


def soal2():
    jawabanBenar = ("a")
    jawabanLengkap = ("[ a. Guido Van Russom ]")
    print('+'*50)
    print("[2]. Siapa Founder Bahasa Pemrograman Python ?")
    print("  a. Guido Van Russom")
    print("  b. Tim Berners Lee")
    print("  c. Julian Assange")
    print("  d. Snowden")
    print("  e. Benjamin Engel")
    print()
    jawaban2 = str(input("Jawaban > "))

    global point
    if jawaban2 is jawabanBenar:
        time.sleep(1)
        print(form_jawaban_benar)
        point += 10
    else:
        time.sleep(1)
        print(form_jawaban_salah, jawabanLengkap)

    time.sleep(1)
    print(form_point, point)
    print()
    time.sleep(1)


def soal3():
    jawabanBenar =("c")
    jawabanLengkap = ("[ c. Bill Gates ]")
    print('+'*50)
    print("[3]. Siapa Founder Sistem Operasi Microsoft ?")
    print("   a. Julian Assange")
    print("   b. Ria Ricis")
    print("   c. Bill Gates")
    print("   d. Tukang Pijat Nurhadi")
    print("   e. Tukang Sampah")
    print()
    jawaban3 = str(input("Jawaban > "))

    global point
    if jawaban3 is jawabanBenar:
        time.sleep(1)
        print(form_jawaban_benar)
        point += 10
    else:
        time.sleep(1)
        print(form_jawaban_salah, jawabanLengkap)

    time.sleep(1)
    print(form_point, point)
    print()
    time.sleep(1)


def soal4():
    jawabanBenar = ("b")
    jawabanLengkap = ("[ b. Benjamin Engel ]")
    print('+'*50)
    print("[4]. Nama Karakter utama di film Who Am I ?")
    print("    a. Kang Urut")
    print("    b. Benjamin Engel")
    print("    c. Bill Gates")
    print("    d. Zilong")
    print("    e. Aldo")
    print()
    jawaban4 = str(input("Jawaban > "))

    global point
    # kondisi untuk jawaban yang benar OKE
    if jawaban4 is jawabanBenar:
        time.sleep(1)
        print(form_jawaban_benar)
        point += 10

    # kondisi untuk jawaban yang salah
    else:
        time.sleep(1)
        print(form_jawaban_salah, jawabanLengkap)

    time.sleep(1)
    print(form_point, point)
    print()
    time.sleep(1)


def soal5():
    jawabanBenar = ("b")
    jawabanLengkap = ("[ b. Sponsbob squarpants ]")
    print('+'*50)
    print("[5]. Nama Karakter utama di sponsbob squarpants ?")
    print("    a. Kang Urut")
    print("    b. Sponsbob squarpants")
    print("    c. Bill Gates")
    print("    d. Zilong")
    print("    e. Aldo")
    print()
    jawaban5 = str(input("Jawaban > "))

    global point
    if jawaban5 is jawabanBenar:
        time.sleep(1)
        print(form_jawaban_benar)
        point += 10
    else:
        time.sleep(1)
        print(form_jawaban_salah, jawabanLengkap)

    time.sleep(1)
    print(form_point, point)
    print()
    time.sleep(1)


def total_point():
    global point
    totalpoint = point
    print("Total Point Kamu Adalah: ", totalpoint)


def kumpulan_soal():
    soal1();
    soal2();
    soal3();
    soal4();
    soal5();
    total_point();



