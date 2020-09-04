from django.forms import ModelForm
from .models import Candidate

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name',
            'matricula', 
            'school', 
            'group',
            'email',
            'questions']
