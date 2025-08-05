📦 Automatización Aduanera con IA
Este proyecto es un MVP funcional que utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) e inteligencia artificial para automatizar la clasificación arancelaria de productos y generar documentación aduanera de forma eficiente y precisa.

🚨 Problema que resuelve
En el comercio internacional, clasificar productos con su código arancelario (HS Code) correcto y generar documentación aduanera adecuada puede ser un proceso:

- Lento y manual
- Propenso a errores humanos
- Costoso en términos de tiempo y recursos

✅ Solución propuesta
Esta app web permite:

- Ingresar la descripción de un producto.
- Clasificar automáticamente el producto en su HS Code (código arancelario).
- Generar un resumen aduanal con el código, categoría y país destino.
- Estimar el costo aduanal con base en reglas definidas por país.

Todo esto utilizando:

- 🧠 Modelos de NLP con TF-IDF y MultinomialNB
- 📂 Un modelo entrenado previamente y guardado en formato .pkl
- 🖥️ Una interfaz simple y funcional en Streamlit

🛠️ Cómo se construyó (Arquitectura del Proyecto)

1. Generación del dataset simulado con descripciones de productos y sus respectivos códigos HS.
2. Vectorización del texto con TfidfVectorizer.
3. Entrenamiento de un modelo de clasificación con MultinomialNB.
4. Evaluación del modelo con métricas de precisión, recall y f1-score.
5. Serialización del modelo y vectorizador (joblib.dump()).
6. Construcción de la interfaz web con Streamlit.
7. Implementación en la nube con Streamlit Cloud.

📂 Estructura del proyecto

├── app.py                      # Código principal de la app en Streamlit
├── modelo_hs.pkl              # Modelo de clasificación entrenado
├── vectorizer_hs.pkl          # Vectorizador TF-IDF entrenado
├── README.md                  # Este archivo

🚀 Cómo usar la app

1. Ve a la app desplegada en Streamlit 👉 [Demo en Streamlit]((https://automatizacion-aduanera-con-ia.streamlit.app/))
2. Ingresa una descripción detallada del producto.
3. Selecciona el país de destino.
4. Haz clic en Clasificar producto.
5. Obtén el HS Code estimado, categoría y costo aproximado de aduana.

📌 Tecnologías utilizadas

- Python 3.11
- Scikit-learn
- Pandas
- Joblib
- Streamlit
- NLP con TF-IDF

🧠 Ejemplos de uso

| Descripción del producto            | Código HS estimado | País destino | Costo estimado |
| ----------------------------------- | ------------------ | ------------ | -------------- |
| Chocolate orgánico oscuro 70% cacao | 180631             | Alemania     | \$102.50       |
| Camiseta de algodón talla M         | 610910             | México       | \$85.00        |
| Teléfono inteligente con 128GB      | 851712             | Brasil       | \$180.00       |

🧪 Posibles mejoras futuras

- Conexión con API oficial de aduanas (ej. SAT, Aduana Argentina, CBP USA).
- Incorporación de validación automática de documentos PDF de facturas.
- Entrenamiento del modelo con datasets reales por país.
- Módulo de autenticación para agentes de comercio exterior.

👤 Autor
Asairi Nava – [LinkedIn](https://www.linkedin.com/in/asairi-nava/)
Proyecto parte de una serie de soluciones impulsadas por IA para comercio electrónico y logística.
