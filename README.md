# K-Means ile Müşteri Segmentasyonu

Bu proje, **K-Means algoritmasını öğrenmek ve uygulamak** amacıyla hazırlanmıştır.  
Projede, bir müşteri veri seti üzerinde yaş ve harcama hacmi özellikleri kullanılarak müşteriler üç gruba ayrılmıştır:  

- Yüksek Hacim  
- Orta Hacim  
- Düşük Hacim  

## Kullanılan Kütüphaneler
- `numpy`  
- `pandas`  
- `matplotlib`  
- `sklearn` (KMeans)

## Projenin Amacı
- K-Means algoritmasının çalışma mantığını görmek  
- Veri üzerinden kümeler oluşturmak  
- Küme merkezlerini görselleştirmek  
- Küme sonuçlarını tabloya ekleyerek analiz etmek  

## Kullanım
1. `musteriler.csv` dosyasını aynı klasöre koyun veya örnek veri oluşturun.  
2. Python ile `kmeans_musteriler.py` dosyasını çalıştırın.  
3. Kod çalıştıktan sonra:  
   - Grafiklerde kümeler renkli olarak gösterilecektir.  
   - Tablo üzerinde her müşterinin hangi kümeye ait olduğu ve küme isimleri görünecektir.

## Örnek Çıktı

| No | Cinsiyet | Yas | Hacim  | Maas | Küme | Küme İsmi     |
|----|----------|-----|--------|------|------|---------------|
| 1  | K        | 60  | 69900  | 6325 | 0    | yüksek hacim  |
| 2  | K        | 30  | 79000  | 5200 | 0    | yüksek hacim  |
| 3  | E        | 52  | 85500  | 7825 | 1    | orta hacim    |
| 4  | E        | 57  | 17100  | 8375 | 2    | dusuk hacim   |

---

Kod, K-Means algoritmasını **adım adım öğrenmek ve görselleştirmek** isteyenler için hazırlanmıştır.
"# kmeans-musteri-segmentasyonu" 
