from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

#    class Meta:
# model = Post
# fields = ('id', 'author', 'text', 'created', 'updated')
