from django.contrib import admin
from .models import Candidate, Skill, Feature, CandidateSkill, FeatureSkill

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CandidateSkill)
class CandidateSkillAdmin(admin.ModelAdmin):
    list_display = ('candidate','skill')

@admin.register(FeatureSkill)
class FeatureSkillAdmin(admin.ModelAdmin):
    list_display = ('feature','skill')
