# ! pip install openai
# ! pip install openai streamlit transformers

import openai

# OpenAI API key
openai.api_key = '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'

# Define a function to get the chatbot response from OpenAI API
def get_chatbot_response(prompt_text, model="gpt-3.5-turbo", max_tokens=100):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt_text,
            max_tokens=max_tokens  # Corrected argument name
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return str(e)

# Example prompt text
prompt_text = "You are a helpful chatbot assisting a new mother with postpartum care. The user asks:"

# Get the chatbot response
chatbot_response = get_chatbot_response(prompt_text)

# Display the chatbot response
print("Chatbot Response:")
print(chatbot_response)

# Different prompt types to try out
prompt_types = [
    "open-ended",
    "instruction",
    "multiple choice",
    "fill in the blank",
    "binary",
    "ordering",
    "prediction",
    "explanation",
    "opinion",
    "scenario",
    "comparative"
]

# Loop through each prompt type and get chatbot responses
for prompt_type in prompt_types:
    complete_prompt = prompt_text + f" '{prompt_type}':"
    chatbot_response = get_chatbot_response(complete_prompt)
    print(f"{prompt_type.capitalize()} Prompt:")
    print(chatbot_response)
    print("=" * 50)

    
import streamlit as st

# Define a function to get the chatbot response from OpenAI API
# (Same function as in the previous script)

# Create Streamlit app
def main():
    st.title("Postpartum Care Chatbot")
    st.markdown("Greetings! I am a ChatBot programmed to provide you with the information that you require.")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Ask"):
        chatbot_response = get_chatbot_response(f"You are a helpful chatbot assisting a new mother with postpartum care. The user asks: '{user_input}'")
        st.text("Chatbot:")
        st.text(chatbot_response)

if __name__ == "__main__":
    main()