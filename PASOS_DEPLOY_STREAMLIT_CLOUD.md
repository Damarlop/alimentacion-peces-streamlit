# Cómo desplegar tu app en Streamlit Cloud 🚀

Sigue estos pasos para subir tu proyecto `Sistema de Alimentación de Peces` a la nube con Streamlit Cloud:

---

## 1. Crea una cuenta en Streamlit Cloud

Ve a: [https://streamlit.io/cloud](https://streamlit.io/cloud) y regístrate con tu cuenta de Google o GitHub.

---

## 2. Sube el proyecto a GitHub

1. Ve a [https://github.com](https://github.com).
2. Crea un nuevo repositorio. Ejemplo: `alimentacion-peces-streamlit`
3. Sube los archivos del ZIP que descargaste:
   - `appv6.py`
   - `historial.csv`
   - `README.md`
   - `requirements.txt`

Puedes hacerlo directamente desde la interfaz web de GitHub:

- En tu repositorio, haz clic en **Add file** → **Upload files**.
- Arrastra y suelta los 4 archivos.
- Haz clic en **Commit changes**.

---

## 3. Publica tu app

1. Entra en [https://streamlit.io/cloud](https://streamlit.io/cloud).
2. Haz clic en **New app**.
3. Selecciona el repositorio que creaste.
4. En el campo **main file path**, escribe:

```
appv6.py
```

5. Haz clic en **Deploy**.

---

## 4. ¡Listo!

Tu app estará en línea con una URL pública tipo:

```
https://nombreusuario-streamlit-alimentacion-peces.streamlit.app
```

---

## ✅ Recomendaciones

- Puedes editar `historial.csv` desde el código o permitir que se llene dinámicamente al usar la app.
- Si haces cambios, solo haz push a GitHub y Streamlit Cloud actualizará automáticamente.

¡Ya puedes compartir tu sistema inteligente de alimentación de peces al mundo! 🐟✨
