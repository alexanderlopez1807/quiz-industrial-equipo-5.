import streamlit as st
import random
import pandas as pd
import os

st.set_page_config(page_title="Quiz Ingeniería Industrial", layout="centered")

ARCHIVO_RESULTADOS = "resultados.csv"

# ---------------- PREGUNTAS ----------------
PREGUNTAS_BASE = [
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
        "pregunta": "¿Cuál de las siguientes acciones contribuye más a reducir los tiempos de ciclo en una línea de producción?",
        "opciones": {
            "A": "Incrementar el número de operarios en la línea",
            "B": "Balancear las operaciones entre las estaciones de trabajo",
            "C": "Optimizar el ritmo de trabajo individual"
        },
        "correcta": "B"
    },
    {
        "pregunta": "¿Qué beneficio aporta un flujo de procesos bien definido?",
        "opciones": {
            "A": "Permite asignar responsabilidades de forma general",
            "B": "Reduce la necesidad de intervención correctiva frecuente",
            "C": "Facilita la identificación de actividades innecesarias o repetidas"
        },
        "correcta": "C"
    }
]

# ---------------- FUNCIONES ----------------
def guardar_resultado(nombre, puntaje, calificacion):
    nuevo = pd.DataFrame([{
        "Nombre": nombre,
        "Puntaje": puntaje,
        "Calificación": calificacion
    }])

    if os.path.exists(ARCHIVO_RESULTADOS):
        df = pd.read_csv(ARCHIVO_RESULTADOS)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo

    df.to_csv(ARCHIVO_RESULTADOS, index=False)

def reiniciar_juego():
    st.session_state.clear()
    st.rerun()

# ---------------- SESSION STATE ----------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "preguntas" not in st.session_state:
    st.session_state.preguntas = random.sample(PREGUNTAS_BASE, 4)

if "indice" not in st.session_state:
    st.session_state.indice = 0

if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0

# ---------------- PANTALLA INICIO ----------------
if st.session_state.pantalla == "inicio":

    st.title("🎮 Quiz – Ingeniería Industrial")

    nombre = st.text_input("Ingresa tu nombre:")

    if st.button("Estoy listo para jugar"):
        if nombre.strip() == "":
            st.warning("Debes ingresar tu nombre")
        else:
            st.session_state.nombre = nombre
            st.session_state.pantalla = "juego"
            st.rerun()

# ---------------- JUEGO ----------------
elif st.session_state.pantalla == "juego":

    if st.session_state.indice >= 4:

        calificacion = (st.session_state.puntaje / 4) * 10
        guardar_resultado(st.session_state.nombre,
                          st.session_state.puntaje,
                          round(calificacion,1))

        st.title("Resultado Final")
        st.write(f"Nombre: {st.session_state.nombre}")
        st.write(f"Puntaje: {st.session_state.puntaje}/4")
        st.write(f"Calificación: {calificacion:.1f}/10")

        if st.button("Reiniciar juego"):
            reiniciar_juego()

    else:

        pregunta = st.session_state.preguntas[st.session_state.indice]

        st.subheader(f"Pregunta {st.session_state.indice + 1}")
        st.write(pregunta["pregunta"])

        respuesta = st.radio(
            "Selecciona:",
            ["A","B","C"],
            key=f"pregunta_{st.session_state.indice}",   # ⭐ ESTA ES LA SOLUCIÓN
            format_func=lambda x: f"{x}) {pregunta['opciones'][x]}"
        )

        if st.button("Responder"):

            if respuesta == pregunta["correcta"]:
                st.success("Correcto")
                st.session_state.puntaje += 1
            else:
                st.error(f"Incorrecto. Respuesta correcta: {pregunta['correcta']}")

            st.session_state.indice += 1
            st.rerun()

