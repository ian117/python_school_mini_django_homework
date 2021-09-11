from django.shortcuts import render

from clases.models import Clase
# Create your views here.


def clases_all(request):

    if request.method == 'GET':
        all_clases = Clase.objects.all()

        contexto = {
            'clases': all_clases
        }

        return render(request, 'clases/lista.html', contexto)

    if request.method == 'POST':
        is_active = 0 if not request.POST.get('activo', False) else True

        Clase.objects.create(
        nombre=request.POST['nombre'],
        horario_begin=request.POST['horario_begin'],
        horario_end=request.POST['horario_end'],
        activo=is_active,
        )

        contexto = {
            'clases': Clase.objects.all()
        }

        return render(request, 'clases/lista.html', contexto)

def clases_by_id(request, id):
    clase = Clase.objects.get(id=id)

    contexto = {
        'clase':clase
    }

    return render(request,'clases/detalles.html', contexto)
