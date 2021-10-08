from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)

#    class Meta:
# model = Post
# fields = ('id', 'author', 'text', 'created', 'updated')
