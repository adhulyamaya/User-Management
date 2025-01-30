import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from main.models import BaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin): #Centralized table for all user-related information
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=15, blank=True, null=True)  

    main_admin = models.ForeignKey('MainAdmin', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'custom_users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        constraints = [
            models.UniqueConstraint(fields=['username', 'main_admin'], name='unique_username_per_main_admin')
        ]

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        if CustomUser.objects.filter(username=self.username, main_admin=self.main_admin).exclude(pk=self.pk).exists():
            raise ValidationError("A user with this username already exists within this MainAdmin.")

    def save(self, *args, **kwargs):
        self.clean()
        super(CustomUser, self).save(*args, **kwargs)

      
class MainAdmin(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    username = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='main_admin_images', null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='admin_mic', null=True, blank=True)

    class Meta:
        db_table = 'main_admins'
        verbose_name = 'Main Admin'
        verbose_name_plural = 'Main Admins'
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    
class Staff(BaseModel): 
    company = models.ForeignKey(MainAdmin, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company_admin_profile')
    class Meta:
        db_table = 'staffs'
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        ordering = ('-date_added',)
        

    def __str__(self):
        return self.full_name
    
# class CompanyAdmin(BaseModel):
    # company = models.ForeignKey(MainAdmin, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # address = models.TextField()
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # is_active = models.BooleanField(default=True)
    # is_deleted = models.BooleanField(default=False)

    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company_admin_profile')
    # class Meta:
    #     db_table = 'company_admins'
    #     verbose_name = 'Company Admin'
    #     verbose_name_plural = 'Company Admins'

    # def __str__(self):
    #     return self.name

