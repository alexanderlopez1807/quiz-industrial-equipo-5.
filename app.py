import streamlit as st
import random
import pandas as pd
import os

st.set_page_config(page_title="Quiz de Procesos y Mejora Continua", layout="centered")

ARCHIVO = "resultados.csv"

# ---------------- PREGUNTAS ----------------
PREGUNTAS = [
    {
        "pregunta": "¿Qué herramienta se utiliza para identificar desperdicios dentro de un proceso?",
        "opciones": {
            "A": "Representación visual estructurada de la secuencia de actividades",
            "B": "Análisis detallado y sistemático de las actividades que conforman el proceso",
            "C": "Registro gráfico del flujo de información y materiales dentro del proceso"
        },
        "correcta": "C"
    },
    {
        "pregunta": "¿Para qué sirve identificar desperdicios en un proceso productivo?",
        "opciones": {
            "A": "Para analizar el desempeño general del proceso",
            "B": "Para detectar actividades que no agregan valor y optimizar el uso de recursos",
            "C": "Para evaluar la eficiencia de cada etapa del proceso"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿Qué es la estandarización dentro de la mejora continua?",
        "opciones": {
            "A": "Establecer criterios generales para la ejecución de las tareas",
            "B": "Definir y documentar la mejor forma de realizar una actividad y aplicarla de manera consistente",
            "C": "Determinar metas operativas para cada área del proceso"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿Por qué es importante medir un proceso dentro de la mejora continua?",
        "opciones": {
            "A": "Para conocer los resultados del proceso y compararlos con los objetivos establecidos",
            "B": "Para documentar información del proceso para futuros análisis",
            "C": "Para registrar el comportamiento del proceso a lo largo del tiempo"
        },
        "correcta": "A"
    },
    {
        "pregunta": "¿Qué papel juega el personal en la mejora continua de los procesos?",
        "opciones": {
            "A": "Ejecutar las actividades conforme a procedimientos establecidos",
            "B": "Supervisar el cumplimiento de normas y políticas internas",
            "C": "Participar activamente en la identificación, análisis y propuesta de mejoras"
        },
        "correcta": "C"
    },
    {
        "pregunta": "¿Qué evidencia indica que el control del proceso aún es frágil?",
        "opciones": {
            "A": "Los resultados se mantienen estables únicamente mediante intervención constante",
            "B": "Los resultados presentan variaciones menores entre periodos",
            "C": "Los resultados cumplen los objetivos establecidos de forma regular"
        },
        "correcta": "A"
    },
    {
        "pregunta": "¿Cuándo puede considerarse que una mejora ha sido correctamente implementada?",
        "opciones": {
            "A": "Cuando se observa una mejora inicial en los indicadores del proceso",
            "B": "Cuando la mejora se mantiene bajo condiciones normales de operación",
            "C": "Cuando el personal percibe el cambio como positivo"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿En qué momento la estandarización debe aplicarse correctamente?",
        "opciones": {
            "A": "Antes de realizar cualquier modificación al proceso",
            "B": "Después de validar que la mejora genera resultados consistentes",
            "C": "Principalmente cuando el proceso presenta desviaciones"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿Cuál acción reduce más los tiempos de ciclo en una línea de producción?",
        "opciones": {
            "A": "Incrementar el número de operarios",
            "B": "Balancear las operaciones entre estaciones",
            "C": "Optimizar el ritmo individual"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿Qué beneficio aporta un flujo de procesos bien definido?",
        "opciones": {
            "A": "Asignar responsabilidades generales",
            "B": "Reducir intervención correctiva frecuente",
            "C": "Identificar actividades innecesarias o repetidas"
        },
        "correcta": "C"
    }
]

# ---------------- FUNCIONES ----------------
def guardar_resultado(nombre, puntaje, calificacion):
    fila = pd.DataFrame([{
        "Nombre": nombre,
        "Puntaje": puntaje,
        "Calificación": calificacion
    }])

    if os.path.exists(ARCHIVO):
        df = pd.read_csv(ARCHIVO)
        df = pd.concat([df, fila], ignore_index=True)
    else:
        df = fila

    df.to_csv(ARCHIVO, index=False)

def reiniciar_juego():
    for key in ["pantalla", "preguntas", "indice", "puntaje", "nombre"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# ---------------- ESTADO ----------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

# ---------------- INICIO ----------------
if st.session_state.pantalla == "inicio":

    st.title("Quiz de Procesos y Mejora Continua")

    st.subheader(" Instrucciones")
    st.write("""
    • Ingresa tu nombre  
    • Responde 4 preguntas aleatorias  
    • Opciones A, B y C  
    • Cada acierto vale 1 punto   
    • Los resultados quedan guardados
    """)

    nombre = st.text_input("Nombre del jugador")
    listo = st.radio("¿Estás listo para jugar?", ["Sí", "No"])

    if st.button("Comenzar"):
        if nombre.strip() == "":
            st.warning("Debes ingresar tu nombre")
        elif listo == "No":
            st.info("Selecciona **Sí** cuando estés listo 😎")
        else:
            st.session_state.nombre = nombre
            st.session_state.preguntas = random.sample(PREGUNTAS, 4)
            st.session_state.indice = 0
            st.session_state.puntaje = 0
            st.session_state.pantalla = "juego"
            st.rerun()

# ---------------- JUEGO ----------------
elif st.session_state.pantalla == "juego":

    if st.session_state.indice >= len(st.session_state.preguntas):

        calificacion = (st.session_state.puntaje / len(st.session_state.preguntas)) * 10
        guardar_resultado(
            st.session_state.nombre,
            st.session_state.puntaje,
            round(calificacion, 1)
        )

        st.title("Resultado Final")
        st.write(f" **Nombre:** {st.session_state.nombre}")
        st.write(f" **Puntaje:** {st.session_state.puntaje}")
        st.write(f" **Calificación:** {calificacion:.1f} / 10")

        if os.path.exists(ARCHIVO):
            st.subheader(" Resultados guardados")
            st.dataframe(pd.read_csv(ARCHIVO))

        if st.button("Reiniciar juego"):
            reiniciar_juego()

    else:
        p = st.session_state.preguntas[st.session_state.indice]

        st.subheader(f"Pregunta {st.session_state.indice + 1}")
        st.write(p["pregunta"])

        respuesta = st.radio(
            "Selecciona una opción:",
            ["A", "B", "C"],
            key=f"resp_{st.session_state.indice}",
            format_func=lambda x: f"{x}) {p['opciones'][x]}"
        )

        if st.button("Responder"):
            if respuesta == p["correcta"]:
                st.success("Correcto ✅")
                st.session_state.puntaje += 1
            else:
                st.error(f"Incorrecto ❌ Respuesta correcta: {p['correcta']}")

            st.session_state.indice += 1
            st.rerun()
