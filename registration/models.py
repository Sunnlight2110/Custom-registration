from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class ProjectManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)
    
class StudentModel(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = ProjectManager()

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """ Hash password before saving it """
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """ Check password with stored hashed password """
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)


