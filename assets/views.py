from django.shortcuts import render



# Main Dashboard page
def home(request):
    template_name = 'home.html'
    context = {
        'Hello': 'Hello, World!'
    }

    return render(request, template_name, context=context)