from django.shortcuts import render
import pywhatkit
import json

dir = "C:/Users/candaku/Desktop/Predi/personas.json"
git = "C:/Users/candaku/Documents/GitHub/Disponibilidad/Github_Disponibilidad.json"
datos = "C:/Users/candaku/Desktop/Predi2/hermanos/DJANGO-APP-DISPONIBILIDAD\hermanos/templates/numeros.json"
mesSiguiente = ""
def CargarInfo():

    # Carga info del Json y la devuelve

    with open(dir, "r") as archivo:
        info = json.load(archivo)

    return info


def cargarNumeros():

    with open(datos, "r") as archivo:
        numeros = json.load(archivo)

    return numeros    

def github(request):

    return render(request, "github.html")



def listarHermanos(request):

    hermanos = CargarInfo()

    for hermano in hermanos:
        hermano["Manana_list"] = [dia for dia in hermano.get("Manana", [""]) if dia]
        hermano["Tarde_list"] = [dia for dia in hermano.get("Tarde", [""]) if dia]

    return render(request, "listarHermanos.html", {'hermanos': hermanos})
def index(request):

    return render(request, "base.html")


def buscarHermano(nombre):

    hermanos = CargarInfo()

    for hermano in hermanos:

        if hermano["Nombre"] == nombre:
            return hermano
    
    return []


def buscar(request):

    return render(request, "buscarHermano.html")

def editar(request):

    nombre = request.POST["nombre"].lower()

    hermano = buscarHermano(nombre)

    if hermano == []:

        return render(request, "editar.html", {'error': "Hermano no encontrado"})
    
    dias_guardados = hermano["Manana"]
    tardes_guardados = hermano["Tarde"]
    
    return render(request, "editar.html", {'Hermano': hermano, 'dias_guardados': dias_guardados, 'tardes_guardados': tardes_guardados })

def editarHermano(request):

    nombre = request.POST["nombre"]
    manana = request.POST.getlist("dias")
    tarde = request.POST.getlist("tardes")
    comentario = request.POST["comentario"]


    if not tarde:
        tarde = [""]

    if not manana:
        manana = [""]

    hermanos = CargarInfo()

    for hermano in hermanos:

        if hermano["Nombre"] == nombre:
            hermano["Nombre"] = nombre
            hermano["Manana"] = manana
            hermano["Tarde"] = tarde
            hermano["Comentario"] = comentario

    Actualizar(hermanos)

    return buscar(request)



def elegirMes(request):

    return render(request, "elegirMes.html")

def cargarMensajes(mes):
    hermanos = CargarInfo()
    numeros = cargarNumeros()

    mensaje = []

    todos = ["lunes",
            "martes",
            "miercoles",
            "jueves",
            "viernes",
            "sabado",
            "domingo"]

    for i in hermanos:

        numero = ""
        # Revisamos la mañana
        if i["Manana"] == [""] or not i["Manana"]:
            mananas_texto = "no podía"
        else:
            mananas_texto = "podía los " + ", ".join(i["Manana"])

        if i["Manana"] == todos:
            mananas_texto = "podía todos los dias"

        # Revisamos la tarde
        if i["Tarde"] == [""] or not i["Tarde"]:
            tardes_texto = "no podía"
        else:
            tardes_texto = "podía los " + ", ".join(i["Tarde"])

        if i["Tarde"] == todos:
            mananas_texto = "podía todas las tardes"

        texto = (
            f"Hola, estamos confirmando su disponibilidad para el mes de {mes} . "
            f"Usted nos dijo que {mananas_texto} en las mañanas, "
            f"y que {tardes_texto} en las tardes. "
            "Confirmar si mantendrá esta disponibilidad o la cambiará. "
            "De antemano se le agradece su buena disposición. "
            "*Si no responde a este mensaje vamos a asumir que la mantiene.*"
        )

        for num in numeros:

            if num["Nombre"] == i["Nombre"]:
                numero = num["Numero"]

        mensaje.append({"Nombre": i["Nombre"], "Texto": texto, "Numero": numero})

    return mensaje


def mensajes(request):

    global mesSiguiente
    mesSiguiente = request.POST["mes"]
    mensaje = cargarMensajes(mesSiguiente)
    
    return render(request, "mensajes.html", {'mensaje': mensaje})



def agregarHermano(request):

    return render(request, "agregarHermano.html")

def agregar(request):

    nombre = request.POST["nombre"]
    manana = request.POST.getlist("dias")
    tarde = request.POST.getlist("tardes")
    comentario = request.POST["comentario"]

    if not tarde:
        tarde = [""]

    if not manana:
        manana = [""]


    hermano = {"Nombre": nombre,
        "Manana":manana
        ,
        "Tarde":  tarde
        ,
        "Mensaje": False,
        "Comentario": comentario}
    
    hermanos = CargarInfo()

    hermanos.append(hermano)

    Actualizar(hermanos)

    return render(request, "agregarHermano.html", {'mensaje': "Hermano agregado"})
    

def wspMensaje(request):

    numero = request.POST["Numero"]
    texto = request.POST["Texto"]

    pywhatkit.sendwhatmsg_instantly(numero,texto)

    mensaje= cargarMensajes(mesSiguiente)

    return render(request, "mensajes.html", {'texto': "Enviado por wsp!", "mensaje": mensaje})






#Aqui van las mismas funciones del programa anterior

def Actualizar(info):

    #Al entregarle un json lo escribe en personas json. Solamente se utiliza al agregar cosas

    with open(dir, "w") as archivo: 
      json.dump(info, archivo, indent=4)

def subir(request):

    info = CargarInfo()
            
    with open(git, "w") as archivo:
        json.dump(info, archivo, indent=4)    


    return render(request, "github.html", {'mensaje': "Realizado! Revisa GitHub Desktop"})


def cargar(request):

    with open(git, "r") as archivo:
        info = json.load(archivo)
    Actualizar(info)

    return render(request, "github.html", {'mensaje': "Realizado! Revisa los cambios"})