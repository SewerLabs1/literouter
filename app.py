import openai
import litellm
import streamlit as st

st.title("🎆MythoMist 7B")

openai.api_base = "https://openrouter.ai/api/v1/chat/completions"
openai.api_key = "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"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gryphe/mythomist-7b"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("🪅"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
