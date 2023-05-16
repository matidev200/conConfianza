from django.db import models
from django.db.models import Q
from apps.user.models import MatiCoffeeUser

class ThreadManager(models.Manager):

    """
    ThreadManager for search the msgs from a user

    input:
    request.user or user.name
    
    return:
    queryset
    """

    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):

    """
    Thread model for save the conversation between two users.
    """

    first_person = models.ForeignKey(MatiCoffeeUser, on_delete=models.CASCADE, null=True, blank= True, related_name='thread_first_person')
    second_person = models.ForeignKey(MatiCoffeeUser, on_delete=models.CASCADE, null=True, blank= True, related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    class Meta:
        unique_together = ['first_person', 'second_person']

class ChatMessage(models.Model):

    """
    Model for save the msgs from request.user with their
    respective thread.
    """
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(MatiCoffeeUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)