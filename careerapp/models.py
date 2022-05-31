from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser  # ghi dè lớp
from django.db import models
from django.utils.html import mark_safe

from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField("image")
    phone = models.CharField(max_length=12, null=True, default=None)
    ADMIN, CANDIDATE = range(2)
    USER = [
        (ADMIN, 'admin'),
        (CANDIDATE, 'candidate'),
    ]
    user_role = models.CharField(
        max_length=10,
        choices=USER,
        default=CANDIDATE
    )
    is_active = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ['-id']


class ModelBase(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_date']

    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Candidate(ModelBase):
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=150, null=True)
    cv = models.FileField(upload_to='uploads/CV/%Y/%m', null=True)
    degree = models.CharField(max_length=150, null=True)
    skill = models.CharField(max_length=150, null=True)
    experience = models.CharField(max_length=150, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class CandidateSkill(ModelBase):
    description = models.CharField(max_length=100, unique=True)
class CandidateBenefit(models.Model):

class Employer(models.Model):
    class Meta:
        unique_together = ('name', 'address')

    title = models.CharField(max_length=100, null=True)
    location = models.ManyToManyField('Location', related_name="employer", blank=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    info_employer = RichTextField(null=True)
    logo = models.ImageField("image", blank=True)
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', related_name="employer", blank=True)
    category = models.ForeignKey('Category', related_name="employer", on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']


class Location(models.Model):
    name = models.CharField(max_length=100)


# Model many to one upload nhiều ảnh
class EmployerImage(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='employer/activity/%Y/%m')

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<img src="https://res.cloudinary.com/dgct8zpvp/%s" width="150" height="150" />' % self.image)
        else:
            return mark_safe('<========== Chọn ảnh để upload')

    image_tag.short_description = 'Image'


class Post(ModelBase):
    position = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=100, null=True)
    salaryMax = models.CharField(max_length=100, null=True)
    salaryMin = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    hide_begin = models.DateField(max_length=100, null=True)
    hide_end = models.DateField(max_length=100, null=True)
    description = RichTextField(null=True)
    benefit = models.ManyToManyField('Tag', related_name="post", blank=True)
    level = models.CharField(max_length=100, null=True)
    requirement = RichTextField(null=True)
    category = models.ForeignKey(Category, related_name="post", on_delete=models.SET_NULL, null=True)
    employers = models.ForeignKey('Employer', related_name="post", on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name="post", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_date']


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ("employer", "creator")


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class Recruitment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_on = models.models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "candidate")


class PostView(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
