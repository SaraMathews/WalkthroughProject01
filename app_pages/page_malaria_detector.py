import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_malaria_detector_body():
    st.info(
        f"* The client is interested in telling whether a given cell contains a malaria parasite "
        f"or not."
        )

    st.write(
        f"* You can download a set of parasitised and uninfected cells for live prediction. "
        f"You can download the images from [here](https://www.kaggle.com/codeinstitute/cell-images-test)."
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload blood smear samples. You may select more than one.',
                                        type='png',accept_multiple_files=True)
   
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Blood Smear Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)


"""
The `page_malaria_detector_body` function defines the content and functionality
of the "Malaria Detector" page in the Streamlit app.

1. The function starts by providing some information about the purpose of the
Malaria Detector:
   - The client is interested in detecting whether a given cell contains a
     malaria parasite or not.

2. The function also informs the user that they can upload blood smear samples
for live prediction and provides a link to download the images if needed.

3. A file uploader is displayed using `st.file_uploader`, allowing the user to
upload one or more PNG images of blood smear samples.

4. If the user uploads images using the file uploader, the function proceeds to
 analyze each image:
   - It creates a DataFrame `df_report` to store the analysis results for each
     uploaded image.

5. For each uploaded image, the following steps are performed:
   - The image is displayed along with its size using `st.image`.
   - The image is resized to a format suitable for the model using the
   `resize_input_image` function.
   - The model is loaded, and the image is passed through the model for
   prediction using `load_model_and_predict`.
   - The predictions and probabilities are plotted using
   `plot_predictions_probabilities`.
   - (The functions are defined in the src folder)

6.The analysis results for each image are appended to the `df_report` DataFrame

7. After analyzing all the uploaded images, the function displays an
"Analysis Report" table using `st.table` to show the results
(image name and prediction) for each image.

8. A link to download the analysis report as a CSV file is also provided using
`st.markdown` with `unsafe_allow_html=True`. The `download_dataframe_as_csv`
function converts the DataFrame to a CSV file and generates an HTML link for
download.

Overall, the `page_malaria_detector_body` function provides a user-friendly
interface for users to upload blood smear samples and obtain live predictions
for each sample. The analysis report is presented in a table, and the user can
download the report as a CSV file for further use.
"""
