from rest_framework import serializers
from api.models import LBBase
import json


class LBBaseSerializer(serializers.ModelSerializer):
    struct = serializers.SerializerMethodField('clean_json') 
    class Meta:
        model = LBBase
        fields = ('struct',)

    def clean_json(self, obj):
        return json.loads(obj.struct)
