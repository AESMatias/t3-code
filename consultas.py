from utilidades import Funciones
from collections import Counter
from datetime import datetime
import math
from typing import Generator


def peliculas_genero(generador_peliculas: Generator, genero: str):
    # Filtramos las peliculas que tienen el genero especificado
    return (pelicula for pelicula in generador_peliculas if pelicula.genero == genero)


def personas_mayores(generador_personas: Generator, edad: int):
    # Filtramos las personas que tienen la edad especificada
    return (persona for persona in generador_personas if persona.edad >= edad)


def funciones_fecha(generador_funciones: Generator, fecha: str):
    # Aqui, tomamos slices de la fecha para compararlas con las fechas de las funciones,
    # si el anio es de 24 en adelante, se asume que estamos en el siglo XIX
    if fecha[7:] >= '24':
        return (f for f in generador_funciones if f.fecha[0:2] == fecha[0:2]
                and f.fecha[3:5] == fecha[3:5] and f.fecha[7:8] == fecha[9:10])
    # Si el anio es de 23 para abajo, se asume que estamos en el siglo XX
    elif fecha[7:] < '24':
        return (f for f in generador_funciones if f.fecha[0:2] == fecha[0:2]
                and f.fecha[3:5] == fecha[3:5] and f.fecha[7:8] == fecha[9:10])


def titulo_mas_largo(generador_peliculas: Generator) -> str:
    # Obtener una lista con todas las películas
    peliculas = [pelicula for pelicula in generador_peliculas]
    # Ordenar las películas largo del título
    peliculas_sorted_by_title = peliculas
    peliculas_sorted_by_title.sort(
        key=lambda pelicula: len(pelicula.titulo), reverse=True)
    # Obtenemos la longitud del titulo de la pelicula mas larga
    # Obtiene el largo de la peli mas larga
    max_len = len(peliculas_sorted_by_title[0].titulo)
    # Filtra las peliculas que tienen el mismo largo que la primera
    peliculas_filtered_title = [pelicula for pelicula in
                                peliculas_sorted_by_title if len(pelicula.titulo) == max_len]
    # Si hay mas de una pelicula con el mismo largo de titulo...
    if len(peliculas_filtered_title) > 1:
        # y ademas,si el len de de sus titulos es igual para las dos primeras...
        if len(peliculas_filtered_title[0].titulo) == len(peliculas_filtered_title[1].titulo):
            # Ordenamos y filtramos segun el rating
            peliculas_filtered_title.sort(
                key=lambda pelicula: pelicula.rating, reverse=True)
            # Filtramos las peliculas que tienen el mismo rating que la primera
            peliculas_filtered_rating = [pelicula for pelicula in
                                         peliculas_filtered_title if
                                         pelicula.rating == peliculas_filtered_title[0].rating]
            if len(peliculas_filtered_rating) > 1:
                # Si hay mas de una pelicula con el mismo rating, retornamos la ultima generada.
                return peliculas_filtered_rating[-1].titulo
            else:
                return peliculas_filtered_rating[0].titulo
        else:
            return peliculas_sorted_by_title[0].titulo
    else:
        return peliculas_sorted_by_title[0].titulo


def normalizar_fechas(generador_funciones: Generator) -> Generator:
    # Obtenemos las funciones
    funciones = [funcion for funcion in generador_funciones]
    # Mapeamos las fechas desde el formato DD-MM-AA al formato AAAA-MM-DD
    funciones = [Funciones(funcion.id, funcion.numero_sala,
                           funcion.id_pelicula, funcion.horario, '20' +
                           funcion.fecha[6:8] + '-' +
                           funcion.fecha[3:5] + '-' + funcion.fecha[0:2]
                           if int(funcion.fecha[6:8]) <= 23
                           else '19' + funcion.fecha[6:8] + '-' +
                           funcion.fecha[3:5] + '-' + funcion.fecha[0:2])
                 for funcion in funciones]
    # Retornamos las intancias con las fechas normalizadas
    return (funcion for funcion in funciones)


