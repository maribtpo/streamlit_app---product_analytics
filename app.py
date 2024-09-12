import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# Set up LangChain
template = """
You are a helpful assistant for answering questions about product analytics.
User: {user_input}
Assistant:"""

prompt = PromptTemplate(input_variables=["user_input"], template=template)
llm = OpenAI(temperature=0.9)  # OpenAI model with temperature for control

# Function to get a response from the LangChain
def get_response(user_input):
    formatted_prompt = prompt.format(user_input=user_input)
    response = llm.generate([formatted_prompt])  # Pass the prompt as a list
    # Access the generated text from the LLMResult object
    return response.generations[0][0].text.strip()

# Streamlit app UI
st.title("Product Analytics Chatbot")

# Create input field for user query
user_input = st.text_input("Ask me anything about product analytics:")

# Create a submit button
if st.button("Submit"):
    if user_input:
        # Get the response from LangChain
        response = get_response(user_input)
        # Display the chatbot's response
        st.write(f"Assistant: {response}")
    else:
        st.write("Please enter a question.")