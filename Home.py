import streamlit as st

"""
Home.py — main entry for the Streamlit multipage app.
This file displays a title, welcome text, and a button that navigates to the pages/app.py page.
"""

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Welcome to the World Cities app")
st.write("Hello! This is the Home page. Use the button below to open the app page (pages/app.py).")

if st.button("Open app.py"):
    # Set the `page` query parameter so Streamlit navigates to the page named "app" (pages/app.py)
    st.experimental_set_query_params(page="app")
    # Rerun so the navigation takes effect immediately
    st.experimental_rerun()

st.write("You can also switch pages using the sidebar pages menu.")
