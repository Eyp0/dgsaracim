import datetime

print("************************")
print("DGS Takip Sistemi")
print("*************************")
hedef_soru = int(input("Hedef Soru Sayısı: "))
dersler = []

while True:
    print("1-Ders Çalışma Ekle")
    print("2-Raporu Göster")
    print("3-Çıkış")
    print("4-Günlük Kayıt Al")
    secim = input("Seçiminiz: ")

    if secim == "1":
        ders = input("Ders Adı: ")
        soru = int(input("Çalışılan Soru Sayısı: "))
        an = datetime.datetime.now()
        tarih = datetime.datetime.strftime(an, '%d/%m/%Y')
        print(f"Tarih otomatik olarak eklendi: {tarih}")
        dersler.append({
            "ders_adi": ders,
            "soru_sayisi": soru,
            "tarih": tarih
        })

    elif secim == "2":
        print("-----------------------")
        print("Rapor Gösteriliyor...")
        print("-----------------------")
        if len(dersler) == 0:
            print("Henüz Ders Çalışma Eklenmedi.")
            print("-----------------------")
        else:
            toplam_soru = 0
            for kayit in dersler:
                print(f"Ders Adı: {kayit['ders_adi']}, Çalışılan Soru Sayısı: {kayit['soru_sayisi']}")
                toplam_soru += kayit['soru_sayisi']
            print("-----------------------")
            print(f"Toplam Çalışılan Soru Sayısı: {toplam_soru}")
            print("-----------------------")
            yuzde = int((toplam_soru / hedef_soru) * 100)
            if yuzde > 100:
                dolu_kisim = 10
            else:
                dolu_kisim = int(yuzde / 10)
            bos_kisim = 10 - dolu_kisim
            print("Hedefe Ulaşma Durumu:")
            print("[" + "#" * dolu_kisim + " " * bos_kisim + f"] %{yuzde}")
            print("-----------------------")
            print("Hedef Değerlendirmesi:")
            if toplam_soru == hedef_soru:
                print("Tebrikler! Hedefinize Ulaştınız.")
            elif toplam_soru > hedef_soru:
                fazlalik = toplam_soru - hedef_soru
                print(f"Tebrikler! Hedefinizi Aştınız. {fazlalik} Soru Fazla Çalıştınız.")
            else:
                kalan = hedef_soru - toplam_soru
                print(f"Hedefinize Ulaşmak İçin {kalan} Soru Daha Çalışmalısınız.")
            print("-----------------------")

    elif secim == "3":
        print("Çıkış Yapılıyor...")
        break
    elif secim == "4":
        print("-----------------------")
        print("Günlük Kayıt Alınıyor...")
        dosya = open("gunluk_kayit.txt", "a", encoding="utf-8")
        for kayit in dersler:
            dosya.write(f"Ders Adı: {kayit['ders_adi']}, Çalışılan Soru Sayısı: {kayit['soru_sayisi']} Tarih: {kayit['tarih']}\n")
        dosya.close()
        print("Günlük Kayıt Başarıyla Alındı.")
        print("-----------------------")
        
    else:
        print("Geçersiz Seçim, Lütfen Tekrar Deneyin.")
        