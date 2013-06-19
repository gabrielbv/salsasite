from django import forms



class PurchaseCode(forms.Form):
	
	code = forms.CharField()

