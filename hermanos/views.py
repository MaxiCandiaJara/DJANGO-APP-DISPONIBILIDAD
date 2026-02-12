from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gestion.models import Hermano
import json
import os


mesSiguiente = ""


# ===== AUTENTICACIÓN =====

def login_view(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'login.html')


def logout_view(request):
    """Cierra la sesión del usuario"""
    logout(request)
    return redirect('login')


# ===== VISTAS PRINCIPALES =====

@login_required
def index(request):
    return render(request, "base.html")


@login_required
def listarHermanos(request):
    hermanos = Hermano.objects.all()
    return render(request, "listarHermanos.html", {'hermanos': hermanos})


@login_required
def buscar(request):
    return render(request, "buscarHermano.html")


@login_required
def editar(request):
    nombre = request.POST["nombre"].lower()
    try:
        hermano = Hermano.objects.get(nombre__iexact=nombre)
    except Hermano.DoesNotExist:
        return render(request, "editar.html", {'error': "Hermano no encontrado"})

    dias_guardados = hermano.manana_list
    tardes_guardados = hermano.tarde_list

    return render(request, "editar.html", {
        'Hermano': hermano,
        'dias_guardados': dias_guardados,
        'tardes_guardados': tardes_guardados
    })


@login_required
def editarHermano(request):
    nombre = request.POST["nombre"]
    manana = request.POST.getlist("dias")
    tarde = request.POST.getlist("tardes")
    comentario = request.POST["comentario"]

    try:
        hermano = Hermano.objects.get(nombre=nombre)
    except Hermano.DoesNotExist:
        return buscar(request)

    hermano.set_mananas(manana)
    hermano.set_tardes(tarde)
    hermano.comentario = comentario
    hermano.save()

    return buscar(request)


@login_required
def elegirMes(request):
    return render(request, "elegirMes.html")


def cargarMensajes(mes):
    hermanos = Hermano.objects.all()
    mensaje = []

    todos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    for h in hermanos:
        manana_list = h.manana_list
        tarde_list = h.tarde_list

        # Revisamos la mañana
        if not manana_list:
            mananas_texto = "no podía"
        elif manana_list == todos:
            mananas_texto = "podía todos los dias"
        else:
            mananas_texto = "podía los " + ", ".join(manana_list)

        # Revisamos la tarde
        if not tarde_list:
            tardes_texto = "no podía"
        elif tarde_list == todos:
            tardes_texto = "podía todas las tardes"
        else:
            tardes_texto = "podía los " + ", ".join(tarde_list)

        texto = (
            f"Hola, estamos confirmando su disponibilidad para el mes de {mes}. "
            f"Usted nos dijo que {mananas_texto} en las mañanas, "
            f"y que {tardes_texto} en las tardes. "
            "Confirmar si mantendrá esta disponibilidad o la cambiará. "
            "De antemano se le agradece su buena disposición. "
            "*Si no responde a este mensaje vamos a asumir que la mantiene.*"
        )

        mensaje.append({
            "Nombre": h.nombre,
            "Texto": texto,
            "Numero": h.numero
        })

    return mensaje


@login_required
def mensajes(request):
    global mesSiguiente
    mesSiguiente = request.POST["mes"]
    mensaje = cargarMensajes(mesSiguiente)
    return render(request, "mensajes.html", {'mensaje': mensaje})


@login_required
def agregarHermano(request):
    return render(request, "agregarHermano.html")


@login_required
def agregar(request):
    nombre = request.POST["nombre"]
    manana = request.POST.getlist("dias")
    tarde = request.POST.getlist("tardes")
    comentario = request.POST["comentario"]

    # Verificar si ya existe
    if Hermano.objects.filter(nombre__iexact=nombre).exists():
        return render(request, "agregarHermano.html", {
            'mensaje_error': f"El hermano '{nombre}' ya existe."
        })

    hermano = Hermano(nombre=nombre, comentario=comentario)
    hermano.set_mananas(manana)
    hermano.set_tardes(tarde)
    hermano.save()

    return render(request, "agregarHermano.html", {'mensaje': "Hermano agregado exitosamente"})


