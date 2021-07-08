from django.db.models.expressions import F
from django.db import models
from .category import Category
from django.db.models.deletion import CASCADE
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from .customer import Customer

STATUS = (
    (1,"1"),
    (2,"2"),
	(3,"3"),
    (4,"4"),
	(5,"5"),
    (6,"6"),
	(7,"7"),
	(8,"8"),
)

class Product(models.Model):
	name = models.CharField(max_length=220)
	student = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True )
	semester = models.IntegerField(choices=	STATUS,default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])
	Teacher = models.CharField(max_length=100,null=True,default='Sir zain')
	price = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100000)])
	department = models.CharField(max_length=100,default='CS@IT',null=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
	Description = models.TextField(null=True,)
	image = models.ImageField(upload_to='upload/products')
	fileupload = models.FileField(upload_to='upload/products',null= True,blank=True)
	phone_number = models.CharField(max_length=13,null=True,default="Number")
	is_Available = models.BooleanField(null=True,)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	# All Product get
	@staticmethod
	def getAllProduct():
		return Product.objects.all()

	# Filter Product By Category
	@staticmethod
	def getProductByFilter(category_id):
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.getAllProduct()

	@staticmethod
	def getProductById(productList):
		return Product.objects.filter(id__in=productList)

	def get_absolute_url(self):
          return reverse('store:home', kwargs={"pk": self.pk})
		

	