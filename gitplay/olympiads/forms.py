from django import forms
from .models import ExerciseType



class ExerciseTypeForm(forms.ModelForm):

    class Meta:
        model = ExerciseType
        fields = [
            'type'
        ]

        labels = {
            'type': 'Add a new exercise type'
        }