import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_cells_visualizer_body():
    st.write("### Cells Visualizer")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a parasitised from an uninfected cell.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_parasitized = plt.imread(
            f"outputs/{version}/avg_var_Parasitized.png")
        avg_uninfected = plt.imread(
            f"outputs/{version}/avg_var_Uninfected.png")

        st.warning(
            f"* We notice the average and variability images did not show "
            f"patterns where we could intuitively differentiate one from another. "
            f"However, a small difference in the colour pigment of the average images is seen for both labels.")

        st.image(avg_parasitized,
                 caption='Parasitised Cell - Average and Variability')
        st.image(avg_uninfected,
                 caption='Uninfected Cell - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average parasitised and average uninfected cells"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"* We notice this study didn't show "
            f"patterns where we could intuitively differentiate one from another.")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/malaria_dataset/cell_images'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


"""
1. `st.write("### Cells Visualizer")`: This line displays the heading
"Cells Visualizer" on the web page.

2. `st.info(...)`: This displays an informational box with some text explaining
what the client is interested in.
It provides an overview of the purpose of the study.

3. `version = 'v1'`: A variable `version` is set to 'v1', indicating the
version of the study.

4. `st.checkbox(...)`: This line displays a checkbox on the web page with the
 label "Difference between average and variability image." If the checkbox is
 checked, the code block 
below this checkbox will be executed.

5. `avg_parasitized = plt.imread(...)` and `avg_uninfected = plt.imread(...)`:
These lines load two images, `avg_parasitized` and `avg_uninfected`, from their
respective paths.
These images represent the average and variability of parasitized and
uninfected cells. The images are read using `plt.imread()` from matplotlib.

6. `st.warning(...)`: This displays a warning box on the web page with some
information about the visualizations.

7. `st.image(...)`: These lines display the loaded images `avg_parasitized`
and `avg_uninfected` on the web page, along with their captions.

8. `st.write("---")`: This adds a horizontal rule to separate the different
sections of the page.

9. `st.checkbox(...)`: This line displays another checkbox with the label
"Differences between average parasitized and average uninfected cells."
If checked, the code block below this checkbox will be executed.

10. `diff_between_avgs = plt.imread(...)`: This line loads an image
`diff_between_avgs` from its path. This image represents the difference between
the average parasitized and average uninfected cells.

11. `st.warning(...)`: This displays another warning box on the web page with
some information about the visualization.

12. `st.image(...)`: This line displays the loaded image `diff_between_avgs`
on the web page, along with its caption.

13. `st.write("---")`: This adds a horizontal rule to separate the different
sections of the page.

14. `st.checkbox(...)`: This line displays a third checkbox with the label
"Image Montage." If checked, the code block below this checkbox will be
executed.

15. `my_data_dir = 'inputs/malaria_dataset/cell_images'`: This line sets the
variable `my_data_dir` to the directory path where the cell images are stored.

16. `labels = os.listdir(...)`: This line lists the subdirectories (labels)
within the 'validation' folder of the cell image dataset and stores them in
the `labels` variable.

17. `label_to_display = st.selectbox(...)`: This line displays a dropdown
select box on the web page, allowing the user to choose one of the available
labels (`options=labels`). The selected label will be stored in the
`label_to_display` variable.

18. `if st.button(...)`: This line displays a button on the web page labeled
"Create Montage." If the button is clicked, the code block below this line will
be executed.

19. `image_montage(...)`: This calls the `image_montage` function, which
creates a montage of cell images from the selected label and displays it on
the web page.

20. `st.write("---")`: This adds a horizontal rule to separate the different
sections of the page.

The function provides interactive elements (checkboxes, select box, and button)
that allow the user to explore and visualize different aspects of the study.
The images and text explanations are dynamically displayed based on the user's
interactions with the checkboxes and buttons.
"""


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")


"""
The `image_montage` function in the `page_cells_visualizer.py` file is re
sponsible for creating an image montage or grid display of images belonging to 
a specific label. It allows the user to visualize multiple images belonging to 
the selected label in a single grid layout.

1. `sns.set_style("white")`: This line sets the background style for the plot 
using Seaborn to "white."

2. `labels = os.listdir(dir_path)`: This line lists all the subdirectories 
(labels) present in the `dir_path` directory. Each subdirectory contains images 
of a specific label (e.g., "Parasitized" or "Uninfected").

3. `if label_to_display in labels:`: This checks if the selected label 
(`label_to_display`) exists in the list of labels available in the `dir_path` 
directory.

4. The next part of the code handles the case when the selected label exists:
   a. It checks whether the total number of images in the selected label is 
   greater than the available space in the montage (nrows * ncols). If it is, 
   a random subset of images is sampled to fit the grid display.

   b. A list of axes indices is created based on `nrows` and `ncols` using the 
   `itertools.product` function. These indices are used to position the images 
   in the grid layout.

   c. A new figure is created using `plt.subplots`, and `nrows` * `ncols` axes 
   are generated.

   d. For each image in the selected subset (`img_idx`), the image is loaded 
   using `imread`, and its shape is retrieved. The image is then displayed on 
   the corresponding axis in the grid layout using `imshow`.

   e. The title of each axis is set with the width and height of the image 
   in pixels.

   f. The x and y ticks are removed to avoid clutter.

   g. The layout of the grid is adjusted using `plt.tight_layout()` to 
   prevent overlapping.

   h. The plot is displayed using `st.pyplot(fig=fig)` to show the image
    montage in the Streamlit app.

5. If the selected label does not exist in the list of available labels, 
the function prints a message indicating that the label does not exist and 
lists the available options.

Overall, the `image_montage` function creates a grid display of images for a s
elected label, allowing the user to visualize multiple images in a single view.
"""
