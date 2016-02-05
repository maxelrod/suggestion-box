from django.views import generic
from braces.views import FormMessagesMixin

from .models import Suggestion
from .forms import AddSuggestionForm


class AddSuggestionView(FormMessagesMixin,
                        generic.CreateView):
    """View to show and process form."""

    form_class = AddSuggestionForm
    template_name = "suggestions/add_suggestion_form.html"
    form_invalid_message = "Please correct the error(s)."
    form_valid_message = "Suggestion saved. Thank you!"
    success_url = "/"
