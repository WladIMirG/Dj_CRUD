Este projeto consiste en un reporteador basado en CRUD:
Caracteristicas:

- Las versiones que se usan en este proyecto son las de Python 3.8 y Django 3.0.7

 Instrucciones:
 - Configuracion de espacio de trabajo:
    *   Instalar python 3.8.2
    **  Actualizar pip a la version 20.1.1
            
            pip install --upgrade pip

    *** Instalacion de las dependencias:
            Ubicate con la terminal en le directorio crud_report/ (cd crud_report o dir crud_report) y ejecuta el siguiente comando:

                pip install -r requirements.txt

            Se instalaran todos los requerimientos necesarios para este proyecto.

- Puesta en marcha del proyecto:
    *   Ubicate en el directorio crud_report/ e insgrese el siguiente comando:
            python3 manage.py runserver
        
    **  Ingrese desde el navegador a http://127.0.0.1:8000/

    *** Login:
            Super:
                Usuario: Desarrollador
                Password: 123456
            
            No super:
                Usuario: usuarioinvitado
                Password: invitado1

            


El proyecto es un Crud sencillo con nivel de reportes. Los reportes se optienen por cada sección.
El proyecto contiene:

    -   CRUD Usuarios visualizado por nivel de autenticacion y reporteador.
    -   CRUD Libros con generador de comentarios y reporteador.
    -   CRUD de Comentarios con reporteador.