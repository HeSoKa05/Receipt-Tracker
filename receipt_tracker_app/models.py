from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ReceiptModel(models.Model):
    """
    Receipt model has main fields: store name, item list, total amount, purchase date as it required.
    I added additional ones like description, and slug fields.
    the slug field used for replacing spaces in the store_name with dashes, like this: store-full-name,
    that is to be used in urls to make them readable and have meaning.
    """

    store_name = models.CharField(max_length=250, null=False, blank=False) # store names should be filled.
    description= models.TextField() # descriptions are optional to be filled.
    item_list = models.TextField(blank=False) # at least one item should be added.
    total_amount = models.IntegerField(default=0)
    purchase_date = models.DateTimeField(auto_now=False, auto_now_add=True) # to set the date of purchase.

    # I used Django built-in model to make it as simple as can
    # each user can view, and manage their own receipt
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # returning the store name to be shown in the admin panel.
    def __str__(self):
        return self.store_name

    def get_absolute_url(self):
        return reverse('receipt_detail', kwargs={'pk': self.pk})
