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
    skills = SkillSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True,required=False)
    orgs = OrganizationSerializer(many=True,required=False)

    class Meta:
        model = Applicant
        fields = '__all__'

    def create(self, validated_data):
        skills_data = validated_data.get('skills', [])
        languages_data = validated_data.get('languages', [])
        orgs_data = validated_data.get('orgs',[])

        applicant = Applicant.objects.create(**validated_data)

        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(**skill_data)
            applicant.skills.add(skill)

        for language_data in languages_data:
            language, _ = Language.objects.get_or_create(**language_data)
            applicant.languages.add(language)

        for org_data in orgs_data:
            org, _ = Organization.objects.get_or_create(**org_data)
            applicant.orgs.add(org)

        return applicant
