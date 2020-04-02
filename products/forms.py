from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ]

class RawproductForm(forms.Form):
    title = forms.CharField(label = '', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField( 
                        required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "my-id": "my-id-for-textarea",
                                "row": 20,
                                "cols":120
                            }
                        ))
    price = forms.DecimalField()