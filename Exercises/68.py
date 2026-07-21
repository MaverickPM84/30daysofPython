d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate(word):
    try:
        return d[word]
    except KeyError:
        return "That word doesn't exist!"

user_input = (input("Enter the word: ")).lower()
print(translate(user_input))