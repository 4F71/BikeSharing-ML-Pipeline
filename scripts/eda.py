"""
Dataset incelemesi

    çalıştırma: python -m scripts.eda
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime


#DATASET YOLUNU BUL

DATA_DIR = Path("data/raw")
TRAIN_PATH = DATA_DIR / "train.csv"
TEST_PATH = DATA_DIR / "test.csv"

if not TRAIN_PATH.exists():
    raise FileNotFoundError(f"Train dataset bulunamadi: {TRAIN_PATH}")


# RAPOR HAZIRLAMA

report_text = ""

def log(msg):
    """CLI + rapor için çift yazma"""
    global report_text
    print(msg)
    report_text += msg + "\n"
    
# EDA BAŞLANGIÇ

log("EDA Baslatiliyor...\n")
log(f"Dataset klasoru: {DATA_DIR}\n")

# VERIYI OKU

log("1/ Train.csv yukleniyor...")
df = pd.read_csv(TRAIN_PATH)
log(f" ✔ Train set yuklendi: {df.shape} (satir, kolon)\n")

# ILK SATIRLAR


log("2/ Ilk 5 satir:")
log(df.head().to_string())
log("")

# KOLON TIPLERI

log("3/ Kolon tipleri:")
log(df.dtypes.to_string())
log("")

# EKSİK DEĞER ANALIZI

log("4/Eksik deger analizi:")
missing = df.isnull().sum()
log(missing.to_string())
log("")

# SAYISAL VE KATEGORIK AYRIMI

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

log("5/ Sayisal kolonlar:")
log(", ".join(numeric_cols) + "\n")

log("6/ Kategorik kolonlar:")
log(", ".join(categorical_cols) + "\n")

# SAYISAL KOLON ISTATİSTIKLERI

log("7/ Sayisal kolon ozet istatistikleri:")
log(df[numeric_cols].describe().to_string())
log("")

# PATTERN / POTANSIYEL LEAKAGE KONTROLU



log("[8] Potansiyel leakage kontrolu:")

target_candidates = [c for c in df.columns if "price" in c.lower() or "cnt" in c.lower() or "target" in c.lower()]

if target_candidates:
    log(f" Muhtemel hedef benzeri kolonlar: {target_candidates}\n")
else:
    log(" Leakage belirtisi yok.\n")

# RAPORU KAYDET

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = Path("reports") / f"eda_report_{timestamp}.txt"

with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_text)

log(f"Rapor kaydedildi: {report_path}")
log("EDA Tamamlandi ")