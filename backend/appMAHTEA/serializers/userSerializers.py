from rest_framework import serializers
from appMAHTEA.models.user import User
from appMAHTEA.models.form import Form
from appMAHTEA.serializers.formSerializers import FormSerializer


class UserSerializer(serializers.ModelSerializer):
    form = FormSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'form']

    def create(self, validated_data):
        formData = validated_data.pop('form')
        userInstance = User.objects.create(**validated_data)
        Form.objects.create(user=userInstance, **formData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        form = Form.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'password': user.password,
                    'email':user.email,
                    'form': {
                        'name': form.name,
                        'last_name':form.last_name,
                        'phone': form.phone,
                        'birthdate': form.birthdate,
                        'adress': form.adress,
                        'occupation': form.occupation,
                        'gender': form.gender,
                        'city': form.city,
                    }
                }