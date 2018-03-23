from django import forms
from django.contrib.auth.models import User
from shop.models import BuyReceipt

class BuyProductForm(forms.ModelForm):
	class Meta:
		model = BuyReceipt
		fields = (
    		'user',
    		'units',
            'price',
            'title',
            'cc_num',
            )

		exclude = ('user', 'title', 'price')

	def save(self, commit=True):
		buy_receipt = super(BuyProductForm, self).save(commit=False)
		buy_receipt.units = self.cleaned_data['units']
	
		if commit:
			buy_receipt.save()
	
		return buy_receipt
