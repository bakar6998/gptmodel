# GPT Model Article Summarizer

A simple Streamlit app that uses OpenAI's GPT model to summarize articles.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Get an OpenAI API key from [OpenAI](https://platform.openai.com/api-keys).

3. For local development, create a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   Or set the environment variable.

4. For Streamlit Cloud deployment, add the API key to Streamlit secrets.

## Run

```
streamlit run app.py
```

## Usage

Paste your article text into the text area and click "Summarize" to get a summary.
