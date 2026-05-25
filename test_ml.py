# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import compute_model_metrics, train_model


# TODO: implement the first test. Change the function name and input as needed
def test_apply_label():
    """
    Tests that the apply_label function returns the correct salary label.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Tests that the train_model function returns a RandomForestClassifier.
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Tests that the compute_model_metrics function returns expected values.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert round(precision, 2) == 1.00
    assert round(recall, 2) == 0.67
    assert round(fbeta, 2) == 0.80
