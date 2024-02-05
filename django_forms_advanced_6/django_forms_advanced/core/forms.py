from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import modelform_factory
from django.urls import reverse

from django_forms_advanced.core.models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        exclude = ("created_by", )

        labels = {
            "first_name": "Enter your first name:",
            "first_last": "Enter your last name:",
        }

        # It's better to do it to the client:
        # labels = {
        #     "first_name": "First Name",
        # }
        # error_messages = {
        #     "first_name": {
        #         "max_length": "The length of the name cannot exceed 30 chars!",
        #         "required": "Enter your name!",
        #     },
        # }

    def __init__(self, *args, **kwargs):
        if "user" in kwargs:
            self.user = kwargs.pop("user")

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("base_form")
        self.helper.add_input(Submit('submit', 'create'))


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance


UserFormSecond = modelform_factory(UserModel, fields="__all__")


class MixinReadOnlyFields:
    fields_readonly = ()

    def _make_fields_to_readonly(self):
        for field_name in self.fields_readonly:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"


class ExtendedUser(MixinReadOnlyFields, UserForm):
    fields_readonly = ("age", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._make_fields_to_readonly()
