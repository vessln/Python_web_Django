from django import forms

from django_forms_basics.demoapp.models import Client


class DemoClientForm(forms.Form):
    FRUITS = (
            (1, "strawberry"),
            (2, "banana"),
            (3, "peach"),
            (4, "apple"),
        )

    first_name = forms.CharField(
        max_length=20,
        required=True,
    )

    age = forms.IntegerField(
        required=True,
    )

    description = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "placeholder": "What is your favorite fruit? Why ?"
            }
        )
    )

    fav_fruit = forms.ChoiceField(
        label="Favorite fruit:",
        choices=FRUITS,
    )

    fav_fruit2 = forms.IntegerField(
        label="Favorite fruit:",
        widget=forms.Select(choices=FRUITS),
    )

    is_vegan = forms.BooleanField(
        label="Are you vegan?",
    )


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = "__all__"  # get all fields from Client model
        # exclude = ("age",) -> without "age"

        # labels
        # help_texts
        # error_messages
        # widgets

        labels = {
            "first_name": "First Name:",
        }

        widgets = {
            "gender": forms.RadioSelect,
        }


