from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def blank(request):
    template_name = 'blank.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)


def email(request):
    template_name = 'email.html'
    return render(request, template_name)


def compose(request):
    template_name = 'compose.html'
    return render(request, template_name)


def calendar(request):
    template_name = 'calendar.html'
    return render(request, template_name)


def chat(request):
    template_name = 'chat.html'
    return render(request, template_name)


def charts(request):
    template_name = 'charts.html'
    return render(request, template_name)


def forms(request):
    template_name = 'forms.html'
    return render(request, template_name)


def ui(request):
    template_name = 'ui.html'
    return render(request, template_name)


def basic_table(request):
    template_name = 'basic-table.html'
    return render(request, template_name)


def datatable(request):
    template_name = 'datatable.html'
    return render(request, template_name)


def google_maps(request):
    template_name = 'google-maps.html'
    return render(request, template_name)


def vector_maps(request):
    template_name = 'vector-maps.html'
    return render(request, template_name)


def p404(request):
    template_name = '404.html'
    return render(request, template_name)


def p500(request):
    template_name = '500.html'
    return render(request, template_name)


def signin(request):
    template_name = 'signin.html'
    return render(request, template_name)


def signup(request):
    template_name = 'signup.html'
    return render(request, template_name)


def buttons(request):
    template_name = 'buttons.html'
    return render(request, template_name)
