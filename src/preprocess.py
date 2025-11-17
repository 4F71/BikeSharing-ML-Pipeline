"""
Modül: preprocess
Amaç: Bike Sharing Demand verisi için özellik mühendisliği, encoding ve ölçeklendirme işlemlerini yapmak.
Yazar: Yedi Sarman
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED  = BASE_DIR / "data" / "processed"

def extract_datetime_features(df: pd.DataFrame):
    
    ##çözümlenen hatalar: 
        #extract_datetime_features(df): // yapıldığında ide(vscode) dataframe olduğunu bilmiyordu
        #extract_datetime_features(df: pd.DataFrame): bu şekilde typehint oluşutarak fonksiyonu düzelttik.

    

    #bu veriseti için skor yükseltecek kısım: datetime kolonu, object olarak çıktı aldığımız için datetime64 tipine dönüştürüyoruz.
    #sonrasında dt.year/dt.month / dt.day/ dt.hour / dt.dayofweek ' olarak ulaşabileceğiz. feature engineering' ile model skoru için kıymetli featureler.
    df["datetime"] =pd.to_datetime(df["datetime"])
    df["year"] = df["datetime"].dt.year
    df["month"] = df["datetime"].dt.month
    df["hour"] = df["datetime"].dt.hour
    df["dayofweek"] = df["datetime"].dt.dayofweek
    df= df.drop(columns=["casual","registered"], errors="ignore")
    
    target=None
    if "count" in df.columns:
        target = df["count"]
        df = df.drop(columns=["count"])

     # Sayısal sütunları tespit et (scaling için kullanılacak)
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
     # Kategorik sütunları  tespit et (one-hot encoding için)
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    preprocessor=ColumnTransformer(
        transformers=[
            ("num",StandardScaler(),numeric_cols),
            #handle_unknown="ignore" yazmazsak:  train & test datasında olamayan sütunlar sebebiyle hata alırız
            #bu sayede encoder kolonu "0" ile doldurup geçecek
            ("cat",OneHotEncoder(handle_unknown="ignore"),categorical_cols)
        
        ],
        #yeni oluşturulan featureler standardscaler & onehotencoder'e gitmiyor, bu yüzden 
        #remainder="passthrough" ile ColumnTransformer’e gitmeyen sütünların kaybolmamasını sağlıyoruz.
        remainder="passthrough"

        #handle_unknown="ignore" &  remainder="passthrough" olmazsa preprocessing pipeline çökecektir!
    )

    #numeric sütunlara / STANDARDSCALER
    #categorical sütunlara / ONEHOTENCODER
    #geri kalan sütunlara / PASSTHROUG 
                                            #uygulacak 
    
    
    preprocessor.fit(df)

    transformed = preprocessor.transform(df)



    transformed = preprocessor.transform(df)
    
    transformed_df = pd.DataFrame(transformed)

    #İşlenmiş (scaled + encoded + FE’li) veriyi kaydediyoruz,
    transformed_df.to_csv(DATA_PROCESSED/"processed_features.csv", index=False)

    #model eğitimi için çağıracağımız blok, testimiz eğer target yoksa kaydetmesi için bir try/cache bloğu
    if target is not None:
        target.to_csv(DATA_PROCESSED / "processed_target.csv", index=False)
    
    #transformed_df: model için hazır feature set
    #target:train'de count sütunu / testte:none

    return transformed_df,target









        