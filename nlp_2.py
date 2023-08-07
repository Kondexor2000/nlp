import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import string
from textblob import TextBlob

# Pobieranie przykładowego tekstu (możesz też podać swój własny tekst)
nltk.download('punkt')
nltk.download('stopwords')
text = input()

# Tworzenie obiektu TextBlob
blob = TextBlob(text)

# Wyświetlenie sentymentu (polarity -1 do 1, subjectivity 0 do 1)
sentiment = blob.sentiment
print(f"Sentyment: Polarity = {sentiment.polarity:.2f}, Subjectivity = {sentiment.subjectivity:.2f}")

# Klasyfikacja sentymentu na podstawie polarity
if sentiment.polarity > 0:
    emocje = "pozytywny"
elif sentiment.polarity < 0:
    emocje = "negatywny"
else:
    emocje = "neutralny"

if emocje != "negatywny":
    # Tokenizacja tekstu na zdania i słowa
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Usuwanie znaków interpunkcyjnych i przekształcanie na małe litery
    cleaned_words = [word.lower() for word in words if word.isalnum()]

    # Usuwanie stop words (słów nieistotnych) z tekstu
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in cleaned_words if word not in stop_words]

    # Analiza częstości występowania słów
    freq_dist = FreqDist(filtered_words)

    # Wyświetlanie najczęściej występujących słów
    print("Najczęściej występujące słowa:")
    for word, frequency in freq_dist.most_common(10):
        print(f"{word}: {frequency}")
else:
    print("Tekst nie jest na miejscu!")