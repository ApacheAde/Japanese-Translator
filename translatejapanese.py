# pip install googletrans==4.0.0-rc1

from googletrans import Translator

# Create an instance of the Translator class
translator = Translator()

# Prompt the user to enter text to translate
text = input("Enter text to translate: ")

# Determine the source language
detect_result = translator.detect(text)
source_lang = detect_result.lang

# Translate the text to the target language
if source_lang == 'ja':
    # If the source language is Japanese, translate to English
    target_lang = 'en'
    translation = translator.translate(text, dest=target_lang).text
    print(f"Japanese: {text}\nEnglish: {translation}")
elif source_lang == 'en':
    # If the source language is English, translate to Japanese
    target_lang = 'ja'
    translation = translator.translate(text, dest=target_lang).text
    print(f"English: {text}\nJapanese: {translation}")
else:
    print("Unsupported language")