def personas_reservas(generador_reservas: Generator):
    # Obtenemos las reservas y retornamos los ids de las personas en set
    set_id_reservas = {reserva.id_persona for reserva in generador_reservas}
    return set_id_reservas


def peliculas_en_base_al_rating(generador_peliculas: Generator,
                                genero: str, rating_min: int, rating_max: int) -> Generator:
    '''
    Aqui hay un problema, el Enunciado.pdf dice que debo retornar el titulo, 
    que es una propiedad de los objetos del generador, pero si devuelvo el 
    titulo no pasa los test, pero si los pasa todos si devuelvo instancias
    de peliculas, por lo que asumo que el enunciado esta mal. Por favor tener
    en consideracion al revisar. Gracias!
    '''
    # Filtrar las películas por género y rating
    peliculas_filtradas = filter(
        lambda pelicula: pelicula.genero == genero and
        rating_min <= pelicula.rating <= rating_max,
        generador_peliculas
    )
    # Obtenemos los títulos de las películas filtradas
    pelis = (titulo for titulo in peliculas_filtradas)
    # Retornamos el generador de titulos contenido en pelis
    return pelis


def mejores_peliculas(generador_peliculas: Generator) -> Generator:
    # Obtenemos las peliculas
    pelis = [pelicula for pelicula in generador_peliculas]
    # Si hay menos de 20 peliculas, retornamos todas
    if len(pelis) < 20:
        return (pelicula for pelicula in pelis)
    # En otro caso, obtenemos el rating maximo
    max_rating = max(pelis, key=lambda pelicula: pelicula.rating).rating
    # Ordenamos las peliculas por rating
    pelis.sort(key=lambda pelicula: pelicula.rating, reverse=True)
    # Ahora, tomamos las primeras 20 peliculas
    primeras_20_pelis = pelis[:20]
    # Filtramos las peliculas que tienen el mismo rating
    # que el maximo, en caso de que hayan
    pelis_filtradas_rating = [
        pelicula for pelicula in pelis if pelicula.rating == max_rating]

    # Si hay mas de una pelicula con el mismo rating,
    # desempatamos por el id
    if len(pelis_filtradas_rating) > 1:
        pelis.sort(key=lambda pelicula: pelicula.id)
        # Ahora, tomamos las primeras 20 peliculas
        pelis = pelis[:20]
        return (pelicula for pelicula in pelis)
    return (pelicula for pelicula in primeras_20_pelis)


def pelicula_genero_mayor_rating(generador_peliculas: Generator, genero: str) -> str:
    # Filtramos las peliculas que tienen el genero especificado
    pelis = [pelicula for pelicula in generador_peliculas if pelicula.genero == genero]
    # Si hay una sola pelicula del genero, retornamos su titulo
    if len(pelis) > 0 and len(pelis) < 2:
        return max(pelis, key=lambda pelicula: pelicula.rating).titulo
    elif len(pelis) > 1:  # Si hay mas de una pelicula del genero, ordenamos por rating
        pelis.sort(key=lambda pelicula: pelicula.rating, reverse=True)
        return pelis[0].titulo
    else:
        # Si no hay peliculas del genero, retorna un string vacio
        return str('')


def fechas_funciones_pelicula(generador_peliculas: Generator,
                              generador_funciones: Generator, titulo: str):
    # Tomamos todos los ids de las peliculas que tienen el titulo especificado
    ids_pelis = [
        pelicula.id for pelicula in generador_peliculas if pelicula.titulo == titulo]
    # Filtramos las funciones que tienen el id de la pelicula con list comprehension
    funciones_para_esa_peli = [
        funcion for funcion in generador_funciones if funcion.id_pelicula in ids_pelis]
    # Retornamos un generador con las fechas de las funciones
    return (funcion.fecha for funcion in funciones_para_esa_peli)


