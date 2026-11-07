# Laboratorio 2 de Óptica y Ondas: imágenes en espejos esféricos

Datos y análisis del laboratorio "Formación y análisis de imágenes en espejos cóncavos y convexos" del curso Óptica y Ondas (UTEC, ciclo 2026-II). Grupo 6: Christopher Perez Torres, Oswaldo Alejandro Quispe Monzón, Camilo Soto Cristobal y Mauricio Teran Taica.

Usamos un espejo de doble cara con distancia focal f = 20 cm según el fabricante (R = 40 cm), una fuente con una flecha de 2 cm colocada en 0 cm del riel óptico y una pantalla de papel grueso. Con la cara cóncava medimos diez posiciones para el Cuadro 1 y los cuatro casos del Cuadro 2. Con la cara convexa comprobamos que la imagen no se puede proyectar en la pantalla.

## Contenido

```
datos/
  cuadro1_concavo.csv        d₀, dᵢ y altura de imagen hᵢ en diez posiciones
  cuadro2_casos.csv          d₀ > R, d₀ = R, f < d₀ < R y d₀ < f: dᵢ medido y M estimado
notebooks/
  01_focal_ajuste.ipynb      f por la ecuación del espejo, ajuste de M contra dᵢ,
                             análisis de error y recta de 1/dᵢ contra 1/d₀
  02_casos_cuadro2.ipynb     dᵢ y M teóricos del Cuadro 2 y del espejo convexo
figuras/                     gráficas que generan los notebooks
fotos/                       fotografías tomadas durante el laboratorio
evidencias/                  hojas de los apéndices A, B y C firmadas por el encargado
documento/                   documento de apoyo del video (HTML y PDF)
presentacion/                diapositivas del video (HTML, PDF y recursos)
generar_pdfs.py              regenera los dos PDF a partir de sus HTML
```

## Resultados

Con la ecuación del espejo aplicada a cada fila del Cuadro 1, f = 19.85 ± 0.05 cm y R = 39.7 ± 0.1 cm, un error de 0.7 % respecto a los 20 cm del fabricante.

Combinando M = −dᵢ/d₀ con la ecuación del espejo sale M = 1 − dᵢ/f, una recta de pendiente −1/f. El ajuste da M = −0.0471·dᵢ + 0.896 con R² = 0.958, de donde f = 21.2 ± 1.6 cm y R = 42.5 ± 3.1 cm (6.2 % de error, dentro de la incertidumbre). Este método es unas treinta veces menos preciso porque depende de hᵢ, que mide entre 0.6 y 1.6 cm con una regla de 1 mm. Si se fija el intercepto en 1, como predice la teoría, f = 19.8 ± 0.1 cm.

La recta de 1/dᵢ contra 1/d₀, que solo usa distancias, tiene pendiente −0.996 ± 0.042 (la teoría pide −1) y da f = 19.9 ± 0.3 cm.

En el Cuadro 2 las diferencias en dᵢ son de 1.0 % (d₀ = 50 cm), 0 % (d₀ = 40 cm) y 10.0 % (d₀ = 35 cm). Con d₀ = 10 cm, menor que f, la imagen es virtual y no se pudo proyectar, como predice el dᵢ teórico negativo (−20 cm). La cara convexa no formó imagen en la pantalla a 50, 30 ni 10 cm.

## Nota sobre los datos

Los valores se transcribieron sin cambios de la hoja firmada del apéndice C (`evidencias/apendice_C_tablas_firmado.jpeg`), con una excepción documentada: en la última fila del Cuadro 2 la hoja dice d₀ = 15 cm, pero la medición se hizo a 10 cm, como confirman los valores calculados en la misma hoja (dᵢ = −20 cm y M = 2). La sección 8 del documento lo detalla.

## Cómo correrlo

```
pip install -r requirements.txt
cd notebooks
jupyter notebook
```

Los notebooks leen los datos con rutas relativas, así que hay que abrirlos desde la carpeta `notebooks/`. Para regenerar los PDF hace falta además `python -m playwright install chromium`; luego `python generar_pdfs.py --video <enlace de YouTube>`.

## Enlaces

- Video: [FALTA: enlace de YouTube]
