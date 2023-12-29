import streamlit as st
from newspaper import Article
from googletrans import Translator
import nltk

# Download 'punkt' tokenizer if not already downloaded
nltk.download('punkt', quiet=True)

# Set NLTK data path to ensure access to the 'punkt' tokenizer
nltk.data.path.append("/path/to/your/nltk_data")

# Function to extract and display article details
def extract_article_details(article_url, target_language):
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()
    translator = Translator()
    
    st.header("Article Details")
    
    # Display complete text
    st.subheader("Complete Text")
    st.write(article.text)

    # Display keywords
    st.subheader("Keywords")
    st.write(", ".join(article.keywords))

    # Display article summary
    st.header("Article Summary")
    st.subheader(article.title)
    st.write(article.summary)

    # Translate content if a target language is selected
    if target_language != "Original" and target_language is not None:
        if article.text:  # Check if the article text is not empty or None
            translated_title = translator.translate(article.title, dest=target_language).text
            translated_text = translator.translate(article.text, dest=target_language).text
            translated_summary = translator.translate(article.summary, dest=target_language).text

            st.header(f"Translated Content ({target_language})")
            st.subheader("Translated Title")
            st.write(translated_title)
            
            st.subheader("Translated Text")
            st.write(translated_text)
            
            st.subheader("Translated Summary")
            st.write(translated_summary)
        else:
            st.warning("No text available for translation.")
    else:
        st.info("Select a target language to translate.")

# Streamlit app
def main():
    st.title("Article Translator")

    # Input for article link and language selection
    article_link = st.text_input("Enter the article link:")
    target_language = st.selectbox("Select Target Language", ["Original", "Spanish", "French", "German", "Italian", "Urdu"])

    if st.button("Translate"):
        if article_link:
            try:
                extract_article_details(article_link, target_language)
            except Exception as e:
                st.error(f"Error: Unable to analyze the article. Please check the link. Exception: {e}")
                st.exception(e)
    	
if __name__ == "__main__":
    main()
