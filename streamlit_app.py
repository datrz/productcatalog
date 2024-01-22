import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import base64

# Function to convert image file to base64 string
def get_base64_of_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Sidebar
with st.sidebar:
    # Country selection
    country = st.selectbox("Select your country:", ["DK", "SE", "NO", "FI"])

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
    st.write("Explore the employee shop catalog. Go to the Product Catalog menu to browse through products.")

# Product Catalog
elif selected == "Product Catalog":
    st.title(f"{selected}")

    # Define product catalog for different countries
    product_catalogs = {
        "DK": {
            "ean_codes": ["3337871311292", "3337871321994", "3337871323646", "3337871324599", "3337872410154"],
            "product_details": {
                "3337871311292": {"Division": "CPD", "Description": "Creme A", "Order Quantity": 6, "Price": "DKK 50"},
                "3337871321994": {"Division": "LDB", "Description": "Creme B", "Order Quantity": 3, "Price": "DKK 75"},
                "3337871323646": {"Division": "CPD", "Description": "Creme C", "Order Quantity": 12, "Price": "DKK 65"},
                "3337871324599": {"Division": "LDB", "Description": "Creme D", "Order Quantity": 8, "Price": "DKK 55"},
                "3337872410154": {"Division": "CPD", "Description": "Creme E", "Order Quantity": 5, "Price": "DKK 80"}
            }
        },
        "SE": {
            # Define product catalog for Sweden
            "message": "Coming soon for Sweden"
        },
        "NO": {
            # Define product catalog for Norway
            "message": "Coming soon for Norway"
        },
        "FI": {
            # Define product catalog for Finland
            "message": "Coming soon for Finland"
        }
    }

    if country in product_catalogs:
        catalog_data = product_catalogs[country]
        if "ean_codes" in catalog_data:
            ean_codes = catalog_data["ean_codes"]
            product_details = catalog_data["product_details"]

            # Prepare DataFrame
            data = []
            for ean in ean_codes:
                product_info = product_details.get(ean, {})
                picture_path = f'https://raw.githubusercontent.com/datrz/productcatalog/main/productphotos/{ean}_1.jpg'
                if os.path.exists(picture_path):
                    # Convert image to base64 string for HTML embedding
                    img_base64 = get_base64_of_image(picture_path)
                    img_html = f'<img src="data:image/jpeg;base64,{img_base64}" width="100">'
                else:
                    img_html = "<p>No Image</p>"
                data.append({
                    "Picture": picture_path,
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
        else:
            st.write(catalog_data["message"])

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
