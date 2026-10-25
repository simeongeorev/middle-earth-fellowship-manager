from django import forms

from fellowships.models import Fellowship


class FellowshipBaseForm(forms.ModelForm):
    class Meta:
        model = Fellowship

        exclude = ['is_active']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'E.g. Fellowship of the Ring'}),
            'leader_name': forms.TextInput(attrs={'placeholder': "E.g. Aragorn"}),
            'formation_date': forms.DateInput(attrs={'type': 'date'},
                                              format='%Y-%m-%d'),
            'origin_realm': forms.TextInput(attrs={'placeholder': 'E.g. The Shire'}),
            'max_members': forms.NumberInput(attrs={'placeholder': 'E.g. 7'}),
        }

        labels = {
            'name': 'Fellowship Name',
            'leader_name': "Leader's Name",
            'formation_date': 'Formation Date',
            'origin_realm': 'Origin Realm',
            'max_members': 'Maximum Members',
        }

        help_texts = {
            'max_members': 'Must be between 2 and 12 companions.',
        }

        error_messages = {
            'name': {
                'unique': 'A fellowship with this name already exists!',
            }
        }