from django.shortcuts import render
# Create your views here.
from django.views import generic
from suggestion_submission.forms import AddSuggestionForm
from braces.views import FormMessagesMixin


class AddSuggestionView(
    FormMessagesMixin,
    generic.CreateView,
):
    form_class = AddSuggestionForm
    template_name = "suggestion_submission/add_suggestion_form.html"
    form_invalid_message = "Please correct the error(s)."
    form_valid_message = "Suggestion saved. Thank you!"

    # def form_valid(self, form):
    #     raise NotImplementedError

    success_url = "/"
