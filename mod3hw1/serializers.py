from rest_framework import serializers
from .models import Tasks
from django.contrib.auth import get_user_model
#from drf_extra_fields.fields import Base64ImageField

# class NonModelSerializer(serializers.Serializer):
#     """Сериализатор с не-модельными полями."""


# class CommentSerializer(serializers.ModelSerializer):
#     """Сериализатор для модели Comment."""
#
#     class Meta:
#         model = Comment
#         # fields = "__all__"
#         exclude = ("author", "to_article",)


class TasksSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Tasks."""

    # article_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # article_comments = CommentSerializer(many=True)
    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    # is_active = serializers.SerializerMethodField('get_task_status')
    #
    # def get_task_status(self, obj):
    #     return not obj.done

    # image = Base64ImageField()

    class Meta:
        model = Tasks
        # read_only_fields = ["id", "slug", "created", "modified"]
        # fields = read_only_fields + ["title"]
        fields = "__all__"
        
        
        # fields = "__all__"
        # fields = ("id", "title", "content", "author")
        # exclude = []
        # fields = ("id", "title", "content", "article_comments", "author", "read_only_field", "slug", "image", "created", "modified", )

    # def validate_title(self, value):
    #     if value != value.capitalize():
    #         raise serializers.ValidationError("Название должно быть с заглавной буквы")
    #     return value

    # def to_internal_value(self, data):
    #     # if self.context["request"]._request.method == "POST":
    #     #     # if not data.get("title"):
    #     #     #     data["title"] = "default_title"
    #     #     if not data.get("content"):
    #     #         data["content"] = "default_content"
    #     # if not data.get("title"):
    #     # data["name"] = data["name"] + "  23"
    #     # data["done"] = True
    #     return super().to_internal_value(data)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["is_active"] = not instance.done
    #     #representation["_request_data_method"] = self.context["request"]._request.method
    #     # representation["_request_data_url"] = self.context["request"]._request.path
    #     return representation
    #
    # def create(self, validated_data):
    #     if not validated_data.get("author"):
    #         User = get_user_model()
    #         validated_data["author"] = User.objects.first()
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    # #     User = get_user_model()
    # #     author = User.objects.first()
    # #     new_comment = Comment(to_article=instance, author=author, coment="Изменено")
    # #     new_comment.save()
    #     validated_data["name"] = validated_data["name"] + "  111"
    #     validated_data["done"] = not self.initial_data["is_active"]
    #     return super().update(instance, validated_data)