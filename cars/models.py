from django.db import models
from django.urls import reverse

# Create your models here.

COLOR_TRANSPORT = (
    ('White','oq'),
    ('Black','qora'),
    ('Blue','kok'),
    ('other','Boshqa'),
    )
CONDITION_TRANSPORT = (
    ('Yangi','Yangi'),
    ('Eski','Eski'),
    ('Ortacha','Ortacha'),
    ('Ishlatip olsa boladi','Ishlatip olsa boladi'),
    ('Vashee Zor','Vashee Zor'),
)

class CategoryTransport(models.Model):
    title = models.CharField(max_length = 150)
    keywords = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length = 150)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})
    
    

class Transport(models.Model):

    brand = models.CharField("brand nomi: ",max_length = 150)
    model = models.CharField(max_length = 150)
    color = models.CharField("Rangi: ",max_length = 150, choices=COLOR_TRANSPORT)
    bodyType = models.CharField("Kuzov turi",max_length = 150, blank=True)
    transmission = models.CharField("Uzatmalar qutisi", max_length = 150, blank=True)
    condition = models.CharField("Avtomobil holati", max_length = 150, choices=CONDITION_TRANSPORT)
    year = models.IntegerField("Ishlap shiqarilgan yili: ", default=1800)
    mileage = models.CharField("Yurgan masofasi",max_length = 150)
    price = models.IntegerField("Narxi: ",)
    description = models.TextField("Qoshimcha malumot",max_length = 500, blank=True, help_text="Metan bor bir bola..")
    slug = models.SlugField(max_length = 150, unique=True)
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(CategoryTransport, on_delete=models.CASCADE, verbose_name="Transport Turi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('transport_detail', kwargs={'slug': self.slug})
    