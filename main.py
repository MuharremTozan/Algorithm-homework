import random

import sqlite3

database_connect = sqlite3.connect("login.db")

imlec = database_connect.cursor()

imlec.execute("""CREATE TABLE IF NOT EXISTS kullanıcılar(skor INTEGER ,kullanıcı_adi TEXT)""")
imlec.execute("""INSERT INTO kullanıcılar VALUES(138,"Ufuk") """)
database_connect.commit()
database_connect.close()



ai_score = 0
your_score = 0
moves = ["Taş", "Kağıt", "Makas"]
seçenek = ["şovalye","kale","ejderha"]
movesplus = {
    "şovalye" : "ejderha",
    "kale"    : "şovalye",
    "ejderha" : "kale",
    "q" : "seçilmez"
}
player = False

zar_seçenek = ["kırmızı","siyah","mor"]
renkler = {
    "kırmızı" : "siyah",
    "siyah"   : "mor",
    "mor"     : "kırmızı"
}


def skor():
    print("\033[1;32mSizin skorunuz:", your_score)
    print("\033[1;31mBilgisayarın skoru:", ai_score)
    print("\n\033[1;0m")
    return

def zar():
    while True:
        player_zar = input('(Kırmızı, Mor ya da Siyah zarı seçin! Çıkmak için q)\n').lower()
        computer_zar = random.choice(zar_seçenek)

        try:

            if computer_zar == player_zar:
                print("Yakaladın!")

            elif renkler[player_zar] == computer_zar:
                print("Daha güçlü zarı seçtin!")

            elif renkler[computer_zar] == player_zar:
                print("Daha zayıf zarı seçtin!")

            elif player_zar == "q":
                break

        except:
            print("Hata!")

while True:
    main_menu = input("""\033[1;34mTAŞ-KAĞIT-MAKAS OYUNU
1-)Oyuna başlamak için 1'e basınız.
2-)Skorları görmek için 2'ye basınız.
3-)Oyundan çıkış yapmak için 3'e basınız.
4-)Şovalye-Kale-Ejderha oyununa geçmek için 4'e basınız.
5-)Zar atma oyununa geçmek için 5'e basınız.
6-)Kendi taş-kağıt-makas oyununuzun bilgilerini girmek ister misiniz?
""")

    if main_menu == "3":
        exit()
    elif main_menu == "1":

        while True:
            ai = random.choices(moves)



            player = str(input("\033[1;34mTaş-Kağıt-Makas? Ya da çıkış için q\n").capitalize())

            try:
                if player == "Taş":

                    if ai == ['Kağıt']:
                        print("\033[1;31mKaybettin! Kağıt Taşı sarar.")
                        ai_score += 1
                    elif ai == ['Makas']:
                        print("\033[1;32mKazandın! Taş Makası kırar." )
                        your_score += 1
                    else :
                        print("\033[1;33mBerabere")


                elif player == "Kağıt":
                    if ai == ['Makas']:
                        print("\033[1;31mKaybettin! Makas Kağıdı keser.")
                        ai_score += 1
                    elif ai == ['Taş']:
                        print("\033[1;32mKazandın! Kağıt Taşı sarar.")
                        your_score += 1
                    else:
                        print("\033[1;33mBerabere!")

                elif player == "Makas":
                    if ai == ['Taş']:
                        print("\033[1;31mKaybettin! Taş Makası kırar.")
                        ai_score += 1
                    elif ai == ['Kağıt']:
                        print("\033[1;32mKazandın! Makas Kağıdı keser.")
                        your_score += 1
                    else :
                        print("\033[1;33mBerabere!")

                elif player == "Q":
                    break

            except:
                print("Hata!")


    elif main_menu == "2":
        skor()


    elif main_menu == "4":
        while True:
            main_menu2 = input("""\033[1;34mŞOVALYE-KALE-EJDERHA OYUNU
1-)Oyuna başlamak için 1'e basınız.
2-)Oyundan çıkış yapmak için 2'e basınız.
""")
            print("\033[1;0m")
            if main_menu2 == "2":
                exit()


            elif main_menu2 == "1":
                while True:

                    player_choice = input('(Şovalye, Kale, Ejderha birini tuşlayın! Çıkmak için q)\n').lower()
                    computer_choice = random.choice(seçenek)
                    try:

                        if computer_choice == player_choice :
                            print("Berabere!")

                        elif movesplus[player_choice] == computer_choice:
                            print("Kazandın!")

                        elif movesplus[computer_choice] == player_choice:
                            print("Kaybettin!")

                        elif player_choice == "q":
                            break

                    except:
                        print("Hata!")


    elif main_menu == "5":
        zar()


    elif main_menu == "6":
        class tip():
            isim = ""
            neyi_yener = ""
            neye_kaybeder = ""


        while (True):
            nesne = tip()
            nesne.isim = input("Hamle Adı Giriniz.")
            nesne.neyi_yener = input("Neyi Yenebileceğini Giriniz.")
            nesne.neye_kaybeder = input("Neye Kaybedebileceğini Giriniz.")

            print("{} {}'ı yener {}'a kaybeder".format(nesne.isim,nesne.neyi_yener,nesne.neye_kaybeder))
            sonuc = input("Devam etmek ister misiniz? (e/h)")

            if (sonuc == "h"):
                break


