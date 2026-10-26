from django import forms

from quests.models import Quest


class QuestBaseForm(forms.ModelForm):
    class Meta:
        model = Quest

        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'E.g. Take the Ring to Mordor'}),
            'region': forms.Select(),
            'threat_level': forms.Select(),
            'reward_gold': forms.NumberInput({'placeholder': '25'}),
            'assigned_fellowships': forms.CheckboxSelectMultiple(),
        }

