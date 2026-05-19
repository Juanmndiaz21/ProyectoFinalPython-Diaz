from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='paginas/', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paginas')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['-fecha_creacion']