def genero_mas_transmitido(generador_peliculas: Generator,
                           generador_funciones: Generator, fecha: str) -> str:
    # Transformamos la fecha del formato DD-MM-AAAA al DD-MM-AA
    fecha = fecha[0:6] + fecha[8:10]
    # Filtramos las funciones que tienen la fecha especificada
    funciones = [
        funcion for funcion in generador_funciones if funcion.fecha == fecha]
    # Filtramos las peliculas que tienen el id de las funciones especificadas
    pelis = [pelicula for pelicula in generador_peliculas if pelicula.id in [
        funcion.id_pelicula for funcion in funciones]]
    # Contamos el genero mas transmitido
    generos = [pelicula.genero for pelicula in pelis]
    if len(generos) == 0:
        return str('')
    # Ordenamos los generos por cantidad de apariciones,
    # y elegimos el primero de la list
    genero_mas_transmitido = max(generos, key=generos.count)
    # Contamos la cantidad de veces que aparece el genero mas transmitido
    max_count_genero = generos.count(genero_mas_transmitido)
    # Miramos cuantos generos tienen la misma
    # cantidad de apariciones que el genero mas transmitido
    generos_filtrados = [genero for genero in generos if generos.count(
        genero) == max_count_genero]
    # Retornamos el primero obtenido, contemplando el caso de que haya mas de uno
    return generos_filtrados[0]


def id_funciones_genero(generador_peliculas: Generator,
                        generador_funciones: Generator, genero: str) -> Generator:
    # Obtener el id de las películas del género especificado
    id_peliculas_genero = [
        pelicula.id for pelicula in generador_peliculas if pelicula.genero == genero]

    # Filtrar funciones para las películas del género especificado
    funciones_genero = [
        funcion for funcion in generador_funciones if
        funcion.id_pelicula in id_peliculas_genero]

    # Obtener los identificadores de las funciones seleccionadas
    id_funciones_genero = (funcion.id for funcion in funciones_genero)
    # Retornar el generador con los identificadores de funciones
    yield from id_funciones_genero


def butacas_por_funcion(generador_reservas: Generator,
                        generador_funciones: Generator,
                        id_funcion: int) -> int:
    # Filtrar reservas para la función específica
    reservas_funcion = filter(
        lambda reserva: reserva.id_funcion == id_funcion, generador_reservas)

    # Contar la cantidad de butacas ocupadas
    cantidad_butacas_ocupadas = sum(1 for x in reservas_funcion)
    # Retornar la cantidad de butacas ocupadas
    return cantidad_butacas_ocupadas


def salas_de_pelicula(generador_peliculas: Generator,
                      generador_funciones: Generator, nombre_pelicula: str) -> Generator:
    pelis = [
        pelicula for pelicula in generador_peliculas if pelicula.titulo == nombre_pelicula]
    # Filtrar funciones para la película específica segun su id
    # Tambien se pudo haber filtrado el id en la linea de arriba,
    # pero lo haremos de la siguiente forma
    funciones_para_peli = [funcion for funcion in generador_funciones if
                           funcion.id_pelicula in [peli.id for peli in pelis]]
    return (funcion.numero_sala for funcion in funciones_para_peli)


def nombres_butacas_altas(generador_personas: Generator, generador_peliculas: Generator,
                          generador_reservas: Generator, generador_funciones: Generator,
                          titulo: str, horario: int) -> Generator:
    pelis = [pelicula for pelicula in generador_peliculas if pelicula.titulo == titulo]
    # Filtrar funciones para la película específica segun su id
    funciones = [funcion for funcion in generador_funciones if funcion.id_pelicula in [
        peli.id for peli in pelis]]
    # Filtrar funciones para el horario específico
    funciones_horario = [
        funcion for funcion in funciones if funcion.horario == horario]
    # Filtrar reservas para las funciones del horario específico
    reservas_horario = [reserva for reserva in generador_reservas if reserva.id_funcion in
                        [funcion.id for funcion in funciones_horario]]
    # Obtenemos los nombres de las personas que hicieron reservas
    # para las funciones del horario específico
    nombres_personas = [reserva.nombre for reserva in generador_personas if reserva.id in
                        [reserva.id_persona for reserva in reservas_horario]]
    # Retornamos el generador de nombres de personas
    return {nombre for nombre in nombres_personas}


