'''def peace_translate(phrase):
    translation = ""
    vowel = ["a", "e", "i", "o", "u"]
    for letter in phrase:
        for element in vowel:
            if phrase[letter] != vowel[element]:
                translation = phrase[letter]
            else:
                phrase[letter] = "g"
                translation = phrase[letter]
    return translation

print(translate(input("Enter a phrase: ")))'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))