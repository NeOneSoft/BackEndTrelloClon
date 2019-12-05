from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        try:
            """
            send_mail(
                'Asunto',
                'Pruebas Seteo SendGrid',
                'from@example.com',
                [user.email, 'gonclapton@hotmail.com'],
                fail_silently=False
            )
            """
            msg = EmailMessage(
                'Asunto',
                '<h1>Hola Mundo</h1>',
                'Gonzalo<gonzalo@gmail.com>',
                [user.email, 'gonclapton@hotmail.com']
            )
            msg.content_subtype = 'html'
            msg.send()
        except Exception as error:
            print(error)
        return user
