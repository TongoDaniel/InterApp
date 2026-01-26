from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Profile(AbstractBaseUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('cabinet_architect', 'Cabinet d\'architecture'),
        ('societe_immo', 'Société immobilière'),
    ]
    user = models.OneToOneField(AbstractBaseUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False, null=True)
    profile_photo = models.ImageField(upload_to="profile_pics",  verbose_name='Photo de profil', default='photo_profil_base.jpg')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    def save(self, *args, **kwargs):
        if self.role == 'client':
           self.is_superuser = False
           self.is_staff = False
           self.set_password(self.password)
        elif self.role == '':
           self.is_superuser = True
           self.is_staff = True
           self.set_password(self.password)
        else:
           self.is_superuser = False
           self.is_staff = True
           self.set_password(self.password)

        super().save(*args, **kwargs)