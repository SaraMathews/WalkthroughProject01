import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Parasitised': 0, 'Uninfected': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


"""
(def plot_predictions_probabilities)
Is responsible for plotting the prediction probabilities for each class
of the input image.

1. The function takes two arguments: `pred_proba` (a floating-point value
representing the predicted probability of the positive class) and `pred_class`
(a string indicating the predicted class label).

2. Inside the function, a pandas DataFrame called `prob_per_class` is created
to hold the probabilities for each class ('Parasitised' and 'Uninfected').
It initializes the DataFrame with probabilities set to 0.

3. The function then updates the probability for the predicted class
`pred_class` in the `prob_per_class` DataFrame with the value from
`pred_proba`. This indicates the model's confidence in predicting that the
input image belongs to the predicted class.

4. Since the DataFrame is initialized with 0 probabilities, the function also
sets the probability for the non-predicted class (the class not equal to
`pred_class`) to `1 - pred_proba`. This is because in a binary classification
scenario, the sum of probabilities for both classes should be 1.

5. The `prob_per_class` DataFrame is then rounded to three decimal places and a
new column 'Diagnostic' is added with the class labels as its values.

6. The function uses Plotly Express (`px.bar`) to create a bar plot with
`prob_per_class`. The x-axis represents the class labels
('Parasitised' and 'Uninfected'), and the y-axis represents the corresponding
probabilities. The y-axis range is set to [0, 1] to ensure that probabilities
are properly scaled.

7. Finally, the function uses Streamlit's `st.plotly_chart()` method to display
the Plotly bar chart in the Streamlit web application.

In summary, this function takes the predicted probability and class label of an
image and creates a bar chart that visualizes the model's prediction
probabilities for each class. This helps users understand the confidence of the
model's prediction for a given input image.
"""


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


"""
(def resize_input_image)
Is responsible for resizing an input image to the average image size used during
training.

1. The function takes two arguments: `img` (the input image as a PIL image) and
`version` (a string representing the version of the model to be used).

2. The function loads the image shape used during training from a pickled file
(`image_shape.pkl`) located in the `outputs/{version}` directory. This shape
represents the average size of images in the training dataset.

3. The input image `img` is then resized using the `resize()` method of the PIL
image. The target size is set to the average image size obtained from the
`image_shape` variable.

4. After resizing, the image is converted to a NumPy array, and its pixel
values are rescaled to be in the range [0, 1] by dividing each pixel value
by 255. This step ensures that the image is normalized before being fed into
the model.

5. Finally, the resized and normalized image is wrapped in an extra dimension
using `np.expand_dims()` to match the shape expected by the model during
inference. The extra dimension is added at the beginning to represent a batch
of size 1 (as the model expects batched input).

6. The resized and normalized image is returned from the function.

In summary, this function takes an input image, resizes it to the average image
size used during training, and prepares it for feeding into the model for
inference. Resizing the input image to the same size as the training images
ensures that the model can make accurate predictions on images of consistent
dimensions.
"""


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/malaria_detector_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Parasitised': 0, 'Uninfected': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample cell is "
        f"**{pred_class.lower()}** with malaria.")

    return pred_proba, pred_class


"""
(def load_model_and_predict)
Is responsible for loading a pre-trained model and using it to predict whether
an input image contains a malaria parasite or not.

1. The function takes two arguments: `my_image` (the input image as a NumPy
array with normalized pixel values) and `version` (a string representing the
version of the model to be used).

2. The function loads the pre-trained model from an HDF5 file
(`malaria_detector_model.h5`) located in the `outputs/{version}` directory.
This model is the trained malaria detector model that was saved during the
training phase.

3. The loaded model is then used to predict the probability of the input image
belonging to the class "Parasitised" (infected with malaria). The prediction
probability is obtained using the `predict` method of the model, and the output
is a single scalar value.

4. The function maps the prediction probability to a class label
("Parasitised" or "Uninfected") using a threshold of 0.5. If the predicted
probability is greater than 0.5, the image is classified as "Parasitised"
(infected with malaria), otherwise as "Uninfected".

5. If the predicted class is "Parasitised", the function reverts the
probability to represent the probability of the image being
"Uninfected" (1 - predicted probability). This step is helpful in case the user
is interested in knowing the probability of the image being "Uninfected"
rather than "Parasitised."

6. The function displays the result of the predictive analysis, indicating
whether the sample cell is predicted to be "Parasitised" or "Uninfected" with
malaria.

7. The function returns the predicted probability and the predicted class as
a tuple.

In summary, this function loads the pre-trained model and uses it to predict
the class label and probability of an input image. The result is then displayed
to the user, indicating whether the sample cell is predicted to be infected
with malaria or not.
"""
