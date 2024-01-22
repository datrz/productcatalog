import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import base64

# Function to convert image file to data URI
def get_image_data_uri(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded_string}"

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
    image_url = "header_loreal.png"  # Replace with your image URL
    if image_url:
        st.image(image_url, width=700)
    st.write("Explore our extensive range of products and services. Navigate through different menus to find what you're looking for.")

# Product Catalog
elif selected == "Product Catalog":
    st.title(f"{selected}")

    # EAN codes and product details
    ean_codes = ["3337871311292", "3337871321994", "3337871323646", "3337871324599", "3337872410154"]
    product_details = {
        "3337871311292": {"Division": "CPD", "Description": "Creme A", "Order Quantity": 6, "Price": "DKK 50"},
        "3337871321994": {"Division": "LDB", "Description": "Creme B", "Order Quantity": 3, "Price": "DKK 75"},
        "3337871323646": {"Division": "CPD", "Description": "Creme C", "Order Quantity": 12, "Price": "DKK 65"},
        "3337871324599": {"Division": "LDB", "Description": "Creme D", "Order Quantity": 8, "Price": "DKK 55"},
        "3337872410154": {"Division": "CPD", "Description": "Creme E", "Order Quantity": 5, "Price": "DKK 80"}
    }

    # Prepare DataFrame
    data = []
    for ean in ean_codes:
        product_info = product_details.get(ean, {})
        picture_path = f'productphoto/{ean}_1.jpg'
        if os.path.exists(picture_path):
            image_data_uri = get_image_data_uri(picture_path)
            image_html = f'<img src="{image_data_uri}" width="100">'
        else:
            image_html = "No Image"
        data.append({
            "Picture": image_html,
            "Division": product_info.get("Division", "Unknown"),
            "EAN Code": ean,
            "Description": product_info.get("Description", "Unknown"),
            "Order Quantity": product_info.get("Order Quantity", 0),
            "Price": product_info.get("Price", "DKK 0")
        })
    df = pd.DataFrame(data)

    # Filters
    division_filter = st.sidebar.selectbox("Filter by Division", ["All"] + list(df["Division"].unique()))
    name_search = st.sidebar.text_input("Search in Name", key="name_search")

    # Filtering Data
    if division_filter != "All":
        df = df[df["Division"] == division_filter]
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

    # Convert image paths to HTML img tag
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
