from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
from datetime import datetime
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

def get_file_path(__instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.now()
    filename = f'{uuid.uuid4()}{now}.{ext}'
    return filename

class SocialMedia(models.Model):
    name = models.CharField("Social Media Name", max_length=30)
    link = models.CharField("Link", max_length=200, null=True, blank=True)
    icon = models.CharField("Icon Name", max_length=30)

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'

    def __str__(self):
        return self.name
    
class Qualities(models.Model):
    name = models.CharField("Name of Quality", max_length=100)
    icon = models.CharField("Icon Name", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Qualitie'
        verbose_name_plural = 'Qualities'


class Occupation(models.Model):
    name = models.CharField("Name of Occupation", max_length=50)
    description = models.CharField("Description of Occupation", max_length=500)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Occupation'
        verbose_name_plural = 'Occupations'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = RichTextField()
    photo = StdImageField('Photo', null=True, blank=True, upload_to=get_file_path, variations={'thumb':{'width':480, 'height': 480, 'crop':True}})
    qualities = models.ManyToManyField(Qualities, blank=True)
    occupation = models.ForeignKey(Occupation, related_name="professionals", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class ProfileSocialMedia(models.Model):
    profile = models.ForeignKey(Profile, related_name="medias", on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    identification = models.CharField("Identification", max_length=3000)
    is_link = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile Owner: {self.profile.user.first_name} / Social Media: {self.social_media.name}"

    class Meta:
        verbose_name = 'ProfileSocialMedia'
        verbose_name_plural = 'Profile Social Medias'

class Comment(models.Model):
    comment = models.TextField("Comment", max_length=1500)
    profile = models.ForeignKey(Profile, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class TypesTechnology(models.Model):
    name = models.CharField("Name of Type", max_length=30)
    description = models.CharField("Description", max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type of Technology'
        verbose_name_plural = 'Types of Technologys'


class Category(models.Model):
    name = models.CharField("Name", max_length=30)
    description = models.TextField("Description", max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

class Technology(models.Model):
    name = models.CharField("Name", max_length=30)
    acronym = models.CharField("Acronym", max_length=10, blank=True, null=True)
    description = models.TextField("Description", max_length=1000)
    image = StdImageField('Photo', null=True, blank=True, upload_to=get_file_path, variations={'thumb':{'width':480, 'height': 480, 'crop':True}})
    percentage = models.IntegerField('Percentage', default=0)
    category = models.ForeignKey(Category, related_name="technologys", on_delete=models.SET_NULL, null=True, blank=True)
    technology_type = models.ForeignKey(TypesTechnology, related_name="technologys", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologys'

class Project(models.Model):
    name = models.CharField("Name", max_length=100)
    photo = StdImageField('Photo', null=True, blank=True, upload_to=get_file_path)
    text = RichTextUploadingField(blank=True, null=True)
    description = models.TextField("Description", max_length=1000)
    link = models.CharField("Link", null=True, blank=True, max_length=3000)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="projects", on_delete=models.SET_NULL, null=True, blank=True)
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


