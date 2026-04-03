from src.data.ingest import load_credit_data
from src.data.preprocess import standardize_column_names, handle_missing_values


def main():
    df = load_credit_data()

    df = standardize_column_names(df)
    df = handle_missing_values(df)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nPreview:")
    print(df.head())


if __name__ == "__main__":
    main()