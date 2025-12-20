# BikeSharing ML Pipeline

Bu proje, şehir içi bisiklet paylaşım sistemlerinde **saatlik talep tahmini**
problemine yönelik uçtan uca bir **makine öğrenmesi pipeline’ı** geliştirmeyi amaçlamaktadır.

Çalışma, Kaggle *Bike Sharing Demand* veri seti üzerinde;
problem tanımı, keşifsel veri analizi (EDA), feature engineering ve modelleme
aşamalarını **adım adım ve dokümante edilmiş** bir şekilde ele alır.

Amaç yalnızca skor üretmek değil,
**veriye dayalı karar alma sürecini şeffaf ve tekrar edilebilir** biçimde kurmaktır.

---

## 📌 Problem Tanımı

Bisiklet paylaşım sistemlerinde talep; zaman, mevsimsellik ve çevresel faktörlere
bağlı olarak önemli ölçüde değişkenlik göstermektedir.

Bu projede amaç, saatlik bisiklet kiralama sayısını (`count`)
zaman ve çevresel değişkenler yardımıyla **regresyon problemi** olarak tahmin etmektir.

Detaylı problem tanımı için:  
📄 `docs/problem_definition.md`

---

## 📂 Proje Yapısı

```
BikeSharing-ML-Pipeline/
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_baseline.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_model_training.ipynb
│ ├── 05_model_evaluation.ipynb
│ └── 06_final_pipeline.ipynb
├── docs/
│ ├── problem_definition.md
│ ├── eda_report.md
│ ├── feature_engineering_report.md
│ ├── baseline_report.md
│ └── final_report.md
├── figures/
├── requirements.txt
└── README.md
```

---

## 🔍 Keşifsel Veri Analizi (EDA)

EDA süreci, modelleme kararlarını yönlendirecek şekilde yapılandırılmıştır.

Bu kapsamda:
- Hedef değişken dağılımı ve dönüşümler
- Zaman bazlı talep paternleri (saat, gün, ay, sezon)
- Mevsimsellik ve kullanım davranışları

incelenmiş ve bulgular ayrı bir rapor halinde dokümante edilmiştir.

📄 `docs/eda_report.md`

---

## 🚧 Proje Durumu

🟡 **Devam Ediyor**

- Kapsamlı EDA tamamlanma aşamasında  
- Feature engineering ve modelleme adımlarına geçilmektedir

---

## 📬 İletişim

- GitHub: https://github.com/4F71
