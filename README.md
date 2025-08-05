# 📦 Automatización Aduanera con IA

Una aplicación web desarrollada con **Streamlit** que utiliza **procesamiento de lenguaje natural (NLP)** y **machine learning** para:

- Leer descripciones de productos desde facturas
- Predecir su **código arancelario (HS Code)**
- Automatizar parte del proceso de documentación aduanal

---

## 🚀 Cómo funciona

1. El usuario ingresa o carga la descripción del producto.
2. La app utiliza un modelo entrenado de clasificación (Random Forest / XGBoost / etc.).
3. Se realiza una predicción del código HS más probable.
4. El resultado se muestra en pantalla.

---

## 🧠 Tecnologías usadas

- `Python`
- `scikit-learn`
- `joblib`
- `pandas`, `numpy`
- `Streamlit`
- `TfidfVectorizer` para vectorización del texto

---

## 📂 Archivos clave

| Archivo                | Descripción                                 |
|------------------------|---------------------------------------------|
| `app.py`               | Código principal de la app Streamlit        |
| `modelo_hs.pkl`        | Modelo entrenado de clasificación           |
| `vectorizer_hs.pkl`    | Vectorizador de texto (TF-IDF)              |
| `requirements.txt`     | Dependencias necesarias                     |

---

## 💻 Cómo correr localmente

```bash
git clone https://github.com/tu_usuario/automatizacion-aduanera-con-ia.git
cd automatizacion-aduanera-con-ia
pip install -r requirements.txt
streamlit run app.py
