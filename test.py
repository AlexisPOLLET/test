import pandas as pd
import streamlit as st
import plotly.express as px

# Titre de l'application
st.title("Analyse des Séismes en France")

# Étape 1 : Téléchargement du fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV contenant les données des séismes", type=["csv"])

if uploaded_file:
    # Lecture du fichier CSV
    try:
        data = pd.read_csv(uploaded_file)
        st.success("Fichier chargé avec succès !")

        # Aperçu des données
        st.subheader("Aperçu des données :")
        st.write(data.head())

        # Vérification des colonnes nécessaires
        if 'latitude' in data.columns and 'longitude' in data.columns and 'significance' in data.columns:
            # Étape 2 : Filtrer les séismes par niveau de significance
            st.subheader("Analyse des Séismes par Niveau de Significance")

            low_significance = data[data['significance'] < 50]
            medium_significance = data[(data['significance'] >= 50) & (data['significance'] < 150)]
            high_significance = data[data['significance'] >= 150]

            st.write(f"Nombre de séismes de faible significance : {len(low_significance)}")
            st.write(f"Nombre de séismes de moyenne significance : {len(medium_significance)}")
            st.write(f"Nombre de séismes de forte significance : {len(high_significance)}")

            # Étape 3 : Créer une carte interactive avec Plotly
            st.subheader("Carte Interactive des Séismes")
            fig_map = px.scatter_mapbox(
                data,
                lat="latitude",
                lon="longitude",
                color="significance",  # Couleur selon la significance
                size="significance",  # Taille des points selon la significance
                hover_name="significance",
                title="Carte des Séismes en France",
                zoom=5,
                mapbox_style="carto-positron"
            )
            st.plotly_chart(fig_map)
        else:
            st.error("Les colonnes nécessaires 'latitude', 'longitude' et 'significance' sont absentes du fichier.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")

