import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


### Function to get response from the llama model

def getLLamaresponse(input_text, no_words, blog_style):



    #llama Model
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",model_type="llama", 
                        config={"max_new_tokens":256, "temperature":0.01})

    #Prompt Template
    template="""
        write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.    
        """   
    
    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_words'], template=template)

    #Generate the response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response
    


st.set_page_config(
    page_title="Blog Generation",
    page_icon="", 
    layout="centered", 
    initial_sidebar_state="collapsed")

st.header("Blog Generation")

input_text = st.text_input("Enter the text you want to generate a blog on") 

## Creating 2 more field
## 1. Number of words to generate
## 2. Number of blogs to generate
col_1, col_2 = st.columns([5,5])
with col_1:
    num_words = st.number_input("Enter the number of words to generate", min_value=10, max_value=1000, value=100)
with col_2:
    blog_style = st.selectbox("Select the blog style", ["researchers", "layman", "technical_audience"], index=0)

submit = st.button("Generate Blog")

if submit:
    st.write(getLLamaresponse(input_text, num_words, blog_style))