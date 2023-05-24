def kullanici_kayit():
    kullanici_bilgi = {}
    kullanici_adi = input("Kullanıcı adını girin: ")
    kullanici_sifre = input("Kullanıcı şifresini girin: ")
    kullanici_bilgi["kullanici_adi"] = kullanici_adi
    kullanici_bilgi["kullanici_sifre"] = kullanici_sifre
    with open("kullanici_bilgileri.txt", "a") as f:
        f.write(kullanici_bilgi["kullanici_adi"] + "," + kullanici_bilgi["kullanici_sifre"] + "\n")
    print("Kullanıcı kaydedildi.")


def giris():
    kullanici_adi = input("Kullanıcı adını girin: ")
    kullanici_sifre = input("Kullanıcı şifresini girin: ")
    with open("kullanici_bilgileri.txt", "r") as f:
        for line in f:
            kayitli_kullanici_adi, kayitli_kullanici_sifre = line.strip().split(",")
            if kullanici_adi == kayitli_kullanici_adi and kullanici_sifre == kayitli_kullanici_sifre:
                print("Giriş başarılı.")
                return
        print("Hatalı kullanıcı adı veya şifre.")


while True:
    secim = int(input("1-Kayıt, 2-Giriş, 3-Çıkış: "))

    if secim == 1:
        kullanici_kayit()

    elif secim == 2:
        giris()

    elif secim == 3:
        print("Çıkış yapılıyor.")
        break

    else:
        print("Yanlış seçim yaptınız.")