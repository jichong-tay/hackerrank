def loud(text):
    print(text.upper())


def quiet(text):
    print(text.lower())


def hello(func):
    func


hello(loud("Hello"))
