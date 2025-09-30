from django.db import models
from django.core.validators import FileExtensionValidator

class Email(models.Model):
    file = models.FileField(upload_to='documentos/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt'])], null=True, blank=True)
    text = models.TextField(null=True, blank=True)

class Resultado(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    classificacao = models.TextField(null=False, blank=False)
    resposta = models.TextField(null=False, blank=False)