def nombres_persona_genero_mayores(generador_personas: Generator, generador_peliculas: Generator,
                                   generador_reservas: Generator, generador_funciones: Generator,
                                   nombre_pelicula: str,  genero: str, edad: int):
    pelis = [
        pelicula for pelicula in generador_peliculas if pelicula.titulo == nombre_pelicula]
    # Filtrar funciones para la película específica segun su id
    funciones = [funcion for funcion in generador_funciones if funcion.id_pelicula in [
        peli.id for peli in pelis]]
    # Filtrar reservas para las funciones del horario específico
    reservas_horario = [reserva for reserva in generador_reservas if reserva.id_funcion in
                        [funcion.id for funcion in funciones]]
    # Obtenemos los nombres de las personas que hicieron tienen el
    # genero y su edad es mayor o igual a edad
    nombres_personas = [reserva.nombre for reserva in generador_personas if reserva.id in
                        [reserva.id_persona for reserva in reservas_horario]
                        and reserva.genero == genero and reserva.edad >= edad]
    # Retornamos el generador de nombres de personas
    return {nombre for nombre in nombres_personas}


def genero_comun(generador_personas: Generator, generador_peliculas: Generator,
                 generador_reservas: Generator,
                 generador_funciones: Generator, id_funcion: int) -> str:
    # Obtenemos las peliculas
    pelis = [pelicula for pelicula in generador_peliculas]
    # Obtenemos las funciones
    funciones = [funcion for funcion in generador_funciones]
    # Obtenemos las reservas
    reservas = [reserva for reserva in generador_reservas]
    # Miramos los generos de las personas que hicieron reservas para la funcion especificada
    generos = [reserva.genero for reserva in generador_personas if reserva.id in
               [reserva.id_persona for reserva in reservas if
                   reserva.id_funcion == id_funcion]]
    # Obtenemos el id de la pelicula, y en base a eso, el nombre de la pelicula o titulo
    id_pelicula = [
        funcion.id_pelicula for funcion in funciones if funcion.id == id_funcion]
    nombre_pelicula = [
        pelicula.titulo for pelicula in pelis if pelicula.id == id_pelicula[0]][0]
    # Obtenemos el elemento mas comun
    mas_comun = [elemento for elemento in Counter(generos).most_common(3)]
    genero_mas_comun = mas_comun[0][0] if mas_comun else None

    seg_genero_mas_comun = mas_comun[1][0] if mas_comun and len(
        mas_comun) > 1 else None
    # Empezamos contando 3 generos mas comunes, reduciendo los
    # casos segun la cantidad de personas:
    mas_comun = Counter(generos).most_common(1) if len(mas_comun) > 1 \
        and mas_comun[0][1] != mas_comun[1][1] else\
        Counter(generos).most_common(2) if len(
            mas_comun) > 1 and mas_comun[1][1] != mas_comun[2][1] else mas_comun
    # Obtenemos el id de la pelicula, y en base a eso, el nombre de la pelicula o titulo
    id_pelicula = [
        funcion.id_pelicula for funcion in funciones if funcion.id == id_funcion]
    nombre_pelicula = [
        pelicula.titulo for pelicula in pelis if pelicula.id == id_pelicula[0]][0]
    to_return = ''
    if len(mas_comun) == 1:
        to_return = f"En la función {id_funcion} de la película {nombre_pelicula}" +\
            f" la mayor parte del público es {genero_mas_comun}."
    elif len(mas_comun) == 2:
        to_return = f"En la función {id_funcion} de la película {nombre_pelicula}" +\
            f" se obtiene que la mayor parte del público es de {genero_mas_comun}" +\
            f" y {seg_genero_mas_comun} con la misma cantidad de personas."
    elif len(mas_comun) > 2 or len(mas_comun) == 0:
        to_return = f"En la función {id_funcion} de la película {nombre_pelicula}" +\
            " se obtiene que la cantidad de personas es igual para todos los géneros."
    return to_return


