"""
bu bir test bloğudur
--------------------
çalıştırmak için:

    scripts/test_preprocess.py

"""


from src.data_loader import load_data
from src.preprocess import extract_datetime_features

train_df, test_df, _ = load_data()

processed_train, train_target = extract_datetime_features(train_df)

print("Train processed:", processed_train.shape)
print("Train target:", train_target.shape)

processed_test, test_target = extract_datetime_features(test_df)

print("Test processed:", processed_test.shape)
print("Test target:", test_target)
