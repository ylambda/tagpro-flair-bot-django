from django.contrib.auth.models import AbstractUser
from social.storage.django_orm import DjangoUserMixin


class TagProUser(DjangoUserMixin, AbstractUser):
    pass