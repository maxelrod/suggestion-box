from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import RadioSelect

from suggestions.models import Suggestion, Recipient


class AddSuggestionForm(ModelForm):
    """Form to show a suggestion."""

    recipient = ModelChoiceField(
        Recipient.objects,
        empty_label=None,
        widget = RadioSelect,
    )

    class Meta:
        model = Suggestion
        fields = ['suggestion', 'recipient']