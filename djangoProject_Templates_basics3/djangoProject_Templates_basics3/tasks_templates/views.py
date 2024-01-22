from datetime import date

from django.shortcuts import render


class Women:
    def __init__(self, first_name, last_name, born, age, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.born = born
        self.age = age
        self.country = country


def index(request):

    context = {
        "1title": "Info for some actors!",
        "today": date.today(),
        "char_list": ["v", "e", "s", "i"],
        "numbers_list": [335, 22, 1, 904, 56],
        "empty_list": [],
        "navigation": ["About", "Services", "Contacts"],
        "params": request.GET,

        "actor": {
            "first_name": "Tom",
            "last_name": "Hanks",
            "born": "9 July, 1956",
            "age": 67,
            "country": "USA",
        },

        "actress_object": Women(
            "Scarlett",
            "Johansson",
            "22 November, 1984",
            39,
        ),

    }

    return render(request, "tasks_templates/index.html", context)


def menu_index(request, option):
    context = {
        "option": option,
    }

    return render(request, "tasks_templates/menu.html", context)

