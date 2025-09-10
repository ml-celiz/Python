# Aplicación Zona Fit con Flask y MySQL

Aplicacion web para la gestión de clientes de un gimnasio. Permite realizar la gestión de clientes 
de un gimnasio. Realiza operaciones CRUD sobre una base de datos MySQL, almacenando información 
como Id, Nombre, Apellido y Membresía.

---

## Tecnologías Utilizadas
- **Python 3**  
- **Flask** – framework web  
- **MySQL** – base de datos relacional  
- **WTForms** – manejo de formularios en Flask  
- **HTML5 / CSS3/ Bootstrap** – interfaz de usuario básica  

---

## Estructura del Proyecto
```
proyecto_1
└── README.md                       # Este documento
|
└── /.venv                          # Entorno virtual de Python
|
└── /data/zona_fit_app_sql          # Script SQL para la base de datos
|
└── /zona_fit_app/.idea             # Configuración del entorno de desarrollo (IDE)
|
└── /zona_fit_app/templates/
    └── index.html                  # Plantilla principal
|
└──/zona_fit_app/
    ├── app.py                      # Programa principal Flask
    ├── cliente.py                  # Clase Cliente (modelo de datos)
    ├── cliente_dao.py              # Acceso a datos (Data Access Object)
    ├── cliente_form.py             # Formulario (WTForms)
    └── conexion.py                 # Conexión a la base de datos
```

## Intalación y Ejecución
1. Clonar el repositorio
   ```bash
   git clone https://github.com/ml-celiz/Python.git
   cd zona-fit
2. Crear y activar un entorno virtual
    ```bash
    python -m venv .venv
    .venv\Scripts\activate      # En Windows
3. Instalar dependencias
    ```bash
    pip install flask mysql-connector-python wtforms
4. Configurar la base de datos
- Importa el archivo SQL ubicado en /data/zona_fit_app_sql a tu servidor MySQL.
- Ajusta las credenciales de conexión en conexion.py.
5. Ejecutar la aplicación
    ```bash
    python zona_fit_app/app.py
Abrir tu navegador en: http://localhost:5000