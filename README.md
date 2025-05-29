# Sistema de Alimentación de Peces 🐠

Esta aplicación desarrollada en Streamlit permite:

- Consultar programas de alimentación personalizados para especies de peces.
- Registrar alimentaciones realizadas.
- Visualizar un historial de alimentaciones.
- Acceder a consejos generales para una alimentación saludable.

## 📂 Archivos incluidos

- `appv6.py`: Código principal de la aplicación.
- `historial.csv`: Archivo donde se registran las alimentaciones.
- `README.md`: Este archivo con instrucciones de uso.

## 🚀 Cómo ejecutar la app

1. Instala Streamlit (si no lo tienes):

```bash
pip install streamlit
```

2. Ejecuta la app:

```bash
streamlit run appv6.py
```

3. Se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📌 Notas

- `historial.csv` se crea automáticamente si no existe.
- Puedes añadir más especies en el diccionario `self.especies_peces` dentro de `appv6.py`.

¡Disfruta gestionando tu acuario de forma inteligente! 🐟
