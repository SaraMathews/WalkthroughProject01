import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")  # You may add an icon, to personalize your App
        # check links below for additional icons reference
        # https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
        # https://twemoji.maxcdn.com/2/test/preview.html

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()


"""
The `multipage.py` file contains a class called `MultiPage`, which is designed
to help generate multiple pages for a Streamlit web application in an
object-oriented manner. 

2. `class MultiPage:`: This line defines a new class called `MultiPage`.

3. `def __init__(self, app_name) -> None:`: This is the constructor method for
the `MultiPage` class. It is executed when an object of the class is created.
The constructor takes an argument `app_name`, which will be used as the title
of the web application.

4. `self.pages = []`: This line initializes an empty list called `pages`.
This list will store the different pages of the web application.

5. `self.app_name = app_name`: This line assigns the `app_name` argument to the
`app_name` attribute of the class. This attribute will store the title of the
web application.

6. `st.set_page_config(...)`: This line sets the configuration for the web
application. It specifies the page title (`page_title`) as the `app_name`,
and it sets an icon (`page_icon`) to personalize the web application.
In this case, the icon is set to "🖥️", representing a computer screen.
Streamlit supports various emoji icons for personalization.

7. `def add_page(self, title, func) -> None:`: This is a method that allows
adding new pages to the web application. It takes two arguments: `title`,
which is the title of the page, and `func`, which is the function that will be
executed when the page is selected.

8. `self.pages.append({"title": title, "function": func})`: This line adds a
new dictionary to the `pages` list. The dictionary contains two key-value pairs:
"title" with the value of the `title` argument and "function" with the value of
the `func` argument. This dictionary represents a single page of the web
application.

9. `def run(self):`: This is a method that runs the web application.

10. `st.title(self.app_name)`: This line displays the title of the web
application using the `app_name` attribute.

11. `page = st.sidebar.radio(...)`: This line creates a radio button in the
sidebar of the web application. The options for the radio button are the titles
of the pages stored in the `pages` list. The selected page's dictionary is
stored in the `page` variable.

12. `page['function']()`: This line calls the function associated with the
selected page. It executes the function and displays the content of that page
on the main part of the web application.

The `MultiPage` class allows you to organize and create multiple pages for your
Streamlit web application easily. By using this class, you can build a more
structured and organized web application with different pages for different
functionalities. Each page's content is defined in separate functions,
and the user can navigate between the pages using the sidebar radio buttons.
"""
