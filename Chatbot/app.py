import streamlit as st
import ollama

st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖"
)

# CSS
st.markdown("""
<style>

.stApp {
    background-color: lightblue;
}

h1 {
    color: darkblue;
    text-align: center;
}

.stTextInput label {
    color: darkblue;
    font-size: 18px;
    font-weight: bold;
}

.stTextInput input {
    background-color: white;
    color: black;
    border: 2px solid blue;
    border-radius: 10px;
}

.stButton button {
    background-color: blue;
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    font-size: 18px;
}

.stButton button:hover {
    background-color: darkblue;
}

</style>
""", unsafe_allow_html=True)


st.title("🤖 Friendly AI Bot")

st.write("Ask me anything")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):

    if question.strip():

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly and funny AI. Explain things simply."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response["message"]["content"]

        st.success("AI Response")
        st.write(answer)

    else:
        st.warning("Please enter a question.")