# visualizer.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from app.data_handler import load_data
from app.matrix_generator import generate_threat_asset_matrix

def main():
    st.title("Threat-Asset Analysis Tool")

    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV/JSON file", type=["csv", "json"])

    if uploaded_file is not None:
        try:
            # Step 1: Load data
            st.subheader("Input Data")
            data = load_data(uploaded_file)
            st.write(data)

            # Step 2: Generate Threat-Asset Matrix
            st.subheader("Threat-Asset Matrix")
            matrix = generate_threat_asset_matrix(data)
            st.write(matrix)

            # Step 3: Display Heatmap
            st.subheader("Heatmap Visualization")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=ax)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
