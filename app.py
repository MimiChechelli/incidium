import streamlit as st
import pickle
import pandas as pd

def get_user_input():
    st.sidebar.header("Insira os dados do filme:")

    # Campos básicos
    title = st.sidebar.text_input("Title", value='The Shawshank Redemption')
    released_year = st.sidebar.number_input("Released Year", min_value=1920, max_value=2020, value=1994)
    
    certificate_options = ['Restricted (17+)',
                           'Parental Guidance Suggested', 
                           'General Audience (All Ages)',
                            'Unrated / Not Classified',
                           'Parents Strongly Cautioned (13+)']
    certificate = st.sidebar.selectbox("Certificate", certificate_options)
    
    runtime = st.sidebar.number_input("Runtime (min)", min_value=45, max_value=321, value=142)
    overview = st.sidebar.text_area("Overview", value='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.')
    
    meta_score = st.sidebar.number_input("Meta Score", min_value=28, max_value=100, value=80)
    director = st.sidebar.text_input("Director", value='Frank Darabont')
    star1 = st.sidebar.text_input("Star 1", value='Tim Robbins')
    star2 = st.sidebar.text_input("Star 2", value='Morgan Freeman')
    star3 = st.sidebar.text_input("Star 3", value='Bob Gunton')
    star4 = st.sidebar.text_input("Star 4", value='William Sadler')
    
    no_of_votes = st.sidebar.number_input("Number of Votes", min_value=25088, max_value=2343110, value=2343110)
    gross = st.sidebar.number_input("Absolute Gross", min_value=1305, max_value=936662225, value=28341469)
    writer = st.sidebar.text_input("Writer")
    country_origin = st.sidebar.text_input("Country of Origin")
    filming_location = st.sidebar.text_input("Filming Location")
    production_company = st.sidebar.text_input("Production Company")
    
    # Oscar checkbox
    st.sidebar.write("Did the movie win an Oscar?")
    oscar = st.sidebar.checkbox("Yes")
    
    # Idiomas (checkboxes)
    st.sidebar.write("Select the languages the movie is translated to:")
    idiomas = ["English", "French", "Spanish", "German", "Italian", "Russian", "Hindi",
            "Latin", "Japanese", "Arabic", "Cantonese", "Mandarin", "Swedish"]
    idiomas_selecionados = [idioma for idioma in idiomas if st.sidebar.checkbox(idioma)]

    # Transforma em string única
    idiomas_str = ", ".join(idiomas_selecionados) if idiomas_selecionados else "None"
    
    # Gêneros (checkboxes)
    st.sidebar.write("Select the genres of the movie:")
    generos = ["Drama", "Comedy", "Thriller", "Adventure", "Action", "Crime", "Romance",
            "Biography", "Mystery", "Period Drama", "Fantasy", "Family", "SciFi",
            "Animation", "Tragedy", "Sci-Fi", "Psychological Drama", "War",
            "History", "Dark Comedy", "Epic", "Docudrama"]
    generos_selecionados = [genero for genero in generos if st.sidebar.checkbox(genero)]

    # Transforma em string única
    generos_str = ", ".join(generos_selecionados) if generos_selecionados else "None"


    # Criar DataFrame com os inputs do usuário
    dados_usuario = pd.DataFrame([{
        'title': title,
        'Released_Year': released_year,
        'Certificate': certificate,
        'Runtime': runtime,
        'Overview': overview,
        'Meta_score': meta_score,
        'Director': director,
        'Star1': star1,
        'Star2': star2,
        'Star3': star3,
        'Star4': star4,
        'No_of_Votes': no_of_votes,
        'Gross': gross,
        'writer': writer,
        'country_origin': country_origin,
        'filming_location': filming_location,
        'production_company': production_company,
        'oscar': int(oscar),
        'Idiomas': idiomas_str,
        'Generos': generos_str
    }])

    return dados_usuario

def main():
    st.title("IMDB Rating Prediction App")
    st.write("Use the sidebar to input movie details and predict its IMDB rating.")

    # Obter inputs do usuário
    dados_usuario = get_user_input()
    
    st.subheader("Movie data you entered:")
    st.write(dados_usuario)


    # Botão de previsão
    if st.sidebar.button("Prever Rating"):
        # Carregar modelo
        with open("xgboost_best_model.pkl", "rb") as f:
            modelo_carregado = pickle.load(f)
        
        # Previsão
        pred = modelo_carregado.predict(dados_usuario)[0]
        st.write(f"Rating previsto: {pred:.2f}")
    st.markdown("---")

if __name__ == "__main__":
    main() # Chama o app Streamlit
