import streamlit as st
from openai import OpenAI

st.title("Article Summarizer with GPT")

# Note: Set your OpenAI API key in Streamlit secrets or environment variable
# For local development, create a .env file with OPENAI_API_KEY=your_key
# and run with streamlit run app.py

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY") or st.text_input("Enter your OpenAI API Key", type="password"))

article = st.text_area("Paste the article text here", height=300)

if st.button("Summarize"):
    if article.strip():
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes articles."},
                    {"role": "user", "content": f"Please summarize the following article:\n\n{article}"}
                ],
                max_tokens=200,
                temperature=0.5
            )
            summary = response.choices[0].message.content.strip()
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some article text.")