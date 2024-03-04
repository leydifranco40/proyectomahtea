from appMAHTEA.models.form import Form
from rest_framework import serializers
class FormSerializer(serializers.ModelSerializer):
 class Meta:
    model = Form
    fields = ['name', 'last_name', 'phone', 'birthdate', 'adress', 'occupation', 'gender', 'city']
