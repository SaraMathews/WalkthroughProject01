import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
   
    
"""
1. **Train, Validation, and Test Set: Labels Frequencies:**
The function starts by displaying the image showing the distribution of labels
across the train, validation, and test sets. This image was previously saved in
the `outputs/{version}/labels_distribution.png` file. It represents the number
of images for each label in each dataset split.

2. **Model History:** 
Next, the function displays the model training accuracy and losses over time. 
It uses two columns to show the images side by side.
The `model_training_acc.png` image shows how the model's accuracy changed
during training, while the `model_training_losses.png` image displays the
changes in the model's loss function over training epochs.

3. **Generalized Performance on Test Set:** Lastly, the function displays the
general performance of the model on the test set. It loads the evaluation
results (loss and accuracy) from the `load_test_evaluation(version)` function
and presents them in a DataFrame. The `load_test_evaluation()` function
retrieves evaluation metrics such as loss and accuracy from a saved file
(`outputs/{version}/evaluation.pkl`) for the test set's performance.

Overall, the `page_ml_performance_metrics()` function provides an overview of
the model's performance by showing training history (accuracy and loss),
the distribution of labels in different datasets, and evaluation metrics for
the test set. This page helps users understand how the model trained and how
well it performs on unseen data.
"""
