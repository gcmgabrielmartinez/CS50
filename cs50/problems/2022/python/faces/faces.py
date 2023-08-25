def main():
    sentence = input()
    c_sentence = convert(sentence)
    print(c_sentence)

def convert(s):

    s2 = s.replace(":)", "🙂").replace(":(", "🙁")
    return s2

main()