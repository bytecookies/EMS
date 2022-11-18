from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class customUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given user_id, email, and password.
        """
        if not email:
            raise ValueError('The Email is Required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # user.password = make_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_exhibitor(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('isExhibitor', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('t_n_d', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
