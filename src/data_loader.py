"""
Modül: data_loader
Amaç:Bike Sharing Demand projesi için ham CSV verilerini yüklemek ve doğrulamak
Yazar: yedisarman
"""
from pathlib import Path
import pandas as pd


# Ana proje dizini ve veri yolları
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"


def load_data():
    
    """
    Bike Sharing Demand verilerini yükler ve temel kontrolünü yapar.
    
    Returns:
        tuple: (train_df, test_df, sample_submission_df)
    """


    train_path =DATA_RAW  / "train.csv"
    test_path = DATA_RAW  / "test.csv"
    sub_path = DATA_RAW   / "sampleSubmission.csv"

    for file in [train_path,test_path,sub_path]:
        if not file.exists():
            raise FileNotFoundError(f"Dosya yoğk: {file}")
        
    train_df= pd.read_csv(train_path)
    test_df=pd.read_csv(test_path)
    sample_submission_df=pd.read_csv(sub_path)

    

    return train_df,test_df,sample_submission_df


def summary_report(df, name="DataFrame"):
    """
    Verilen DataFrame için hızlı bir özet raporu üretir.
    """

    print(f"\n {name} özeti") 
    print(f"Boyut: {df.shape}")
    print(f"Eksik değerler:\n {df.isnull().sum()}")
    print(f"veri tipleri: \n {df.dtypes}")
    print("─" * 40)
    return



if __name__ == "__main__":
    train_df, test_df, sub_df = load_data()
    summary_report(train_df, "Train")
    summary_report(test_df, "Test")

