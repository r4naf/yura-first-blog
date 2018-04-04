from django.db import models
from django.utils import timezone

"""
c:\Python\mydjango\dj1\Scripts\activate.bat
cd c:\Python\mydjango\dj1\yurasite\
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py runserver
"""

class Keyword(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text="Напишите кто редактор",verbose_name="Редактор")
    title = models.CharField(default='', max_length=250, help_text="Обязательно укажите название",verbose_name="Название")
    text = models.TextField(verbose_name="Описание")
    field7 = models.CharField(default='', max_length=210,verbose_name="Примечание")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Дата создания")
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="Дата публикации")
    myBooleanField = models.BooleanField(default=True,verbose_name="Книга на русском")
    myDateField = models.DateField(default=timezone.now, blank=True,verbose_name="Просто дата")
    myDecimalField = models.DecimalField(default=10, decimal_places=2, max_digits=10,verbose_name="Вес в кг")
    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    BOSS = 'BO'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
		(BOSS, 'Yuraz'),
    )
    mySelectCharField = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=BOSS,verbose_name="Рецензент")
									
    myEmailField1 = models.EmailField(default='', blank=True,verbose_name="Почта 1")
    myEmailField2 = models.EmailField(default='mail@mail.ru',verbose_name="Почта 2")
    myIPAddressField = models.GenericIPAddressField(default='', null=True, blank=True)
    myURLField = models.URLField(default='', null=True, blank=True)
    myImageField = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/no-img.jpg', null=True, blank=True,verbose_name="Картинка")
	
    keywords = models.ManyToManyField(Keyword, blank=True)
	
    def is_upperclass(self):
        return self.mySelectCharField in (self.JUNIOR, self.SENIOR)
									  
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
