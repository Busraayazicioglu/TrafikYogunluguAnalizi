import pandas as pd
import numpy as np
import geohash2  # Geohash hesaplamak için
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Veri setini yükleyin
file_path = "C:/Users/Busra/Downloads/traffic_density__202404.csv"  # Dosya yolunu doğru şekilde ayarlayın
data = pd.read_csv(file_path)

# Zaman damgasını datetime formatına çevirin
data['DATE_TIME'] = pd.to_datetime(data['DATE_TIME'])

# Ek özellikler oluşturun
data['hour'] = data['DATE_TIME'].dt.hour
data['day_of_week'] = data['DATE_TIME'].dt.dayofweek
data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Trafik yoğunluğunu etkileyen ana özellikleri seçin
selected_features = ['hour', 'day_of_week', 'is_weekend', 'AVERAGE_SPEED', 'NUMBER_OF_VEHICLES', 'LATITUDE', 'LONGITUDE']
data = data[selected_features]

# GEOHASH kolonunu enlem ve boylamdan hesaplayın
data['GEOHASH'] = data.apply(lambda row: geohash2.encode(row['LATITUDE'], row['LONGITUDE']), axis=1)

# Giriş ve hedef değişkenlerini ayırın
X = data[['hour', 'day_of_week', 'is_weekend', 'AVERAGE_SPEED']]
y = data['NUMBER_OF_VEHICLES']

# Eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturun
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)  # Çıkış katmanı
])

# Modeli derleyin
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Modeli eğitin
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Modeli kaydedin
model.save("traffic_density_model.h5")

# Kaydedilen modeli yükleyin
loaded_model = load_model("traffic_density_model.h5")

# Doğruluk oranını hesaplayın
y_pred_train = loaded_model.predict(X_train)  # Eğitim seti tahminleri
y_pred_test = loaded_model.predict(X_test)  # Test seti tahminleri

# Eğitim ve test seti doğruluk oranları
train_mae = mean_absolute_error(y_train, y_pred_train)
test_mae = mean_absolute_error(y_test, y_pred_test)

# Ortalama değerler üzerinden doğruluk yüzdesi
average_train = y_train.mean()
average_test = y_test.mean()

train_accuracy = 100 - (train_mae / average_train * 100)
test_accuracy = 100 - (test_mae / average_test * 100)

print(f"Eğitim seti doğruluk oranı: %{train_accuracy:.2f}")
print(f"Test seti doğruluk oranı: %{test_accuracy:.2f}")

# Kullanıcıdan giriş al
geohash_input = input(f"Lütfen geohash kodunu girin (örnek: {', '.join(data['GEOHASH'].unique()[:5])}): ")
kullanici_saat = input("Lütfen bir saat girin (örnek: 09:00): ")
hour = int(kullanici_saat.split(":")[0])  # Saat bilgisini alın

# Kullanıcının ortalama hız girdisi
ortalama_hiz = float(input("Tahmini ortalama hızını girin (örnek: 40): "))
day_of_week = int(input("Haftanın gününü girin (0: Pazartesi - 6: Pazar): "))
is_weekend = 1 if day_of_week >= 5 else 0

# Model girdisi
input_features = np.array([[hour, day_of_week, is_weekend, ortalama_hiz]])

# Modelden tahmin al
tahmin = loaded_model.predict(input_features)

# Sonucu ekrana yazdır
print(f"{geohash_input} geohash bölgesinde, {kullanici_saat} saatinde, haftanın {day_of_week}. günü, tahmini trafik yoğunluğu: {tahmin[0][0]} araç")

# Isı haritası için veri hazırlama
heatmap_data = []
for h in range(24):
    input_features = np.array([[h, day_of_week, is_weekend, ortalama_hiz]])
    prediction = loaded_model.predict(input_features)
    heatmap_data.append(prediction[0][0])

# Isı haritasını oluşturun ve görselleştirin
plt.figure(figsize=(10, 6))
sns.heatmap(
    np.array(heatmap_data).reshape(-1, 1),
    annot=True,
    fmt=".1f",
    cmap="YlOrRd",
    cbar=True
)
plt.title(f"Geohash: {geohash_input} - Saatlik Trafik Yoğunluğu")
plt.yticks(np.arange(24) + 0.5, [f"{h}:00" for h in range(24)], rotation=0)
plt.xlabel("Saat")
plt.ylabel("Saat Dilimi")
plt.show()
