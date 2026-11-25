PROYECTO: MUNDO DEPORTIVO
Tema: Deportes
Tecnología: Python, Flask, HTML, CSS y plantillas Jinja2.

ESTRUCTURA
Deportes_Web/
│ app.py
│ requirements.txt
│ README.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── futbol.html
│   ├── baloncesto.html
│   └── voleibol.html
└── static/
    └── estilos.css

¿CÓMO SE APLICA LA HERENCIA?
Las tres páginas de contenido (futbol.html, baloncesto.html y voleibol.html)
utilizan {% extends "base.html" %}. La plantilla base contiene la estructura
general, el encabezado, el menú de navegación, el espacio de contenido y el pie
de página. Cada página hija reemplaza el bloque "contenido" con su información.

REQUISITOS
- Python 3.10 o superior.
- Flask.

CÓMO EJECUTAR
1. Descomprime el archivo ZIP.
2. Abre una terminal dentro de la carpeta Deportes_Web.
3. Instala Flask con: pip install -r requirements.txt
4. Ejecuta: python app.py
5. Abre en el navegador: http://127.0.0.1:5000

PÁGINAS
- Inicio: presentación general y enlaces a los deportes.
- Fútbol: descripción, reglas básicas y beneficios.
- Baloncesto: descripción, reglas básicas y beneficios.
- Voleibol: descripción, reglas básicas y beneficios.

OBJETIVO
Crear una aplicación web informativa con navegación entre páginas y una
plantilla reutilizable mediante herencia.
