import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# CSV dosyasını oku
data = pd.read_csv('Video_Games_Data.csv')

# Dönüştürülecek sütunlar
columns_to_convert = ['title', 'console', 'genre', 'publisher', 'developer']

# LabelEncoder nesnelerini saklamak için bir sözlük
label_encoders = {}

# Belirtilen sütunları seçme ve dönüştürme
for column in columns_to_convert:
    if (column in data.columns):  # Sütun veri setinde varsa
        label_encoder = LabelEncoder()  # LabelEncoder nesnesi oluştur
        data[column] = label_encoder.fit_transform(data[column])  # Sütunu sayısal değerlere dönüştür
        label_encoders[column] = label_encoder  # Encoder'ı sakla

# NaN (eksik) değerleri atma
data = data.dropna()

# Gereksiz sütunları çıkarma
data = data.drop(['release_date', 'last_update', 'img'], axis=1)

# Özellik ve hedef değişkenlerin ayrılması
X = data.drop(columns=['critic_score'])  # Özellikler
y = data['critic_score']  # Hedef değişken

# Eğitim ve test verilerinin ayrılması
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelin eğitilmesi
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Eğitim ve test verileri üzerinde tahminler yapma
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Modelin değerlendirilmesi
mse = mean_squared_error(y_test, y_test_pred)
print('Dogruluk:', mse)

# Tahminleri orijinal veri setine ekleme
data['Tahminler'] = pd.NA  # Tüm satırlara NA değeri atama

# Eğitim verileri için tahminler ekleme
data.loc[X_train.index, 'Tahminler'] = y_train_pred

# Test verileri için tahminler ekleme
data.loc[X_test.index, 'Tahminler'] = y_test_pred

# LabelEncoder nesneleri ile sayısal değerleri geri dönüştürme
for column, encoder in label_encoders.items():
    data[column] = encoder.inverse_transform(data[column].astype(int))

# Sonuçları CSV'ye yazma
data.to_csv('Sonuc.csv', index=False)

# Sonuç dosyasını okuma ve yazdırma
df = pd.read_csv('Sonuc.csv')
print(df)