from django.forms import ModelForm
from suggestion_submission.models import Suggestion



class AddSuggestionForm(ModelForm):

    class Meta:
        model = Suggestion
        exclude = []
