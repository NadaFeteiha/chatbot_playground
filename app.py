import streamlit as st
from groq import Groq


# Initialize the Groq API client
client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

if "llm" not in st.session_state:
    st.session_state["llm"] = ""

# store the chat messages i
if "messages" not in st.session_state:
    st.session_state["messages"] = []

print("Session state: ", st.session_state)

#Page Header
st.header("Hello World Nada!", divider="orange", anchor=False)
st.title(":orange[Chat App]", anchor=False)
st.subheader("This is a simple chat app built with Streamlit")

#Sidebar
st.sidebar.title("Parameters")
