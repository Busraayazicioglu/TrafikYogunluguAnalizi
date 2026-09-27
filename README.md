# İstanbul Trafik Yoğunluğu Tahmin Projesi

Bu proje, İstanbul'a ait trafik verilerini kullanarak trafik yoğunluğunu tahmin etmek amacıyla geliştirilmiş bir yapay zeka projesidir.

## Projenin Amacı

Projenin amacı; trafik verilerindeki araç sayısı, ortalama hız, maksimum/minimum hız, zaman ve konum gibi değişkenleri kullanarak trafik yoğunluğunu tahmin etmektir.

## Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow / Keras
* Matplotlib

## Kullanılan Veri

Projede İstanbul Büyükşehir Belediyesi'ne ait trafik verileri kullanılmıştır.

Veri setinde bulunan bazı değişkenler:

* `DATE_TIME` – Tarih ve saat
* `LONGITUDE` – Boylam
* `LATITUDE` – Enlem
* `GEOHASH` – Konum bilgisi
* `MINIMUM_SPEED` – Minimum hız
* `MAXIMUM_SPEED` – Maksimum hız
* `AVERAGE_SPEED` – Ortalama hız
* `NUMBER_OF_VEHICLES` – Araç sayısı

## Proje Aşamaları

1. Trafik verilerinin Python ile okunması
2. Verilerin incelenmesi ve temizlenmesi
3. Eksik ve hatalı verilerin kontrol edilmesi
4. Verilerin modele uygun hale getirilmesi
5. Eğitim ve test verilerinin ayrılması
6. TensorFlow/Keras kullanılarak yapay sinir ağı modelinin oluşturulması
7. Modelin eğitilmesi
8. Tahmin sonuçlarının değerlendirilmesi
9. Hata oranlarının incelenmesi ve modelin geliştirilmesi

## Yapay Zeka Kullanımı

Projede TensorFlow/Keras kullanılarak yapay sinir ağı (ANN) modeli oluşturulmuştur. Model, trafik verileri arasındaki ilişkileri öğrenerek trafik yoğunluğu tahmini yapmaktadır.

Geliştirme sırasında AI araçlarından; Python kodlarının geliştirilmesi, kullanılan kütüphanelerin araştırılması, karşılaşılan hataların anlaşılması ve farklı çözüm yöntemlerinin değerlendirilmesi aşamalarında destek alınmıştır. Ancak verilerin hazırlanması, modelin kurulması, test edilmesi ve sonuçların değerlendirilmesi proje kapsamında tarafımdan gerçekleştirilmiştir.

## Karşılaşılan Problemler

Proje sırasında veri kalitesi, eksik veriler ve modelin beklenen doğruluk seviyesine ulaşmaması gibi problemlerle karşılaşılmıştır.

Bu problemleri çözmek için veriler analiz edilmiş, gerekli veri temizleme işlemleri yapılmış ve model farklı şekilde test edilmiştir. Modelin sonuçları hata metrikleri kullanılarak değerlendirilmiş ve iyileştirme yapılabilecek noktalar belirlenmiştir.

## Proje Durumu

Proje geliştirme ve iyileştirme aşamasındadır. Özellikle veri kalitesinin iyileştirilmesi ve model performansının artırılması üzerine çalışmalar yapılabilir.
