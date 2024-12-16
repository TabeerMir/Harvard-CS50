'''def main():
    yell('Tabi wrote this for CS50')

def yell(phrase):
    print(phrase.upper())'''


def main():
    yell("this", "is", "CS50")

def yell(*words):
    '''uppercased = []
    for word in words:
        uppercased.append(word.upper())'''
    '''uppercased = map(str.upper, words)'''
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()