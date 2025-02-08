from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from test_app.models import Candidate, Feature, Skill, CandidateSkill, FeatureSkill


def table_view(request):

    # pass all data to populate the table
    candidates = Candidate.objects.all()
    features = Feature.objects.all()
    skills = Skill.objects.all()

    context = {
        'candidates': candidates,
        'features': features,
        'skills': skills,
    }

    return render(request, 'relationships.html', context)


def candidate_skills_view(request, candidate_id):

    # Retrieve the Candidate object by its ID
    candidate = get_object_or_404(Candidate, id=candidate_id)

    # Get the related Skill objects
    skills = candidate.get_skills()
    
    # Pass the candidate to frontend
    skills_data = [{'id': skill.id, 'name': skill.name} for skill in skills if skill]

    return JsonResponse({'skills': skills_data})


def feature_skills_view(request, feature_id):
    # Retrieve the Candidate object by its ID
    features = get_object_or_404(Feature, id=feature_id)
    
    # Get the related Skill objects
    skills = features.get_skills()

    # Pass the candidate to frontend
    skills_data = [{'id': skill.id, 'name': skill.name} for skill in skills if skill]
    
    return JsonResponse({'skills': skills_data})



def skill_detail_view(request, skill_id):
    
    # Retrieve the Skill object by its ID
    skill = get_object_or_404(Skill, id=skill_id)
    
    # Get the related Candidate and Feature objects
    candidates = skill.get_candidates()
    features = skill.get_features()

    candidate_data = [{'id': candidate.id, 'name': candidate.name} for candidate in candidates if candidate]
    feature_data = [{'id': feature.id, 'name': feature.name} for feature in features if feature]

    return JsonResponse(
        {
            'candidate_data': candidate_data, 
            'feature_data': feature_data
        }
    )
