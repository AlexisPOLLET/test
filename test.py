import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Incorporer et Visualiser un Document Excel")

# Étape 1 : Téléchargement du fichier Excel
uploaded_file = st.file_uploader("Téléchargez un fichier Excel ici :", type=["xlsx", "xls", "scv"])

if uploaded_file:
    # Étape 2 : Lecture du fichier Excel
    try:
        data = pd.read_excel(uploaded_file, engine="openpyxl")  # Utilise 'openpyxl' pour .xlsx
        st.success("Fichier chargé avec succès !")
        
        # Étape 3 : Aperçu des données
        st.subheader("Aperçu des données :")
        st.write(data.head())

        # Étape 4 : Statistiques descriptives
        st.subheader("Statistiques descriptives :")
        st.write(data.describe())

        # Étape 5 : Visualisation optionnelle
        st.subheader("Graphique interactif :")
        selected_column = st.selectbox("Choisissez une colonne pour visualiser :", data.columns)
        if selected_column:
            st.line_chart(data[selected_column])
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
