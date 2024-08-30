import streamlit as st
import streamlit_app  # Import the main app script
import feedback_page  # Import the feedback page script

PAGES = {
    "Main Page": streamlit_app.main,
    "Feedback Page": feedback_page.feedback_page
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()