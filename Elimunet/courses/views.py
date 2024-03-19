from django.shortcuts import render

def index(request):
    # Fetch courses from your database or define some context
    context = {
        # 'courses': courses,
    }
    return render(request, 'courses/index.html', context)

