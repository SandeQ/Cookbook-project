from django.http import HttpResponse
def user_data(request):
    ctx = {'username': request.user.username}
    return ctx
def is_logged(request):
    ctx = {'logged': "Witaj {}".format(request.user.username), 'not_logged': "Jesteś niezalogowany"}
    return ctx
def logged_in_info(request):
    if request.user.id == None:
        ctx = {'info': "Jesteś niezalogowany",
        'button1': "Zaloguj się",
        'button2': "Zarejestruj się",
        'link1': "/login",
        'link2': "/register",
        'glyph1': "glyphicon-user",
        'glyph2': "glyphicon-log-in"}


        return ctx
    else:
        ctx = {'info': 'Witaj {}'.format(request.user.username),
            'button1': "Zmień hasło",
            'button2': "Wyloguj",
            'link1': "/changepassword",
            'link2': "/logout",
            'glyph1': "glyphicon-wrench",
            'glyph2': "glyphicon-log-out"}
        return ctx
