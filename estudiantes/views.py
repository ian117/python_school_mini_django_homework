from django.shortcuts import render

from estudiantes.models import Estudiante
# Create your views here.


def estudiantes_all(request):

    if request.method == 'GET':
        all_Estudents = Estudiante.objects.all()

        contexto = {
            'estudiantes': all_Estudents
        }

        return render(request, 'estudiantes/lista.html', contexto)

    if request.method == 'POST':
        is_active = 0 if not request.POST.get('activo', False) else True

        Estudiante.objects.create(
        nombre=request.POST['nombre'],
        correo=request.POST['correo'],
        telefono=request.POST['telefono'],
        edad=request.POST['edad'],
        activo=is_active,
        )

        contexto = {
            'estudiantes': Estudiante.objects.all()
        }

        return render(request, 'estudiantes/lista.html', contexto)

def estudiantes_by_id(request,id):
    estudiante = Estudiante.objects.get(id=id)

    contexto = {
        'estudiante':estudiante
    }

    return render(request,'estudiantes/detalles.html', contexto)
