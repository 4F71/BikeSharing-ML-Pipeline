#  Baseline Model Raporu

**Tarih:** 09.01.2025
**Dosya:** `02_baseline.ipynb`

---

## 1. Amaç
Karmaşık makine öğrenmesi modellerine geçmeden önce "Hiçbir şey yapmasak ne kadar hata yapıyoruz?" sorusuna yanıt aramak ve geçilmesi gereken minimum başarı skorunu belirlemektir.

## 2. Sonuçlar

| Model | RMSLE Skoru | Açıklama |
| :--- | :---: | :--- |
| **Naive (Ortalama)** | **1.58** | Her saate sadece ortalamayı atayan model. (En kötü senaryo) |
| **Linear Regression** | **1.30** | Saat ve sıcaklık ilişkisine bakan basit model. |

## 3. Tespit Edilen Kritik Sorunlar
Modelin çıktıları incelendiğinde şu sistemsel hatalar görülmüştür:
* **Negatif Değer Üretimi:** Model, talebin düşük olduğu saatlerde `0` yerine `-15` gibi fiziksel olarak imkansız tahminler üretmiştir.
* **Doğrusallık Sorunu:** Bisiklet talebi mevsimsel ve saatlik olarak eğrisel (non-linear) bir yapıdadır. Lineer model bu yapıyı öğrenememiştir (Underfitting).

## 4. Nihai Karar ve Strateji
* **KARAR:** Linear Regression modeli, yukarıdaki hatalar nedeniyle **final model olarak kullanılmayacaktır.** Sadece kıyaslama (benchmark) amacıyla saklanacaktır.
* **SONRAKİ ADIM:** Veri setindeki karmaşık desenleri yakalayabilmek için **Feature Engineering** yapılacaktır.
* **HEDEF MODELLER:** Doğrusal olmayan ilişkileri çözebilen **Decision Trees (Karar Ağaçları), Random Forest** veya **Gradient Boosting (XGBoost)** modelleri denenecektir.