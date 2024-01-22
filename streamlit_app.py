import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Main page
if selected == "Home":
    st.title(f"You Have Selected {selected}")
    st.header('Snowflake Healthcare App')
elif selected == "Projects":
    st.title(f"You Have Selected {selected}")
elif selected == "Contact":
    st.title(f"You Have Selected {selected}")
