from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_skills(self):
        return self.skills.all()

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_skills(self):
        return self.skills.all()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    candidates = models.ManyToManyField(Candidate, through='CandidateSkill', related_name='skills')
    features = models.ManyToManyField(Feature, through='FeatureSkill', related_name='skills')

    def __str__(self):
        return self.name

    def get_candidates(self):
        return self.candidates.all()

    def get_features(self):
        return self.features.all()

class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate.name} - {self.skill.name}"

class FeatureSkill(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.feature.name} - {self.skill.name}"
