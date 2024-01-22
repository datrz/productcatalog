import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Product Catalog",
        options=["Home", "Product Catalog", "Contact"],
        icons=["house", "cart", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Home Page
if selected == "Home":
    st.title(f"{selected}")
    st.header("Welcome to our Product Catalog")
    # Image link placeholder
    image_url = ""  # Replace with your image URL
    if image_url:
        st.image(image_url, width=700)
    st.write("Explore our extensive range of products and services. Navigate through different menus to find what you're looking for.")

# Product Catalog
elif selected == "Product Catalog":
    st.title(f"{selected}")

    # Sample Data for Product Catalog
    sample_data = {
        "Picture": ["https://via.placeholder.com/100", "https://via.placeholder.com/100", "https://via.placeholder.com/100"],
        "Division": ["Electronics", "Home Appliances", "Sports"],
        "EAN Code": ["123456789", "987654321", "112233445"],
        "Description": ["Smartphone", "Microwave Oven", "Tennis Racket"],
        "Brand": ["Brand A", "Brand B", "Brand C"],
        "Order Quantity": [10, 20, 15],
        "Price": ["$299", "$159", "$89"]
    }
    df = pd.DataFrame(sample_data)

    # Filters
    division_filter = st.sidebar.selectbox("Filter by Division", ["All"] + list(df["Division"].unique()))
    brand_filter = st.sidebar.selectbox("Filter by Brand", ["All"] + list(df["Brand"].unique()))
    name_search = st.sidebar.text_input("Search in Name")

    # Filtering Data
    if division_filter != "All":
        df = df[df["Division"] == division_filter]
    if brand_filter != "All":
        df = df[df["Brand"] == brand_filter]
    if name_search:
        df = df[df["Description"].str.contains(name_search, case=False)]

    # Display Table with Images
    st.write("""
        <style>
            .dataframe img {
                max-width: 100px;
                max-height: 100px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Convert image URLs to HTML img tag
    df['Picture'] = df['Picture'].apply(lambda x: f'<img src="{x}" width="100">')

    # Display DataFrame as HTML
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)


# Contact Page
elif selected == "Contact":
    st.title(f"{selected}")
    st.header("Get in Touch")

    # Tech Support Contact
    st.subheader("Tech Support")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("Name: John Doe")
    with col2:
        st.text("Email: johndoe@example.com")
    with col3:
        st.text("Function: Tech Support Lead")

    # Product Catalog Owner Contact
    st.subheader("Product Catalog Owner")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text("Name: Jane Smith")
    with col2:
        st.text("Email: janesmith@example.com")
    with col3:
        st.text("Function: Catalog Manager")
