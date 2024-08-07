from django.db import IntegrityError, models
from django.contrib.auth.models import User
from django.forms import ValidationError
from stdimage.models import StdImageField
from datetime import datetime
import uuid
import re
import requests
from django.core.validators import URLValidator
import tldextract
from django.core.validators import validate_email
from django_ckeditor_5.fields import CKEditor5Field



def len_no_ansi(string):
    y = re.sub(r'\r\n','\n', string)
    return len(y)

def add_https(value):
    if not re.match(r'^https?://', value):
        value = f'https://{value}'
    return value

def validate_link(value):
    url_pattern = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not re.match(url_pattern, value):
        raise ValidationError("O valor fornecido não é um link válido.")
    r = requests.head(value)
    try:
        r = requests.head(value)
        r.raise_for_status()

    except requests.RequestException as e:
        raise ValidationError("O link fornecido não é válido ou não está acessível: " + str(e))

def email_validation(value):
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError("O endereço de email fornecido é inválido.")
    
    
def validate_number(value):
    value_cleaned = value.replace("(", "").replace(")", "").replace("+", "")
    if value_cleaned.isdigit():
        if len(value) != 13:
            raise ValidationError("O número de telefone deve ter exatamente 13 caracteres, por favor, revise o número para garantir que não tenha digitado incorretamente.")
    else:
        raise ValidationError("O número é inválido, por favor, revise o número e garanta que contenha apenas números.")

def validate_url(value, choosed_social_media):
    value_cleaned = add_https(value)
    validate = URLValidator
    try:
        validate(value)
    except:
        raise ValidationError("A identificação fornecida não é um URL válido")

    if not any(ext in value for ext in ['.com', '.net']):
        raise ValidationError("A URL fornecida não contém um domínio completo (.com ou .net)")
    
    ext = tldextract.extract(value)
    domain = f"{ext.domain}.{ext.suffix}"
    if not domain in choosed_social_media.link:
        raise ValidationError("A URL fornecida não pertence a rede social escolhida")
    if value == "":
        raise ValidationError("A URL fornecida não pertence a rede social escolhida")
    validate_link(value_cleaned)
    return value_cleaned

def get_file_path(__instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.now()
    filename = f'{uuid.uuid4()}{now}.{ext}'
    return filename

def validate_image(image):
    limit = 2*1024*1024
    if image:
        if image.size > limit:
            raise ValidationError("O arquivo de imagem é muito largo ( Limite máximo: 4mb )")
        return image
    else:
        raise ValidationError("A imagem carregada não pode ser lida")


class SocialMedia(models.Model):
    name = models.CharField("Social Media Name", max_length=30)
    link = models.CharField("Link", max_length=200, null=True, blank=True)
    icon = models.CharField("Icon Name", max_length=30)
    is_link = models.BooleanField(default=False)

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
    description = CKEditor5Field(max_length = 1000, config_name='default', blank=True, null=True)
    photo = StdImageField('Photo', null=True, blank=True, upload_to=get_file_path, validators=[validate_image])
    qualities = models.ManyToManyField(Qualities, blank=True)
    occupation = models.ForeignKey(Occupation, related_name="professionals", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
class ProfileSocialMedia(models.Model):
    profile = models.ForeignKey(Profile, related_name="medias", on_delete=models.CASCADE, blank=False)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, blank=False)
    identification = models.CharField("Identification", max_length=3000)

    def __str__(self):
        return f"Profile Owner: {self.profile.user.first_name} / Social Media: {self.social_media.name}"

    class Meta:
        verbose_name = 'Profile Social Media'
        verbose_name_plural = 'Profile Social Medias'
    
    def clean_social_media(self):
        if self.social_media is None:
            raise ValidationError("Por favor, selecione uma rede social")
    
    def clean_identification(self):
        social_media = self.social_media
        if social_media.name == "Whatsapp":
            validate_number(self.identification)
        elif social_media.name == "Email":
            email_validation(self.identification)
        else:
            self.identification = validate_url(self.identification, self.social_media)
    
    def clean_profile(self):
        profile = self.profile
        if profile is None:
            raise ValueError("O perfil deve ser fornecido para a função clean.")
        limit = 6
        socials = profile.medias.all()
        if socials.count() >= limit:
            raise ValidationError("Você atingiu o limite(6) de redes socias que podem ser adicionadas, altere ou exclua uma rede social existente.")

        
    def clean(self):
        self.clean_profile()
        self.clean_identification()
              
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    

class Comment(models.Model):
    comment = models.TextField("Comment", max_length=1500)
    profile = models.ForeignKey(Profile, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def clean_profile(self):
        profile = self.profile
        if profile is None:
            raise ValueError("O perfil deve ser fornecido para a função clean.")
        if profile.comments.all().count() > 1:
            raise ValidationError("Você só pode adicionar um testemunho, caso queira alterar alguma coisa, edite o testemunho existente.")    
        
    def clean_comment(self):
        comment = self.comment
        comment_count = len_no_ansi(comment)
        if comment_count > 1500:
            raise ValidationError(f"O seu texto pode ter no máximo 1500 caracteres, você digitou {comment_count}")
    
    def clean(self):
        self.clean_profile()
        self.clean_comment()

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
    image = StdImageField('Photo', null=True, blank=True, upload_to=get_file_path)
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
    text = CKEditor5Field(blank=True, null=True, config_name='extends')
    description = models.TextField("Description", max_length=1000)
    link = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="projects", on_delete=models.SET_NULL, null=True, blank=True)
    technology = models.ManyToManyField(Technology)
    repository = models.URLField(blank=True, null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


