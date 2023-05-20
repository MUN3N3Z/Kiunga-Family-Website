from django.db import models

""" User profile details """
class Profile(models.Model):
    class Families(models.TextChoices):
        Mithika = 'Mithika', 'Mithika'
        Kinoti = 'Kinoti', 'Kinoti'
        Kalayu = 'Kalayu', 'Kalayu'
        Kanini = 'Kanini', 'Kanini'
        Kimathi = 'Kimathi', 'Kimathi'
        Karimi = 'Karimi', 'Karimi'
        Kalele = 'Kalele', 'Kalele'
        Kirito = 'Kirito', 'Kirito'
    family = models.TextField(choices=Families.choices, null=False)
    phone_number = models.IntegerField(null=True, unique=True, help_text="Example: 254700000000")
    birth_date = models.DateField(null=True, help_text="DD/MM/YYYY")

