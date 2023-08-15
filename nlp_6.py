# Słownik tłumaczeń
translation_dict = {
    "hello": "cześć",
    "how": "jak",
    "are": "się",
    "you": "masz"
}

# Tekst do przetłumaczenia
text = input()
text_split = text.split()

if text_split in translation_dict.keys():
    

    # Funkcja tłumacząca
    def translate_text(text, translation_dict):
        words = text.split()
        translated_words = [translation_dict.get(word.lower(), word) for word in words]
        translated_text = " ".join(translated_words)
        return translated_text
    
    # Tłumaczenie tekstu
    translated_text = translate_text(text, translation_dict)
    
    print(f"Oryginalny tekst: '{text}'")
    print(f"Przetłumaczony tekst: '{translated_text}'")
else:
    print("Sorry! I speak a little Polish!")