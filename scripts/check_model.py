"""
Model modülünün temel fonksiyonlarini manuel olarak test eden script.
CLI uzerinden calistirilabilir: python -m scripts.test
"""

import numpy as np
from datetime import datetime
import json

from src.model import (
    get_model,
    train_model,
    evaluate_model,
    save_model,
    load_model,
)

# ---- REPORT BUFFERS ----
report_text = ""

report_json = {
    "model_factory": None,
    "train_r2": None,
    "train_rmse": None,
    "save_load": None,
    "timestamp": datetime.now().isoformat()
}

def print_and_log(message):
    global report_text
    print(message)
    report_text += message + "\n"

print_and_log(">>> Model testleri baslatiliyor...\n")
#----

print_and_log("[1] Model Factory testi...")

model_names = ["linear", "ridgecv", "rf", "gb"]

for name in model_names:
    model = get_model(name)
    if model is None:
        print_and_log(f" Model olusturulamadi: {name}")
    else:
        print_and_log(f" Model olusturuldu: {name}")

print()

#----

print_and_log("[2] Train & Evaluate testi...")

# Sahte veri oluştur
X = np.random.rand(50, 3)
y = np.random.rand(50)

# Modeli oluştur ve eğit
model = get_model("ridgecv")
model = train_model(model, X, y)

# Değerlendir
scores = evaluate_model(model, X, y)

print_and_log(f"  R2: {scores['r2']:.4f}")
print_and_log(f"  RMSE: {scores['rmse']:.4f}\n")

#---

print_and_log("[3] Save & Load testi...")

# Modeli eğit
model = get_model("linear")
model = train_model(model, X, y)

# Kaydedilecek yol (sadece isim veriyoruz!)
save_path = "check_model_test.joblib"

# Kaydet
save_model(model, save_path)
print_and_log(f"  Model kaydedildi: models/{save_path}")

# Yükle
loaded = load_model(f"models/{save_path}")

# Tahmin testi
preds = loaded.predict(X)
print_and_log(f"  Yuklenen model isledi, tahmin sayisi: {len(preds)}\n")

#---
print_and_log(">>> Tum model testleri basariyla tamamlandi! ")


# --- RAPOR KAYDETME ---

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

txt_path = f"reports/check_model_{timestamp}.txt"
json_path = f"reports/check_model_{timestamp}.json"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(report_text)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(report_json, f, indent=4)

print_and_log(f"Raporlar kaydedildi:\n - {txt_path}\n - {json_path}\n")
