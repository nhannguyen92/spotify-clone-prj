from django.db import models
from music.models import Artist, Album, Track
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  # Email duy nhất
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')  # Chỉ 'admin' và 'user'(default)

    def __str__(self):
        return self.username  

# User-Favourite-Track relationship (many-to-many)
class UserFavouriteTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_tracks')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='favourited_by_users')

    def __str__(self):
        return f"{self.user.name} likes {self.track.name}"

# User-Created Album (custom playlist-like albums)
class UserCreatedAlbum(models.Model):
    album_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_albums')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/albums/', null=True, blank=True)
    # artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.user.name}"

# User-Created Album Track relationship (many-to-many)
class UserCreatedAlbumTrack(models.Model):
    album = models.ForeignKey(UserCreatedAlbum, on_delete=models.CASCADE, related_name='tracks')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='in_user_albums')

    def __str__(self):
        return f"{self.track.name} in {self.album.name}"
