from django import forms
from django.contrib.auth.models import User
from shop.models import BuyReceipt

class BuyProductForm(forms.ModelForm):
	class Meta:
		model = BuyReceipt
		fields = (
			'owner',
			'product',
			'price',
			'units',
			'total',
			'cc_num',
            )
		labels = {
			'cc_num': 'Credit Card Number'
			}

		exclude = ('owner', 'product', 'price', 'total')

	def save(self, commit=True):
		buy_receipt = super(BuyProductForm, self).save(commit=False)
		buy_receipt.units = self.cleaned_data['units']
		
		if commit:
			buy_receipt.save()

		return buy_receipt
