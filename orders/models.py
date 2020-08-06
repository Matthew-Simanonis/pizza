from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Placed_Order(models.Model):
    discount = models.DecimalField(max_digits=12,decimal_places=2, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.customer_id.username

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Menu_Item(models.Model):
    item_name = models.TextField()
    price = models.DecimalField(max_digits=12,decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=12,decimal_places=2, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    active = models.BooleanField()
    slug = models.SlugField(default='')

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        value = self.item_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', kwargs={
            'slug': self.slug
        })

    def change_quantity_url(self):
        return reverse('change-quantity', kwargs={
            'slug': self.slug
        })


class Order_Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Menu_Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.item_name}'

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Order_Item)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False )

    def __str__(self):
        return self.user.username

