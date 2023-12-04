import api
import requests


class Peliculas:

    def __init__(self, host, port):
        # declaramos la base de la API con el host y el puerto que
        # se nos entrega, para solicitudes http
        self.base = f"http://{host}:{port}"

    def saludar(self) -> dict:
        # hacemos un get a la base de la API
        mensaje = requests.get(f"{self.base}/")
        # guardamos el status code y el mensaje
        status = mensaje.status_code
        # guardamos el json del mensaje
        json_ms = mensaje.json()
        # retornamos un diccionario con el status code y el mensaje
        return {"status-code": status, "saludo": json_ms["result"]}

    def verificar_informacion(self, pelicula: str) -> bool:
        # hacemos un get al endpoint de peliculas de la API
        mensaje = requests.get(f"{self.base}/peliculas")
        # guardamos el status code y el mensaje
        json_ms = mensaje.json()
        # si la pelicula esta en el json de la API, retornamos True
        if pelicula in json_ms["result"]:
            return True
        # si no, retornamos False
        else:
            return False

    def dar_informacion(self, pelicula: str) -> dict:
        # declaramos los parametros que le pasaremos a la API
        parametros = {
            "pelicula": pelicula,
        }
        # hacemos un get al endpoint informacion con los parametros
        # y guardamos el status code y el mensaje
        mensaje = requests.get(f"{self.base}/informacion", params=parametros)
        status = mensaje.status_code
        # parseamos el mensaje a json
        json_ms = mensaje.json()
        # retornamos un diccionario con el status code y el mensaje
        return {"status-code": status, "mensaje": json_ms["result"]}

    def dar_informacion_aleatoria(self) -> dict:
        # hacemos un get al endpoint de aleatorio de la API
        mensaje_1 = requests.get(f"{self.base}/aleatorio")
        # guardamos el status code y el mensaje
        status = mensaje_1.status_code
        # si el status code es 200, hacemos un get al mensaje
        if status == 200:
            mensaje = requests.get(mensaje_1.json()["result"])
            status = mensaje.status_code
        # si no, retornamos el mensaje
        else:
            mensaje = mensaje_1
        # status = mensaje.status_code
        json_ms = mensaje.json()
        return {"status-code": status, "mensaje": json_ms["result"]}

    def agregar_informacion(self, pelicula: str, sinopsis: str, access_token: str) -> dict:
        # agregamos en headers, el access token Authorization
        headers = {
            'Authorization': access_token,
        }
        # agregamos en data, la pelicula y la sinopsis
        data = {
            'pelicula': pelicula,
            'sinopsis': sinopsis,
        }
        # hacemos un post al endpoint de agregar de la API
        response = requests.post(
            f"{self.base}/update", headers=headers, data=data)
        # guardamos el status code
        status = response.status_code
        # si el status code es 401, retornamos un mensaje de error forbidden
        if status == 401:
            return "Agregar pelicula no autorizado"
        # si el status code es 400, retornamos el mensaje de error
        elif status == 400:
            return response.json()["result"]
        # si no, retornamos el mensaje de exito
        else:
            return "La base de la API ha sido actualizada"

    def actualizar_informacion(self, pelicula: str, sinopsis: str, access_token: str) -> dict:
        # agregamos en headers, el access token Authorization
        headers = {
            'Authorization': access_token,
        }
        # agregamos en data, la pelicula y la sinopsis
        data = {
            'pelicula': pelicula,
            'sinopsis': sinopsis,
        }
        # hacemos un patch al endpoint de actualizar de la API
        response = requests.patch(
            f"{self.base}/update", headers=headers, data=data)
        status = response.status_code
        # si el status code es 401, retornamos un mensaje de error forbidden
        if status == 401:
            return "Editar información no autorizado"
        # si el status code es 400, retornamos el mensaje de error
        elif status == 200:
            return "La base de la API ha sido actualizada"
        # si no, retornamos el mensaje de exito
        else:
            return response.json()["result"]

    def eliminar_pelicula(self, pelicula: str, access_token: str) -> dict:
        # agregamos en headers, el access token Authorization
        headers = {
            'Authorization': access_token,
        }
        # agregamos en data, la pelicula
        data = {
            'pelicula': pelicula,
        }
        # hacemos un delete al endpoint de eliminar de la API
        response = requests.delete(
            f"{self.base}/remove", headers=headers, data=data)
        # guardamos el status code de la respuesta de la API luego de usar
        # el endpoint delete de la API
        status = response.status_code
        # si el status code es 200, retornamos el mensaje de exito
        if status == 200:
            return "La base de la API ha sido actualizada"
        # si el status code es 401, retornamos un mensaje de error forbidden
        elif status == 401:
            return "Eliminar pelicula no autorizado"
        # si no, returnamos la repuesta en formato json en su key result
        else:
            return response.json()["result"]


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    DATABASE = {
        "Mamma Mia": "Mamma Mia es una Comedia musical con ABBA",
        "Monsters Inc": "Monsters Inc trata sobre monstruos que asustan, niños y risas",
        "Incredibles": "Incredibles trata de una familia de superhéroes que salva el mundo",
        "Avengers": "Avengers trata de superhéroes que luchan contra villanos poderosos",
        "Titanic": "Titanic es sobre amor trágico en el hundimiento del Titanic",
        "Akira": "Akira es una película de ciencia ficción japonesa con poderes psíquicos",
        "High School Musical": "High School Musical es un drama musical adolescente en East High",
        "The Princess Diaries": "The Princess Diaries es sobre Mia, una joven que descubre que es"
        "princesa de Genovia",
        "Iron Man": "Iron Man trata sobre un hombre construye traje de alta tecnología "
        "para salvar al mundo",
        "Tarzan": "Tarzan es sobre un hombre criado por simios en la jungla",
        "The Pianist": "The Pianist es sobre un músico judío que sobrevive en Varsovia"
        " durante el Holocausto",
    }
    thread = api.Server(HOST, PORT, DATABASE)
    thread.start()

    Peliculas = Peliculas(HOST, PORT)
    print(Peliculas.saludar())
    print(Peliculas.dar_informacion_aleatoria())
    print(Peliculas.actualizar_informacion("Titanic", "Titanic es sobre amor trágico inspitado"
                                           " en el historico hundimiento del Titanic", "tereiic2233"))
    print(Peliculas.verificar_informacion("Tarzan"))
    print(Peliculas.dar_informacion("The Princess Diaries"))
    print(Peliculas.dar_informacion("Monsters Inc"))
    print(Peliculas.agregar_informacion("Matilda", "Matilda es sobre una niña con poderes"
                                        "telequinéticos que enfrenta a su malvada directora",
                                        "tereiic2233"))
    print(Peliculas.dar_informacion("Matilda"))
