# IMDB Movies Prediction

Bu proje, IMDB filmleri veri kümesi kullanarak film puanlarını tahmin etmek için bir sinir ağı modeli oluşturur. Model, PyTorch kütüphanesi kullanılarak eğitilmiştir.

## Kullanılan Kütüphaneler

- `pandas` - Veri işleme ve analiz için
- `torch` - Derin öğrenme ve sinir ağı oluşturma için
- `sklearn` - Veriyi ön işleme ve model değerlendirme için

## Veri Kümesi

- `imdb_movies.csv`: IMDB filmleri hakkında çeşitli bilgiler içeren CSV dosyası.

## Adımlar

1. **Veri Yükleme ve Ön İşleme**
   - Veriler CSV dosyasından yüklenir.
   - Belirtilen sütunlar sayısal değerlere dönüştürülür.
   - Eksik değerler ve gereksiz sütunlar temizlenir.
   - Özellikler ve hedef değişken ayrılır.

2. **Veri Bölme ve Ölçeklendirme**
   - Veri eğitim ve test setlerine ayrılır.
   - Özellikler standartlaştırılır.

3. **PyTorch Veri Kümesi ve Veri Yükleyicileri**
   - Veriler PyTorch tensorlerine dönüştürülür.
   - Eğitim ve test veri kümesi ve veri yükleyicileri oluşturulur.

4. **Model Tanımlama ve Eğitim**
   - Bir sinir ağı modeli tanımlanır ve eğitilir.
   - Modelin performansı epoch başına kayıp fonksiyonu ile izlenir.

5. **Model Değerlendirme ve Tahmin**
   - Model test verileri üzerinde değerlendirilir ve doğruluk metrikleri hesaplanır.
   - Tüm veri kümesi üzerinde tahminler yapılır ve sonuçlar CSV dosyasına kaydedilir.

## Model Yapısı

- **Giriş Katmanı:** 3 özellik (budget_x, revenue, country)
- **Gizli Katman 1:** 64 nöron
- **Gizli Katman 2:** 32 nöron
- **Çıkış Katmanı:** 1 nöron (puan tahmini)

## Eğitim ve Değerlendirme

- **Kayıp Fonksiyonu:** Ortalama Kare Hata (MSE)
- **Optimizasyon Yöntemi:** Adam
- **Epoch Sayısı:** 5000

## Sonuçlar

- Modelin tahminleri `Sonuc.csv` dosyasına kaydedilir.
- Sayısal değerler, orijinal kategorik değerlerle geri dönüştürülür.

## Kullanım

Projenin çalıştırılması için gerekli kütüphanelerin yüklü olduğundan emin olun. Ardından Python kodunu çalıştırarak tahminler yapabilirsiniz.

```bash
pip install pandas torch scikit-learn
python main.py
