# VIDEO EXPLICATIVO
https://drive.google.com/file/d/1SINXiaR4XJJXLjec3EAPNL7YPG1TVu_V/view?usp=drive_link
# Estas son las funcionalidades de la página:
- Se pueden crear usuarios con nombre, email y contraseña. 
- Una vez creados, se pueden logear y ver todos los datos del usuario
- Cuando se hace click en el nombre del usuario, te dirige a una página que muestra los datos del usuario con un bonito estilo de tarjeta, y también hay un botón de editar usuario
- En la edición de usuario se le puede agregar un avatar, nombre y apellido y el género favorito. Si no se le carga avatar, se le asigna el default. También hay un botón de cambiar contraseña
- En la pantalla de cambiar contraseña, se puede cambiar la contraseña o volver atrás

# Luego tenemos las vistas que manejan películas: 
- La ruta base es el inicio, donde tiene una introducción y luego botones que cambian según el usuario logeado tenga o no películas cargadas en la lista.
- Tanto Crear Peli Nueva como Listado de pelis tienen decoradores y mixin para no mostrarse si no se está logeado.
- La vista de "about us" está libre, para que cualquiera ingrese independiente de si tiene usuario o no. Tiene una breve descripción de las funcionalidades de la página web.
- La vista de crear peli tiene la opción de crear una película nueva, con los campos título, director, fecha de lanzamiento (datefield), duración en minutos, género (choicefield), puntaje (choicefield de int) y poster (imgfield).
- Cuando se agrega la película nueva, se redirige a la lista de películas ya cargadas.
- Se muestran solo las películas del usuario logeado, y se muestran primero las películas del género favorito del usuario que ingresó al crear el usuario (si es que ingresó).
- En esta vista, se ven algunos de los campos de cada película que pueden ser filtradas por título, director, fecha de estreno, duración, género y puntaje.
- Además, cada peli tiene 3 botones:
  1) ver más: redirecciona a una vista que muestra todos los detalles (campos) de la película seleccioanda. Tiene un botón para volver al listado de películas.
  2) Editar: redirecciona a una vista que permite editar cualquier campo de la película, incluso el poster
  3) Eliminar: Elimina a la película seleccionada

# Algunos detalles extra:
- Le agregué un ícono a la web para que se vea en la pestaña
- Le agregué un estilo de identidad a la web, con colores consistentes en todas las vistas
- Le agregué botones más bonitos que los default siempre que pude
- Le cambié la forma al avatar del navbar
- Le mejoré el css a varias vistas de la página.