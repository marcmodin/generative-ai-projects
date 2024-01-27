import streamlit as st
from bedrock import CallBedrockChain, CallRenderPrompt, SampleQuestions

def answer(question):
    assistant = st.chat_message("assistant")
    output = CallBedrockChain(question)
    # output = "I don't know the answer to that question."
    assistant.write(output.answer)


st.title('The Middleman Project')

st.subheader('A simple AI application based on Langchain and using LLM models from AWS Bedrock.')

st.markdown(""":blue[Middleman] was an idea we had at work. The idea was to have an AI that could act as a middleman between a user and a support team. To help in triaging issues and to help the user get the right support.""")

st.sidebar.markdown(""" When a question come in via Slack, the AI would ask the user for more information if it feels like the question is not detailed enough. However the AI should never try to answer the question itself since it's only a *middleman* :sunglasses:\n""")

st.sidebar.divider()

expander = st.sidebar.expander("Example questions")

# create a radio button with the sample questions as options
selected_question = expander.radio(
    "Here are some example questions for you to test out:",
    [val for i, val in enumerate(SampleQuestions.values()) if i < 3],
)

question = st.text_area('label', selected_question, label_visibility="hidden")

# create two columns for the buttons
col1, col2 = st.columns([9,2])

# alternate way to disable button when clicked
def disable_button(a,b):
    st.session_state["disabled_a"] = a
    st.session_state["disabled_b"] = b

with col1:
    # when button is clicked, disable it and enable the other button
    submitted = st.button('Submit', on_click=disable_button, args=(True, False), disabled=st.session_state.get("disabled_a", False))
with col2:
    # when button is clicked, disable it and enable the other button
    clear = st.button('Clear Results', on_click=disable_button, args=(False, True), disabled=st.session_state.get("disabled_b", True))

# create an empty placeholder so it can be filled later
placeholder = st.empty()

with placeholder.container():
    
    if submitted:
        human = st.chat_message("human")
        human.write(question)
        with st.spinner('Thinking...'):
            answer(question)

    # when clear button is pressed clear the results
    if clear:
        #  empty everything inside the container
        placeholder.empty()
