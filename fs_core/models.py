from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid

from io import BytesIO
from PIL import Image

from django.core.files import File


AGE = (
    ('all', 'All'),
    ('kid', 'Kid'),
)

MOVIE_TYPE = (
    ('series', 'Series'),
    ('single', 'Single'),
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female')
)


class User(AbstractUser):
    """
    user account
    user can have multiple profiles (for each family member)
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'

    #uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    # True if user are blocked
    is_locked = models.BooleanField(default=False)
    
    date_of_birth = models.DateField(blank=True, null=True, default=None)
    city = models.CharField(max_length=250, blank=True, null=True, default=None)
    region = models.CharField(max_length=200, blank=True, null=True, default=None)
    profiles = models.ManyToManyField("Profile", blank=True)
    
    def create_user(self, username, email, password, first_name=None, last_name=None):
        """
        create and save a user with given email and password
        """
        if not username:
            raise ValueError('username required for Users')
        if not password:
            raise ValueError('password required for Users')
        if not email:
            raise ValueError('email address required for Users')
        
        user = self.model(
            username = username,
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        
        group, _ = Group.objects.get_or_create(name="Common")
        user.groups.add(group)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    
class Profile(models.Model):
    """profile details"""
    
    
    profile_name = models.CharField(max_length=50)
    age_restriction = models.CharField(choices=AGE, max_length=10, default='Kids')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    slug = models.SlugField()
    
    # profile avatar picture
    #avatar = models.ImageField(upload_to='', default='', blank=True, null=True)
    
    def __str__(self):
        return self.profile_name
    
    def get_absolute_url(self):
        return f'/{self.user.slug}/{self.slug}/'
    
    
    
class Movie(models.Model):
    """the Movie"""
    
    GENRE = (
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('fiction', 'Fiction'),
        ('romance', 'Romance'),
        ('documentary', 'Documentary'),
        ('animation', 'Animation'),
        ('fantasy', 'Fantasy'),
        ('sports', 'Sports'),
        ('spirituality', 'Spirituality')
    )
    
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    movie_type = models.CharField(choices=MOVIE_TYPE, max_length=50)
    genre = models.CharField(choices=GENRE, max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/thumbnail/', blank=True, null=True)
    videos = models.ManyToManyField("Video")
    age_restriction = models.CharField(choices=AGE, max_length=10)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return ('http://127.0.0.1:8000' + self.image.url)
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return ('http://127.0.0.1:8000' + self.thumbnail.url)
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return ('http://127.0.0.1:8000' + self.thumbnail.url)
            return ''
        
    def make_thumbnail(self, image, size=(300, 200)):
        """create thumbnail from image"""
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100, subsampling=0)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
    
    def get_video(self):
        if self.videos:
            return [video.get_video() for video in self.videos.all()]
        return ''
        
    
    
class Video(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title
    
    def get_video(self):
        if self.file:
            return ('http://127.0.0.1:8000' + self.file.url)
        return ''
