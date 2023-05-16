from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError


# Create your models here.
class MatiCoffeeUser(AbstractUser):

    """
    AbstractUser for the page with 3 aditional fields
    * profile_img
    * friends
    * last_person_chat (Last person the user messaged with)
    
    """

    profile_img = models.ImageField(upload_to='src/profile_images', default='src/profile_images/default.png')
    friends = models.ManyToManyField('Friend', blank=True)
    last_person_chat = models.IntegerField(null=True)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='maticoffeeuser_set',
        related_query_name='maticoffeeuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='maticoffeeuser_set',
        related_query_name='maticoffeeuser'
    )

class Friend(models.Model):

    """
    Friend Model
    Is used for managing requests and the friends system.
    
    """

    user = models.ForeignKey(MatiCoffeeUser, on_delete=models.CASCADE, related_name='user')
    user_to_request = models.ForeignKey(MatiCoffeeUser, on_delete=models.CASCADE, related_name='user_to_request')
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):

        user = self.user
        user_to_request = self.user_to_request

        if user == user_to_request:
            raise ValidationError('No puedes enviarte una solicitud a vos mismo')
        
        if Friend.objects.filter(user=user, user_to_request=user_to_request).exists():
            raise ValidationError('La solicitud ya existe o ya son amigos.')