@login_required
def eliminarHermano(request):
    """Elimina un hermano de la base de datos"""
    if request.method == 'POST':
        hermano_id = request.POST.get('hermano_id')
        try:
            hermano = Hermano.objects.get(id=hermano_id)
            nombre = hermano.nombre
            hermano.delete()
            return render(request, "buscarHermano.html", {
                'mensaje': f"Hermano '{nombre}' eliminado correctamente."
            })
        except Hermano.DoesNotExist:
            return render(request, "buscarHermano.html", {
                'error': "Hermano no encontrado."
            })
    return redirect('buscar')


@login_required
def wspMensaje(request):
    try:
        import pywhatkit
        numero = request.POST["Numero"]
        texto = request.POST["Texto"]
        pywhatkit.sendwhatmsg_instantly(numero, texto)
        mensaje = cargarMensajes(mesSiguiente)
        return render(request, "mensajes.html", {'texto': "Enviado por wsp!", "mensaje": mensaje})
    except ImportError:
        mensaje = cargarMensajes(mesSiguiente)
        return render(request, "mensajes.html", {
            'texto': "Error: pywhatkit no está instalado en el servidor.",
            "mensaje": mensaje
        })


# ===== HOJA DE CÁLCULO / DISPONIBILIDAD =====

@login_required
def hojaCalculo(request):
    """Vista de hoja de cálculo con filtros por día y turno"""
    hermanos = Hermano.objects.all()

    # Obtener filtros desde GET
    filtro_dia = request.GET.get('dia', '')
    filtro_turno = request.GET.get('turno', '')

    # Aplicar filtros
    if filtro_dia and filtro_turno:
        if filtro_turno == 'manana':
            filtro_field = f'manana_{filtro_dia}'
        else:
            filtro_field = f'tarde_{filtro_dia}'
        hermanos = hermanos.filter(**{filtro_field: True})
    elif filtro_dia:
        # Filtrar por día (mañana o tarde)
        manana_field = f'manana_{filtro_dia}'
        tarde_field = f'tarde_{filtro_dia}'
        from django.db.models import Q
        hermanos = hermanos.filter(Q(**{manana_field: True}) | Q(**{tarde_field: True}))
    elif filtro_turno:
        # Filtrar por turno (cualquier día)
        from django.db.models import Q
        if filtro_turno == 'manana':
            q = Q(manana_lunes=True) | Q(manana_martes=True) | Q(manana_miercoles=True) | \
                Q(manana_jueves=True) | Q(manana_viernes=True) | Q(manana_sabado=True) | Q(manana_domingo=True)
        else:
            q = Q(tarde_lunes=True) | Q(tarde_martes=True) | Q(tarde_miercoles=True) | \
                Q(tarde_jueves=True) | Q(tarde_viernes=True) | Q(tarde_sabado=True) | Q(tarde_domingo=True)
        hermanos = hermanos.filter(q)

    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    return render(request, "hojaCalculo.html", {
        'hermanos': hermanos,
        'dias': dias,
        'filtro_dia': filtro_dia,
        'filtro_turno': filtro_turno,
    })


# ===== IMPORTAR DATOS JSON (una sola vez) =====

@login_required
def importarJSON(request):
    """Importa datos desde archivos JSON existentes"""
    if request.method == 'POST':
        archivo = request.FILES.get('archivo_json')
        if not archivo:
            return render(request, "importar.html", {'error': 'No se seleccionó ningún archivo'})

        try:
            contenido = archivo.read().decode('utf-8')
            datos = json.loads(contenido)
            count = 0

            for item in datos:
                nombre = item.get('Nombre', '')
                if not nombre:
                    continue

                hermano, created = Hermano.objects.get_or_create(nombre=nombre)
                hermano.comentario = item.get('Comentario', '')

                mananas = item.get('Manana', [])
                tardes = item.get('Tarde', [])
                hermano.set_mananas(mananas if mananas != [''] else [])
                hermano.set_tardes(tardes if tardes != [''] else [])
                hermano.save()

                if created:
                    count += 1

            return render(request, "importar.html", {
                'mensaje': f"Se importaron {count} hermanos nuevos exitosamente."
            })

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            return render(request, "importar.html", {
                'error': f"Error al leer el archivo: {str(e)}"
            })

    return render(request, "importar.html")