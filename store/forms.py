from django import forms
from store.models import Product


class Notes(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ["name",
              "semester",
               "Teacher",
               "price",
               "department",
               "phone_number",
            #    "fileupload",
               "category",
               "Description",
               "image",
            #    "is_Available",

        ]
       
       
        widgets = {
             'name' : forms.TextInput(attrs={'class':'form-control',  }),
             'Teacher' : forms.TextInput(attrs={'class':'form-control',}),
             'price' : forms.NumberInput(attrs={'class':'form-control', }),
             'semester' : forms.Select(attrs={'class':'form-control',}),
            'department' : forms.TextInput(attrs={'class':'form-control', }),
            'phone_number' : forms.TextInput(attrs={'class':'form-control',}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'Description' : forms.Textarea(attrs={'class':'form-control',}),
         

        }





class FreeNotes(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ["name",
              "semester",
               "Teacher",
            #    "price",
               "department",
               "phone_number",
               "fileupload",
               "category",
               "Description",
               "image",
            #    "is_Available",

        ]
       
       
        widgets = {
             'name' : forms.TextInput(attrs={'class':'form-control',  }),
             'Teacher' : forms.TextInput(attrs={'class':'form-control',}),
            #  'price' : forms.NumberInput(attrs={'class':'form-control', }),
             'semester' : forms.Select(attrs={'class':'form-control',}),
            'department' : forms.TextInput(attrs={'class':'form-control', }),
             'phone_number' : forms.TextInput(attrs={'class':'form-control',}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'Description' : forms.Textarea(attrs={'class':'form-control',}),

        }
