# Feature Engineering (Özellik Mühendisliği) Raporu

**Tarih:** 09.01.2025
**Dosya:** `03_feature_engineering.ipynb`

---

## 1. Giriş
Baseline modelin yetersiz kalmasının temel sebebi, verinin ham halinde (raw) bulunan karmaşık ilişkilerin model tarafından çözülememesiydi. Bu çalışmada, veriye **domain bilgisi (alan bilgisi)** katılarak modelin işi kolaylaştırılmıştır.

## 2. Uygulanan Teknikler

### A. Zaman Mühendisliği (Temporal Engineering)
* **Zaman Dilimleme (`time_label`):** Saat verisi sadece bir sayı olmaktan çıkarılıp insan davranışına göre gruplandı.
    * `0`: Gece (Düşük Aktivite)
    * `1`: Sabah İşe Gidiş (Yüksek Talep)
    * `2`: Gündüz
    * `3`: Akşam İş Çıkışı (En Yüksek Talep)
    * `4`: Gece Yarısı
* **Hafta Sonu (`is_weekend`):** Cumartesi ve Pazar günleri işaretlendi.

### B. Anlamsal Kodlama (Semantic One-Hot Encoding)
Klasik `1, 2, 3` kodlaması yerine, sütunlar okunabilir hale getirilerek ikili (binary) sisteme çevrildi. Bu sayede modelin **Kış mevsimini sayısal olarak İlkbahar'dan büyük sanması** engellendi.

* **Dönüşüm Tablosu:**
    * `season` -> `season_Spring`, `season_Summer`, `season_Fall`, `season_Winter`
    * `weather` -> `weather_Clear_FewClouds`, `weather_Mist_Cloudy`, `weather_Light_Rain_Snow`, `weather_Heavy_Rain_Ice`

Bu yaklaşım, modelin yorumlanabilirliğini (Interpretability) artırmıştır.

### C. Hedef Değişken Stabilizasyonu (Log Transform)
* **Sorun:** Bisiklet kiralama sayıları (`count`) aşırı sağa çarpık (skewed) bir dağılıma sahipti.
* **Çözüm:** `np.log1p` (Logaritma) dönüşümü uygulandı.
* **Sonuç:** Veri dağılımı "Normal Dağılım"a (Gaussian) yaklaştı. Bu işlem, özellikle RMSE/RMSLE metriğini optimize eden modellerde performansı artırır.

## 3. Sonuç ve Karar
Veri seti artık ham sayı yığınından, anlamlı özellikler (features) kümesine dönüşmüştür. Karmaşık (Advanced) özellikler yerine **sağlam ve açıklanabilir (Robust & Explainable)** özellikler tercih edilmiştir.

**Sıradaki Adım:** Oluşturulan `processed` veri seti ile **Random Forest** modeli kurulacaktır.