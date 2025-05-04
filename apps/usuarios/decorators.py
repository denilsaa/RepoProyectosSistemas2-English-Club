from django.shortcuts import redirect

def solo_directivo(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('rol') != 'directivo':
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
