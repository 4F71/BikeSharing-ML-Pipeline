#  EDA Raporu

**Proje:** Bike Sharing Demand Prediction
**Tarih:** 09.01.2025


---

## 1. Genel Bakış
Bu doküman, bisiklet kiralama veri seti üzerinde yapılan detaylı analizlerin, veri kalitesi kontrollerinin ve model stratejisine yönelik alınan kararların özetini içerir. Analiz sürecinde hedef değişkenin (`count`) zamansal, meteorolojik ve kategorik faktörlerle olan ilişkisi incelenmiştir.

## 2. Kritik Bulgular (Key Insights)

### A. Hedef Değişken (Count)
* **Dağılım:** Veri sağa çarpık (Right-skewed) bir yapıdadır. Çoğu saatte talep düşüktür, yüksek talep nadirdir.
* **Aksiyon:** Model performansını artırmak ve RMSLE metriğine uyum sağlamak için hedef değişkene **Logaritmik Dönüşüm (`np.log1p`)** uygulanacaktır.

### B. Zamansal Desenler (Time-Series Patterns)
* **Saatlik Davranış:** Kullanıcı davranışında iki farklı desen tespit edilmiştir:
    * **İş Günleri (Working Day):** Sabah 08:00 ve Akşam 17:00-18:00 saatlerinde iki büyük zirve (Commuter trafiği).
    * **Hafta Sonu:** Öğlen 12:00-16:00 arasında tek bir geniş zirve (Gezi/Eğlence).
* **Mevsimsellik:** Talep, kış aylarında (Ocak-Şubat) dip yaparken, Yaz ve Erken Sonbahar (Haziran-Eylül) aylarında zirveye ulaşmaktadır.
* **Yıllık Trend:** 2012 yılı talebi, 2011 yılına göre belirgin bir artış göstermektedir (Büyüme trendi).

### C. Hava Durumu Etkisi
* **Sıcaklık:** Talep ile sıcaklık arasında pozitif ancak doğrusal olmayan bir ilişki vardır. Çok soğuk ve çok sıcak havalarda talep düşmektedir.
* **Veri Kalitesi:** `windspeed` (Rüzgar hızı) değişkeninde yapay `0` değerleri tespit edilmiştir. Bu değerler muhtemelen ölçülemeyen verilerin doldurulmasıdır.

### D. Veri Sızıntısı (Data Leakage) Riski
* `casual` ve `registered` sütunları, hedef değişken `count`'un alt bileşenleridir (`count = casual + registered`).
* Test setinde bu sütunlar bulunmamaktadır. Bu nedenle model eğitiminde **Feature olarak kullanılmayacaklardır.**

## 3. Feature Engineering Stratejisi

Analiz sonucunda modelde kullanılması planlanan stratejiler:

1.  **Türetilecek Değişkenler:** `hour`, `month`, `year`, `dayofweek`.
2.  **Dönüşümler:** `count` -> `log(count+1)`.
3.  **Etkileşimler (Interactions):** Saat bilgisinin anlamı güne göre değiştiği için `hour` * `workingday` etkileşimi model için kritiktir.
4.  **Temizlik:** `weather=4` verisi birleştirilecek, `windspeed=0` değerleri için imputation stratejisi geliştirilecek.

## 4. Sonuç
Veri seti, güçlü mevsimsel ve zamansal desenler barındırmaktadır. Basit lineer modeller yerine, bu desenleri ve kırılımları yakalayabilecek **Ağaç Tabanlı Modellerin (XGBoost, Random Forest vb.)** daha başarılı olacağı öngörülmektedir.