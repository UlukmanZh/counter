from django.shortcuts import render, redirect
def index (request):
    if 'counter' in request.session:
        print('key exists!')
        request.session ['counter'] += 1 
    else:
        print("key 'counter' does NOT exist")
        request.session ['counter'] = 1
    
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')

def double (request):
    request.session ['counter'] += 2
    return render(request, 'index.html')


