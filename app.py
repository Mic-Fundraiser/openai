import streamlit as st
import openai

# Inserisci la tua chiave API di OpenAI qui
openai.api_key = "sk-5NueFBCbvf-EuxhS3fvodRgJRDQqHPJWWgbHdERGXgT3BlbkFJMatqGr2LPvzqsAzjWZgrZPFpKpPvudmSX8rqRe1s0A"

# Configura la pagina Streamlit
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

# Funzione per ottenere la risposta da OpenAI
def get_openai_response(prompt):
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
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
        message = response.choices[0].message.content.strip()
        return message
    except Exception as e: # Cattura tutte le eccezioni
        return f"Errore: {e}" # Restituisci un messaggio di errore generico

# Campo di input per l'utente
user_input = st.text_input("Tu:", "")

# Pulsante per inviare il messaggio
if st.button("Invia") and user_input:
    with st.spinner("Generando risposta..."):
        response = get_openai_response(user_input)
        st.success("Risposta ricevuta:")
        st.write(response)
