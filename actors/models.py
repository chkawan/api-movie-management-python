from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (

    ("BR", "Brasileiro"),
    ("US", "Americano"),
    ("CA", "Canadense"),
    ("FR", "Francês"),
    ("DE", "Alemão"),
    ("IT", "Italiano"),
    ("ES", "Espanhol"),
    ("PT", "Português"),
    ("JP", "Japonês"),
    ("CN", "Chinês"),
    ("IN", "Indiano"),
    ("RU", "Russo"),
    ("AU", "Australiano"),
    ("AR", "Argentino"),
    ("MX", "Mexicano"),
    ("GB", "Britânico"),
    ("ZA", "Sul-Africano"),
    ("KR", "Sul-Coreano"),
    ("NL", "Holandês"),
    ("CH", "Suíço")

)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
        )

    def __str__(self):
        return self.name
    
