import streamlit as st
import datetime
import csv
import os
from typing import Dict

class SistemAlimentacionPeces:
    def __init__(self):
        self.historial_alimentacion = []
        self.archivo_csv = "historial.csv"

        self.especies_peces = {
            "goldfish": {"frecuencia_diaria": 2, "cantidad_gramos": 0.5, "horarios": ["08:00", "18:00"], "ayuno_semanal": True, "dia_ayuno": "domingo"},
            "betta": {"frecuencia_diaria": 1, "cantidad_gramos": 0.2, "horarios": ["09:00"], "ayuno_semanal": True, "dia_ayuno": "domingo"},
            "guppy": {"frecuencia_diaria": 2, "cantidad_gramos": 0.3, "horarios": ["08:30", "17:30"], "ayuno_semanal": False, "dia_ayuno": None},
            "tetra": {"frecuencia_diaria": 2, "cantidad_gramos": 0.4, "horarios": ["08:00", "19:00"], "ayuno_semanal": True, "dia_ayuno": "domingo"},
            "angel": {"frecuencia_diaria": 2, "cantidad_gramos": 0.8, "horarios": ["07:30", "18:30"], "ayuno_semanal": True, "dia_ayuno": "domingo"}
        }

    def obtener_info_especie(self, especie: str) -> Dict:
        return self.especies_peces.get(especie.lower(), None)

    def es_dia_ayuno(self, especie: str) -> bool:
        info = self.obtener_info_especie(especie)
        if not info or not info["ayuno_semanal"]:
            return False

        hoy = datetime.datetime.now().strftime("%A").lower()
        dias_espanol = {
            "monday": "lunes", "tuesday": "martes", "wednesday": "miércoles",
            "thursday": "jueves", "friday": "viernes", "saturday": "sábado", "sunday": "domingo"
        }
        dia_hoy_espanol = dias_espanol.get(hoy, hoy)
        return dia_hoy_espanol == info["dia_ayuno"]

    def calcular_proxima_alimentacion(self, especie: str) -> str:
        info = self.obtener_info_especie(especie)
        if not info:
            return "Especie no encontrada"

        ahora = datetime.datetime.now()
        hoy = ahora.date()

        if self.es_dia_ayuno(especie):
            manana = hoy + datetime.timedelta(days=1)
            return f"Mañana {manana.strftime('%d/%m/%Y')} a las {info['horarios'][0]} (hoy es día de ayuno)"

        for horario in info["horarios"]:
            hora_alimentacion = datetime.datetime.strptime(f"{hoy} {horario}", "%Y-%m-%d %H:%M")
            if hora_alimentacion > ahora:
                return f"Hoy a las {horario}"

        manana = hoy + datetime.timedelta(days=1)
        return f"Mañana {manana.strftime('%d/%m/%Y')} a las {info['horarios'][0]}"

    def registrar_alimentacion(self, especie: str, cantidad: float):
        registro = {
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "especie": especie,
            "cantidad": cantidad
        }
        self.historial_alimentacion.append(registro)

        archivo_nuevo = not os.path.exists(self.archivo_csv)
        with open(self.archivo_csv, mode="a", newline="", encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["fecha", "especie", "cantidad"])
            if archivo_nuevo:
                writer.writeheader()
            writer.writerow(registro)

    def leer_historial_csv(self):
        if not os.path.exists(self.archivo_csv):
            return []
        with open(self.archivo_csv, newline="", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def consejos_alimentacion(self):
        return [
            "Alimenta solo la cantidad que puedan comer en 2-3 minutos",
            "Es mejor quedarse corto que sobrealimentar",
            "El ayuno semanal ayuda a la digestión y salud del pez",
            "Observa si quedan restos de comida y ajusta la cantidad",
            "Varía el tipo de alimento ocasionalmente",
            "Mantén el agua limpia, la sobrealimentación contamina",
            "Si vas de vacaciones, es mejor que ayunen 3-4 días que sobrealimentar"
        ]

sistema = SistemAlimentacionPeces()

st.title("🐠 Sistema de Alimentación de Peces")
menu = st.sidebar.radio("Selecciona una opción:", (
    "Ver especies disponibles", "Consultar programa de alimentación",
    "Registrar alimentación", "Ver historial de alimentación",
    "Consejos de alimentación"
))

if menu == "Ver especies disponibles":
    st.header("🐠 Especies de peces disponibles")
    st.markdown(f"**Total: {len(sistema.especies_peces)} especies**")
    for especie in sistema.especies_peces:
        st.markdown(f"- **{especie.capitalize()}**")

elif menu == "Consultar programa de alimentación":
    especie = st.selectbox("Selecciona una especie:", list(sistema.especies_peces.keys()))
    info = sistema.obtener_info_especie(especie)
    if info:
        st.subheader(f"📋 Programa de alimentación - {especie.upper()}")
        st.text(f"Frecuencia diaria: {info['frecuencia_diaria']} veces")
        st.text(f"Cantidad por vez: {info['cantidad_gramos']} gramos")
        st.text(f"Horarios: {', '.join(info['horarios'])}")
        st.text(f"Día de ayuno: {info['dia_ayuno'] if info['ayuno_semanal'] else 'Ninguno'}")
        st.success(f"⏰ Próxima alimentación: {sistema.calcular_proxima_alimentacion(especie)}")
        if sistema.es_dia_ayuno(especie):
            st.warning("🔔 ¡HOY ES DÍA DE AYUNO! No alimentar.")
        else:
            st.info("✅ Hoy sí debes alimentar según el horario.")

elif menu == "Registrar alimentación":
    especie = st.selectbox("Selecciona la especie alimentada:", list(sistema.especies_peces.keys()))
    cantidad = st.number_input("Cantidad en gramos:", min_value=0.0, step=0.1)
    if st.button("Registrar"):
        sistema.registrar_alimentacion(especie, cantidad)
        st.success("✅ Alimentación registrada correctamente")
        historial = sistema.leer_historial_csv()
        if historial:
            st.subheader("📜 Historial de alimentaciones")
            st.dataframe(historial)

elif menu == "Ver historial de alimentación":
    st.header("📜 Historial de Alimentaciones")
    historial = sistema.leer_historial_csv()
    if historial:
        st.dataframe(historial)
    else:
        st.info("No hay registros todavía.")

elif menu == "Consejos de alimentación":
    st.header("💡 Consejos importantes para alimentar peces")
    for consejo in sistema.consejos_alimentacion():
        st.markdown(f"- {consejo}")
