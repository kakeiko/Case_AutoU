from django import forms
from Case.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        widgets = {
            "file": forms.FileInput({'class':'input-file'}),
            "text": forms.Textarea({'class':'input-text'}),
        }

    def clean(self):
        cleaned_data = super().clean()
            
        file = cleaned_data.get('file')
        text = cleaned_data.get('text')

        if not file and not text:
            raise forms.ValidationError(
                'Você deve preencher o campo de arquivo OU o campo de texto.'
            )

        if file and text:
            self.add_error('file', 'Preencha apenas um dos campos.') 
            self.add_error('text', 'Preencha apenas um dos campos.')
                
        return cleaned_data