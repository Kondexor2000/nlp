from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Przykładowy tekst do analizy sentymentu
text = "To jest naprawdę świetny film! Bardzo polecam."

# Tworzenie obiektu TextBlob
blob = TextBlob(text)

# Wyświetlenie sentymentu (polarity -1 do 1, subjectivity 0 do 1)
sentiment = blob.sentiment

# Klasyfikacja sentymentu na podstawie polarity
if sentiment.polarity > 0:
    emocje = "pozytywny"
elif sentiment.polarity < 0:
    emocje = "negatywny"
else:
    emocje = "neutralny"

# Przykładowe dane treningowe dla klasyfikacji tekstu
corpus = [
    (text, emocje),
    ("Nie podobał mi się ten film, kompletnie nie warty czasu.", "negatywny"),
    ("Fantastyczna obsada i wciągająca fabuła.", "pozytywny"),
    ("Okropny film, nie polecam nikomu.", "negatywny")
    # Dodaj więcej przykładów
]

# Podział danych na teksty i etykiety
texts = [doc for doc, label in corpus]
labels = [label for doc, label in corpus]

# Przygotowanie cech za pomocą wektoryzacji tekstu
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Inicjalizacja modelu klasyfikacji i nauka na danych treningowych
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Predykcja na danych testowych
y_pred = clf.predict(X_test)

# Ocena dokładności modelu
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność modelu klasyfikacji tekstu: {accuracy:.2f}")