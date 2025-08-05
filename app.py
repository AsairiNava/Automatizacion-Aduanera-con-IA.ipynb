import streamlit as st
import joblib
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Clasificación Arancelaria con IA", layout="centered")

# Título
st.title("📦 Clasificador Arancelario Automatizado")
st.markdown("Este sistema usa inteligencia artificial para predecir el **código arancelario (HS Code)** a partir de la descripción del producto.")

# Cargar modelo y vectorizador
try:
    modelo = joblib.load("modelo_hs.pkl")
    vectorizador = joblib.load("vectorizer_hs.pkl")
except Exception as e:
    st.error(f"❌ Error al cargar el modelo o vectorizador: {e}")
    st.stop()

# Entrada de texto del usuario
descripcion_input = st.text_area("📝 Ingresa la descripción del producto a clasificar", height=150)

# Botón para predecir
if st.button("📌 Predecir código arancelario") and descripcion_input.strip():
    try:
        # Vectorizar texto
        descripcion_vectorizada = vectorizador.transform([descripcion_input])

        # Predecir código
        prediccion = modelo.predict(descripcion_vectorizada)[0]

        # Mostrar resultado
        st.success(f"🔢 Código Arancelario Predicho: **{prediccion}**")

        # Crear DataFrame para mostrar y descargar
        resultado_df = pd.DataFrame({
            "Descripción del Producto": [descripcion_input],
            "Código Arancelario (HS)": [prediccion]
        })

        st.dataframe(resultado_df)

        # Botón para descargar resultado
        csv = resultado_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Descargar resultado en CSV",
            data=csv,
            file_name="clasificacion_arancelaria.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"⚠️ Error durante la predicción: {e}")
elif descripcion_input.strip() == "":
    st.info("✍️ Ingresa una descripción para comenzar.")
