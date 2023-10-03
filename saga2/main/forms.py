from django import forms
from .models import Story, CHOICES

class CreateNewStory(forms.Form):
    story_id = forms.ChoiceField(label='Story ID', choices=CHOICES)

    def clean_story_id(self):
        story_id = self.cleaned_data['story_id']
        return int(story_id)
