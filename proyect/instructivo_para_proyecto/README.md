#***INSTRUCTIVO PARA PROYECTOS(IPP)***

##video:
Enlace del video [IPP](https://youtu.be/rwQ0KqpgmFI).


##Integrantes:
- Salvador Alejandro Largaespada Zelaya
- Jorge Wilson Sandoval Rodríguez

Una de las situaciones en las que nos podemos encontrar al momento de realizar un proyecto, es la falta de ideas, ya sea tener la mente en blanco o necesita unicamente un refresco de ideas; pues este es el fin con el cual se creo este proyecto dirigido a estudiantes de programacion de CS50 los cuales seran capaces de interactuar con el sitio donde podran extraer ideas y exponer sus propias ideas tambien.


A continuacion la estructura del programa:

Crear la plantilla index; esta mostrará una interfaz básica, con un botón ingresar que redireccionará a una plantilla creada posteriormente llamada register; esta tendrá acceso a una base de datos con la posibilidad de actualizar la base de datos(CS50) y tendrá un enlace "iniciar sesión" que redireccionará a una plantilla login; una vez ingrese el usuario; entrará a una plantilla "Home" la cual contendrá aspectos básicos tanto del sitio web como de CS50; existirán tantas plantillas de temáticas asociadas a proyectos que contendrán el mismo nombre de su temática, dentro de cada plantilla ~temáticas~ existirá numerosos ejemplos de proyectos con una descripción correspondiente acerca de:
-¿Cómo debería funcionar el proyecto o aplicación?
-¿Qué herramientas necesito para lograr el funcionamiento de mi proyecto?
-¿Qué conocimientos debo de tener para trabajar esta temática y/o proyecto?

El usuario podrá ingresar libremente a estas plantillas(*temáticas*) según sea su interés.
EL usuario dentro de "HOME" tendrá acceso a una herramienta llamada "AYUDA DINÁMICA", al hacer click llevará a una plantilla la cual contendrá un formulario el cual podrá completar para que através de base de datos, fórmulas matemáticas correspondientes y las respuestas ingresadas mostrará resultados porcentuales de las temáticas y proyectos más asociados a las herramientas y conocimientos a los que tiene acceso el usuario.



##**HTML**:
###index:
Dentro de está plantilla existirá descripciones acerca de el propio proyecto, y de CS50, existirán los botones "Register" y "Login" con acceso a las páginas del mismo nombre; esta tendrá enlace a la página principal de CS50 para personas extrañas a CS50, y puedan conocer el curso.
Logo del proyecto o su acrónimo: IPPCSx50






###**register**:
Está será una plantilla sencilla donde se contendrá 3 entradas del usuario las cuales serán "Nombre de Usuario", "Contraseña" y "Confirmar Contraseña" una vez llenado los campos automáticamente enviará al usuario a la plantilla "login". De existir la posibilidad dentro de la base de datos existirá ya una columna llamada correo, con correos electrónicos previamente recolectados por el curso para un acceso exclusivo del staff y de estudiantes de CS50, con esto existiría en la plantilla una entrada de datos más llamada "Correo".

###**login**:
El Login contendrá 2 entradas que serán "Nombre de Usuario" y "Contraseña" de haber obtenido los datos correctamente el programa hará que el usuario entre a "Home".


###**home**:
En este apartado se explicarán conceptos básicos de las herramientas informáticas y lenguajes de programación. Se podrá acceder a las diferentes plantillas "~temáticas~" a través de una barra de navegación pero también a través de diferentes cuadros dónde se observarán las descripciones de cada temática. en está plantilla se implementará el botón "AYUDA DINÁMICA" el cual nos llevará a una plantilla llamada "know".

###**know**:
know será una página para los que no tienen conocimiento alguno de dónde empezar; con un formulario referido a preferencias, conocimientos y herramientas propias del usuario, esto retornará una los resultados de forma porcentual del usuario.
Contendrá una base de datos con las respuestas preestablecidas con lo cual se podrá calcular las preferencias del usuario.

Luego de que el usuario conteste el formulario, se mostrará cuáles tipos de enfoques están afiliados a la persona, de manera gráfica con porcentajes incluidos.

###**_temáticas_**: Mostrara los proyectos correspondientes a cada temática de la informática en la que se puede elaborar un proyecto.


###**JAVASCRIPT**:
Cada plantilla en su etiqueta script contendrá código JAVASCRIPT para el funcionamiento visual del sitio web.

Existirá un foro en el cual los usuarios podrán plantear sus dudas o recomendaciones acerca los proyectos.
Cada ejemplo de proyecto recibirá una función que creará un caja comentarios dondé los usuarios podrán comentar un proyecto en específico.


###**PYTHON**:
Desde el archivo app.py se trabajará la mecánica de redireccionamiento y lógica del sitio incluyendo las consultas y acciones necesarias sobre la base de datos.
Se encargará de la seguridad de registro e ingreso de los usuarios trabajando encima de la base de datos.

En el caso que la persona quiera registrarse pero el correo que ingresa no está en la base de datos, no se podrá registrar ya que no es parte de cs50.
Si el correo ya existe, y el nombre de usuario y contraseña son nulos(aun no se han llenado), entonces se realizará el registro, pero si tanto el username y password ya tiene algo almacenado se le redirigirá a la plantilla “login”

###**SQL**:
En SQL se capturaran los datos de ingreso y depuración para el ingreso de los usuarios siendo información personal cómo Correos, nombres, contraseña(solo del sitio).
La informacionos posts y sus comentarios estaran contenidos en la base de datos

Con una tabla destinada para la verificación de las personas que pueden acceder al sitio.