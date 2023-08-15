# Prosty przykład projektu generowania odpowiedzi w czacie

# Lista zapytań i możliwych odpowiedzi
questions = ["Jak się masz?", "Co robisz?", "Jaka jest pogoda?", "Czym się interesujesz?"]
answers = ["Dobrze, a Ty?", "Programuję.", "Chyba będzie padać.", "Interesuję się astronomią."]

# Funkcja generująca odpowiedź
def generate_response(input_text):
    response = "Przepraszam, nie rozumiem."
    for i in range(len(questions)):
        if questions[i] in input_text:
            response = answers[i]
            break
    return response

# Pętla czatu
print("Witaj! Możemy porozmawiać.")
print("")
print("Pytania do dyspozycji")
print("")
for i in questions:
    print(i)
print("")

print("Jeżeli chcesz wyłączyć program, napisz koniec.")

while True:
    user_input = input("Ty: ")
    if user_input.lower() == "koniec":
        print("Do widzenia!")
        break
    response = generate_response(user_input)
    print("Bot:", response)