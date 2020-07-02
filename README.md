Este projeto consiste en un reporteador basado en CRUD:
Caracteristicas:

- Las versiones que se usan en este proyecto son las de Python 3.8 y Django 3.0.7

 Instrucciones:

	La prueba de conocimiento se basa en 2 fases Backend y Frontend, los cuales al deben conectar entre sí.
     Backend
        Modelos a crear
            users
                id_user
                username
                password
                first_name
                last_name
            books
                id_book
                title
                publication_date
            comments
                id_comment
                id_book
                text
                created_date
                id_user
        Controladores
            Cada modelo debe tener los métodos CRUD
            Externo: se debe consumir un api externo ( Spotify - Twitter - Marvel - OpenLibra) y entregar los datos por ese endPoint.
            Reporte: Los datos del api externo también debe revolverse dentro de un reporte en formato PDF y Excel. 
    Frontend
        Vistas
            Login
            CRUD
                Users
                Books
                    Se debe poder agregar los comentarios
            ApiExterna
                Se debe poder generar los reportes en los 2 formatos.

Se debe utilizar una base de datos en SQLite.
Se podrá utilizar cualquier FrameWork, para el API.
El Fronted se podrá utilizar los templates nativos de framework, o una librería reactiva.
