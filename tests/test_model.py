"""
model.py icin temel birim testleri.
Model olusturma, egitim, degerlendirme ve kaydetme/yukleme adimlarini dogrular.
"""

import numpy as np
from src.model import (
    get_model,
    train_model,
    evaluate_model,
    save_model,
    load_model,
)

def test_model_factory():
    model_names= ["linear", "ridgecv", "rf", "gb"]
    for name in model_names:
        model = get_model(name)
        assert model is not None , f"model '{name}' oluşturulmadı!"

def test_train_and_evalute():
    #sahte veri oluşturma
    X=np.random.rand(50,3)
    y=np.random.rand(50)

    #model eğit
    model=get_model("ridgecv")
    model= train_model(model,X,y)

    #değerlendir
    scores =evaluate_model(model,X,y)    

    #test
    assert "r2" in scores, "R2 skoru yok"
    assert "rmse" in scores, "RMSE skoru yok"
    assert isinstance(scores["r2"], float), "R2 float olmali!"
    assert isinstance(scores["rmse"], float), "RMSE float olmali!"