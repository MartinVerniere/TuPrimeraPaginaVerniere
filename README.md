# Como ejecutar el proyecto
- Estando parados en la carpeta principal del proyecto (donde se encuentran myapp y TerceraEntrega), ejecutar el comando "python manage.py runserver" en la consola.

# Probar la app de Django
- Para probar la app, puede hacer click en uno de los botones de la pagina de inicio, o de los botones del navegador, que lo redireccionaran a las URLs que muestran un listado para cada elemento.
- Haciendo click en Crear/Añadir puede añadir un nuevo elemento llenando un formulario
- Utilizando el campo de busqueda puede filtrar resultados que se mostraran (para filtrar se utilizan el nombre del estudiante, el nombre del profesor, y el nombre del curso, respectivamente).
- Si quiere que se muestren todos los resultados deje el campo de busqueda vacio y haga click en buscar.

# Estructura de codigo
- En myapp se encuentra la configuracion relacionada a la app, 
- En el archivo models.py se detallan los modelos
- En el archivo views.py se detallan las vistas
- En el archivo forms.py se detallan los formularios
- Dentro de templates hay un archivo base.html con lo relacionado al navbar
- Dentro de templates/myapp se encuentran los archivos html relacionados a la pagina de inicio, y en cada subcarpeta los archivos html para la lista de elementos y para el formulario de creacion de un elemento nuevo