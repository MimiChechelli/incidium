# 🎬 IMDB Rating Prediction

This project aims to **predict movie ratings** based on production features, cast information, and commercial performance. The goal is to develop a Python-based application using **Streamlit** as an interactive interface, allowing users to test predictions for a given movie.

## 🚀 How to Run the Application
In your terminal, open the repository in your preferred IDE and run:  

```bash
streamlit run app.py
```

## 🗂️ Data Sources

Base dataset provided by Indicium

External DB source 1: [Top Movies per Year (Base dos Dados)](https://basedosdados.org/dataset/6ba4745d-f131-4f8e-9e55-e8416199a6af?table=79de8c5e-9c21-4398-a9fb-bc40e6d6e77f&utm_source=chatgpt.com)

## 🔮 Future Work
### Additional Data Sources

- External DB source 2: [Kaggle - The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&utm_source=chatgpt.com)

### Model Enhancements

- Incorporate textual descriptions (overview, title) using NLP techniques (TF-IDF, embeddings, transformers)

- Support categorical columns such as: language, country_origin, writer, filming_location and production_company

- Future improvement: include user comments (e.g., Twitter/X) to enrich sentiment and popularity analysis

### Project Organization

- Containerize the application for pre-production or cloud testing
