import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')


"""
The `load_test_evaluation(version)` function in the `evaluate_clf.py` file is
responsible for loading the evaluation results of the trained model on the
test set.

1. `import streamlit as st`: This line imports the Streamlit library,
which is used for building interactive web applications.

2. `from src.data_management import load_pkl_file`:
This line imports the `load_pkl_file` function from the `data_management.py`
file located in the `src` folder. The `load_pkl_file` function is likely a
utility function that loads a pickled (serialized) file containing evaluation
results.

3. `def load_test_evaluation(version)`:
This line defines the function `load_test_evaluation`, which takes one argument
`version`. The `version` argument is a string that indicates the version of the
model for which evaluation results are to be loaded (e.g., 'v1').

4. `return load_pkl_file(f'outputs/{version}/evaluation.pkl')`:
This line returns the evaluation results loaded from a pickled file named
`evaluation.pkl` located in the `outputs/{version}` directory.
The `load_pkl_file` function is called with the appropriate file path
to load the data.

The purpose of this function is to retrieve evaluation metrics
(e.g., loss and accuracy) of the model's performance on the test set.
It is used in the `page_ml_performance_metrics()` function
(from the `page_ml_performance.py` file) to display the general performance of
the model on the test set. By loading the evaluation results, it allows users
to assess how well the model performs on unseen data.
"""
