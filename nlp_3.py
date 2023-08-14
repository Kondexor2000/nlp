from textblob import TextBlob

text = input()

# Tworzenie obiektu TextBlob
blob = TextBlob(text)

translation = blob.translate(from_lang="pl", to="en")

# Wyświetlenie sentymentu (polarity -1 do 1, subjectivity 0 do 1)
sentiment = translation.sentiment

# Klasyfikacja sentymentu na podstawie polarity
if sentiment.polarity > 0:
    emocje = "pozytywny"
elif sentiment.polarity < 0:
    emocje = "negatywny"
else:
    emocje = "neutralny"


if emocje != "negatywny":  
    if emocje == "pozytywny":
        print("To jest miły komentarz")
    else:
        print("Komentarz nie ma nic szczególnego")
else:
    print("Tekst nie jest na miejscu!")