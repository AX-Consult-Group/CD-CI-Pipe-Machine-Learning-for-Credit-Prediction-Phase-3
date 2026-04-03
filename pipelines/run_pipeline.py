# pipelines/run_pipeline.py

from src.data.ingest import load_data
from src.data.preprocess import preprocess_data
from src.data.split import split_data


def run_pipeline(data_path):
    print("Starting pipeline...")

    df = load_data(data_path)
    df = preprocess_data(df)

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    print("Done ✅")
    print(f"Train: {X_train.shape}")
    print(f"Val: {X_val.shape}")
    print(f"Test: {X_test.shape}")


if __name__ == "__main__":
    data_path = "data/raw/your_data.csv"  # update this
    run_pipeline(data_path)