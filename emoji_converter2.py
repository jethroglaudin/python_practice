def emoji_convertor(sentence):
    emojis = {
        ":)": "😀",
        ":(": "☹️",
        ":'(": "😢",
        ":|": "😐",
        ":p": "😜"

    }
    output = ""

    words = sentence.split(" ")
    for word in words:
        output += emojis.get(word, word) + " "

    return output


sentence = input('>')
print(emoji_convertor(sentence))


