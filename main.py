from src.data_loader import load_data
from src.eda import basic_info, check_missing_values, plot_churn_distribution
from src.preprocessing import clean_data
from src.train import train_pipeline, save_pipeline
from src.evaluate import evaluate_model, plot_confusion_matrix, plot_roc_curve
from sklearn.model_selection import train_test_split


def main():
    print("\n🚀 Starting Customer Churn Pipeline...\n")

    # Load data
    df = load_data()
    if df is None:
        return

    # EDA
    basic_info(df)
    check_missing_values(df)
    plot_churn_distribution(df)

    # Cleaning
    df = clean_data(df)

    # Split
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train pipeline
    pipeline = train_pipeline(df)

    # Evaluate
    y_pred = evaluate_model(pipeline, X_test, y_test)
    plot_confusion_matrix(y_test, y_pred)
    plot_roc_curve(pipeline, X_test, y_test)

    # Save
    save_pipeline(pipeline)

    print("\n✅ Project completed successfully!")


if __name__ == "__main__":
    main()