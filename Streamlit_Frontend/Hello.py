import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Eat Healthy")

st.sidebar.success("Use this nav bar to navigate through the website.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, Flask and Streamlit.
    """
)
