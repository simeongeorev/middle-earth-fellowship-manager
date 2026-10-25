from django import forms

from characters.models import Character


class CharacterBaseForm(forms.ModelForm):
    class Meta:
        model = Character

        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'E.g. Saruman'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/saruman.jpg'}),
            'race': forms.Select(),
            'specialization': forms.Select(),
            'combat_power': forms.NumberInput(attrs={'placeholder': '1-100'}),
            'weapon': forms.TextInput(attrs={'placeholder': 'E.g. Bow of the Galadhrim'}),
            'biography': forms.Textarea(attrs={
                'placeholder': "Describe the Hero's lore...",
                'rows': 4
            }),
            'fellowship': forms.Select(),
        }

        labels = {
            'name': 'Hero Name',
            'image_url': 'Portrait Image Link',
            'race': 'Race',
            'specialization': 'Class',
            'combat_power': 'Combat Power',
            'weapon': 'Primary Weapon',
            'biography': 'Hero Lore',
            'fellowship': 'Assigned Fellowship',
        }

        help_texts = {
            'combat_power': 'Specify a power level between 1 and 100.',
            'fellowship': 'Optional. Select a fellowship or leave empty for free agents.',
        }

class CharacterEditForm(CharacterBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['race'].disabled = True