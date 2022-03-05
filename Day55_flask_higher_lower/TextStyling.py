def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"

    return wrapper_function


def make_em(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper

class TextStyling:
    def __init__(self):
        pass
