import streamlit as st
import openai
import os

# Configura la pagina
st.set_page_config(
    page_title="Chat con OpenAI",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="auto",
)

# Titolo dell'app
st.title("💬 Chat con OpenAI")

# Descrizione
st.write(
    "Inserisci un messaggio e interagisci con il modello di linguaggio di OpenAI."
)

# Sidebar per inserire la chiave API
st.sidebar.header("Configurazione API")
api_key = st.sidebar.text_input(
    "Inserisci la tua chiave API di OpenAI",
    type="password",
    help="La tua chiave API non sarà condivisa. Puoi ottenerne una da [OpenAI](https://platform.openai.com/account/api-keys)."
)

# Funzione per ottenere la risposta da OpenAI
def get_openai_response(prompt, api_key):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Puoi sostituire con "gpt-3.5-turbo" se preferisci
            messages=[
                {"role": "system", "content": "Sei un assistente utile."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].message['content'].strip()
        return message
    except openai.error.OpenAIError as e:
        return f"Errore: {e}"

# Campo di input per l'utente
user_input = st.text_input("Tu:", "")

# Pulsante per inviare il messaggio
if st.button("Invia") and user_input:
    if not api_key:
        st.error("Per favore, inserisci la tua chiave API di OpenAI nella sidebar.")
    else:
        with st.spinner("Generando risposta..."):
            response = get_openai_response(user_input, api_key)
            st.success("Risposta ricevuta:")
            st.write(response)
