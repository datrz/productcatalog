import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Product Catalog",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Main page
if selected == "Home":
    st.title(f"{selected}")
    st.header('Snowflake Healthcare App')
elif selected == "Projects":
    st.title(f"{selected}")
elif selected == "Contact":
    st.title(f"{selected}")
