from django.shortcuts import render, get_object_or_404
from .models import Therapist,Patient,Problem,Solution


def index(request):
    total_users = Patient.objects.count()
    total_therapists = Therapist.objects.count()
    total_problems = Problem.objects.count()
    total_solutions = Solution.objects.count()

    context = {
        'total_users': total_users,
        'total_therapists': total_therapists,
        'total_problems': total_problems,
        'total_solutions': total_solutions,
    }
    return render(request, "index.html", context)




def therapist(request):
    single = Therapist.objects.all()
    context = {
        'single' : single
    }
    return render(request,"therapist.html", context)


def single_therapist(request, therapist_id):
    therapist = get_object_or_404(Therapist, therapist_id=therapist_id)
    return render(request, 'therapistSinglePage.html', {'therapist': therapist})


def user(request):
    user_data = Patient.objects.all()
    context = {
        'user_data' : user_data
    }
    return render(request,"user.html", context)

def single_user(request, patient_id):
    user = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'singleUserPage.html', {'user': user})