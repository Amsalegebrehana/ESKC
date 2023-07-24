# serializers.py
from rest_framework import serializers
from .models import Applicant, Skill, Language, Organization


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    skills = serializers.ListField( child=serializers.CharField(), required=False, write_only=True)
    languages = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)
    orgs = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)



    class Meta:
        model = Applicant
        fields = '__all__'
        # exclude = ('skills', 'languages', 'orgs')
        


    def create(self, validated_data):
        skills = validated_data.pop('skills',[])
        languages = validated_data.pop('languages',[])
        orgs = validated_data.pop('orgs',[])

        applicant = Applicant.objects.create(**validated_data)

        for skill_data in skills:
            skill, _ = Skill.objects.get_or_create(name=skill_data)
            applicant.skills.add(skill)

        for language_data in languages:
            language, _ = Language.objects.get_or_create(name=language_data)
            applicant.languages.add(language)

        for org_data in orgs:
            org, _ = Organization.objects.get_or_create(name=org_data)
            applicant.orgs.add(org)

        return applicant
    
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['skills'] = instance.skills.values_list('name', flat=True)
            return representation