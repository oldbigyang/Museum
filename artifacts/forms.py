from django import forms
from .models import Artifact

class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = '__all__'  # 或者可以指定特定字段

