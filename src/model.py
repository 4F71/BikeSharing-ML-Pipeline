"""
model.py
--------
Modelleri oluşturan, eğiten,değerlendiren ve kaydeden çekirdek modül.
"""
#yol yönetimi için
from pathlib import Path
#model kaydetme/yükleme için
import joblib
#modelleri getirir
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
#Skor hesapları için r2 ve rmse fonksiyonları
from sklearn.metrics import r2_score, mean_squared_error


#modellerin kaydedileceği klasör:
MODEL_DIR=Path("models")
#exist_ok=true" klasör yoksa oluşturur
MODEL_DIR.mkdir(exist_ok=True)

def get_model(name):
    """
    Verilen model adina gore uygun sklearn regresyon modelini dondurur.
    
    Parametreler
    ------------
    name : str
        'linear', 'ridge', 'rf' veya 'gb' model adlarindan biri.

    Donus
    -----
    model : sklearn estimator
        Hazır sklearn regresyon modeli.
    """
    #büyük-küçük harf kontrolü hata sebebiyle eklendi.
    name == name.lower()

    if name == "linear":
        return LinearRegression()
    
    elif name == "ridgecv":
        return RidgeCV(alphas=[0.1, 1.0, 10.0])
    
    elif name=="rf":
        return RandomForestRegressor(
            
            n_estimators=200,
            #evrenin rakamı 42 :)
            random_state=42,
            #kullanacağı cpu çekirdeği// -1 tüm çekirdekleri kullanır
            n_jobs=-1
        )
    elif name=="gb":
        return GradientBoostingRegressor(
            random_state=42
        )
    else:
        #raise "print(mesaj'dan)"" ya da "Warning(uyarı'dan )"farklı programı durdurmasını sağlayan bir hata mesajıdır
        raise ValueError(f"Desteklenmeyen model adı: {name}")
    
        
    