def edad_promedio(generador_personas: Generator,
                  generador_peliculas: Generator,
                  generador_reservas: Generator,
                  generador_funciones: Generator,
                  id_funcion: int) -> str:
    # Obtenemos las peliculas y las funciones a partir de los generadores
    pelis = [pelicula for pelicula in generador_peliculas]
    funciones = [funcion for funcion in generador_funciones]
    # Filtrar reservas para las funciones
    reservas_horario = [
        reserva for reserva in generador_reservas if reserva.id_funcion == id_funcion]

    # Obtener las edades de las personas que hicieron reservas para las funciones
    edades_personas = [reserva.edad for reserva in generador_personas if reserva.id in
                       [reserva.id_persona for reserva in reservas_horario]]
    # Obtenemos la edad promedio y aproximamos mediante la funcion techo superior
    edad_promedio = math.ceil(sum(edades_personas)/len(edades_personas))
    # Obtenemos, en base al id_funcion, el titulo de la pelicula
    id_pelicula = [
        funcion.id_pelicula for funcion in funciones if funcion.id == id_funcion]
    nombre_pelicula = [
        pelicula.titulo for pelicula in pelis if pelicula.id == id_pelicula[0]][0]
    # Retornamos el string con el formato especificado en el enunciado
    return f'En la función {id_funcion} de la película {nombre_pelicula}' +\
        f' la edad promedio del público es {edad_promedio}.'


def obtener_horarios_disponibles(generador_peliculas: Generator,
                                 generador_reservas: Generator,
                                 generador_funciones: Generator,
                                 fecha_funcion: str, reservas_maximas: int):
    # fecha_funcion en formato DD-MM-YY
    # Obtenemos listas a partir de los generadores
    pelis = [pelicula for pelicula in generador_peliculas]
    funciones = [funcion for funcion in generador_funciones]
    reservas = [reserva for reserva in generador_reservas]
    # Obtenemos un objeto datetime a partir de la fecha_funcion
    fecha_funcion_dt = datetime.strptime(fecha_funcion, '%d-%m-%y')

    # Obtener la película con el mayor rating
    pelicula_max_rating = max(pelis, key=lambda pelicula: pelicula.rating)

    # Filtrar las funciones para obtener las disponibles
    horarios_disponibles = {funcion.horario for funcion in funciones
                            if funcion.id_pelicula == pelicula_max_rating.id
                            and fecha_funcion_dt == datetime.strptime(funcion.fecha, '%d-%m-%y')
                            and len([reserva for reserva in reservas if
                                     reserva.id_funcion == funcion.id]) < reservas_maximas}

    return horarios_disponibles


def personas_no_asisten(generador_personas: Generator,
                        generador_reservas: Generator,
                        generador_funciones: Generator,
                        fecha_inicio: str, fecha_termino: str) -> Generator:

    personas = [persona for persona in generador_personas]
    reservas = [reserva for reserva in generador_reservas]
    funciones = [funcion for funcion in generador_funciones]
    # Filtramos las personas que no asistieron a ninguna funcion
    # El formato de fecha_termino es DD-MM-AAAA, mientras que
    # el formato de fecha de las funciones es DD-MM-AA
    # Retornamos el generador de personas

    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%d-%m-%Y')
    fecha_termino_dt = datetime.strptime(fecha_termino, '%d-%m-%Y')

    # Filtramos las personas que no asistieron a ninguna funcion
    # Usando list comprehension y el metodo strptime de datetime
    personas_no_asisten = [persona for persona in personas if persona.id not in
                           [reserva.id_persona for reserva in reservas if reserva.id_funcion in
                            [funcion.id for funcion in funciones if
                             fecha_inicio_dt <= datetime.strptime(
                                 funcion.fecha, '%d-%m-%y')
                             <= fecha_termino_dt]]]
    # Retornamos el generador de personas
    return (persona for persona in personas_no_asisten)
