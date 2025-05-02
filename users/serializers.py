from rest_framework import serializers

from users.models import Payment, Users


class PaymentSerializer(serializers.ModelSerializer):
    product_type = serializers.ChoiceField(
        choices=[("course", "Course"), ("lesson", "Lesson")]
    )
    product_id = serializers.IntegerField()

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
