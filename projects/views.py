from django.shortcuts import render

from projects.models import Project


def all_projects(request):
    projects = Project.objects.all()

    return render(request, 'projects/all_projects.html', 
                  {'projects': projects})


def project_list(request):
    return render(request, 'projects/index.html')


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render (request, 'projects/detail.html', {'project': project})
