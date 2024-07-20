# Video Games Critic Score Prediction

Bu proje, video oyunlarının eleştirmen puanlarını tahmin etmek için bir Random Forest modeli kullanır. Proje, belirli özelliklere sahip oyun verilerini işler ve bu verileri kullanarak bir tahmin modeli oluşturur.

## İçindekiler
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Açıklaması](#proje-açıklaması)
- [Veri Seti](#veri-seti)
- [Model Eğitimi ve Değerlendirme](#model-eğitimi-ve-değerlendirme)
- [Sonuçlar](#sonuçlar)

## Kurulum

Gerekli paketleri yüklemek için aşağıdaki adımları izleyin:

1. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install pandas scikit-learn
    ```

2. Proje dosyasını klonlayın veya indirin.

## Kullanım

Proje dosyasını çalıştırmak için:

1. `main.py` dosyasını çalıştırın:
    ```bash
    python main.py
    ```

## Proje Açıklaması

Bu proje, video oyunlarının belirli özelliklerini kullanarak eleştirmen puanlarını tahmin eder. Model, `RandomForestRegressor` kullanarak oluşturulmuştur. Proje adımları aşağıdaki gibidir:

1. Verilerin okunması ve işlenmesi
2. Gerekli sütunların sayısal verilere dönüştürülmesi
3. Verilerin eğitim ve test setlerine ayrılması
4. Modelin eğitilmesi ve değerlendirilmesi
5. Tahminlerin orijinal veri setine eklenmesi
6. Sonuçların CSV dosyasına yazılması

## Veri Seti

Kullanılan veri seti `Video_Games_Data.csv` adlı dosyadır. Bu veri seti, aşağıdaki sütunları içermektedir:
- title: Oyunun adı
- console: Oyunun konsolu
- genre: Oyunun türü
- publisher: Yayıncı
- developer: Geliştirici
- release_date: Yayınlanma tarihi
- last_update: Son güncelleme tarihi
- img: Resim URL'si
- critic_score: Eleştirmen puanı

## Model Eğitimi ve Değerlendirme

Model, `RandomForestRegressor` kullanarak eğitilir ve test seti üzerinde değerlendirilir. Modelin doğruluğu `mean_squared_error` ile ölçülür.

## Sonuçlar

Modelin tahminleri orijinal veri setine eklenir ve sonuçlar `Sonuc.csv` dosyasına yazılır. Bu dosyada, her bir oyun için modelin tahmin ettiği eleştirmen puanları bulunur.

## İletişim

Proje ile ilgili sorularınız için [uzayk204@gmail.com](mailto:uzayk204@gmail.com) adresinden iletişime geçebilirsiniz.
