import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score


def get_data() -> pd.DataFrame:
    # Read data
    df = pd.read_csv("jbi100_app/data/tic_data.csv")

    # Any further data preprocessing can go her
    # Remove rows with missing values (there are None)
    df = df.dropna()

    return df


def get_models_errors(df_train: pd.DataFrame, df_test: pd.DataFrame):
    """
    Trains NBc and DTc models on the training data and
     returns the models and their errors on the test data
     models are returned for feature importances
    :return:
    """
    train_features = df_train.drop("CARAVAN", axis=1)
    train_labels = df_train["CARAVAN"]
    test_features = df_test.drop("CARAVAN", axis=1)
    test_labels = df_test["CARAVAN"]

    # Apply naive bayes and decision tree
    nb_model = GaussianNB(var_smoothing=0.0001)
    dt_model = DecisionTreeClassifier(random_state=0)
    nb_model.fit(train_features, train_labels)
    dt_model.fit(train_features, train_labels)
    nb_y_pred = nb_model.predict(test_features)
    dt_y_pred = dt_model.predict(test_features)

    # Calculate accuracy, precision and recall
    nb_acc = accuracy_score(test_labels, nb_y_pred)
    nb_precision = precision_score(test_labels, nb_y_pred)
    nb_recall = recall_score(test_labels, nb_y_pred)
    dt_acc = accuracy_score(test_labels, dt_y_pred)
    dt_precision = precision_score(test_labels, dt_y_pred)
    dt_recall = recall_score(test_labels, dt_y_pred)

    return nb_model, dt_model, [nb_acc, nb_precision, nb_recall], [dt_acc, dt_precision, dt_recall]
