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

		exclude = ('owner', 'product', 'price', 'total')

	def save(self, commit=True):
		buy_receipt = super(BuyProductForm, self).save(commit=False)
		buy_receipt.units = self.cleaned_data['units']
		print(commit)
		if commit:
			buy_receipt.save()
			print("***************SUCCESFUL COMMIT***************")
		else:
			print("***************COMMIT FAILED***************")
		return buy_receipt
