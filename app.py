import streamlit as st
import random

# -----------------------------
# Base de datos de preguntas
# -----------------------------
preguntas = [
    {
        "pregunta": "¿Qué herramienta se utiliza para identificar desperdicios dentro de un proceso?",
        "opciones": {
            "A": "Representación visual estructurada de la secuencia de actividades",
            "B": "Análisis detallado y sistemático de las actividades que conforman el proceso",
            "C": "Registro gráfico del flujo de información y materiales dentro del proceso"
        },
        "respuesta": "C"
    },
    {
        "pregunta": "¿Para qué sirve identificar desperdicios en un proceso productivo?",
        "opciones": {
            "A": "Para analizar el desempeño general del proceso",
            "B": "Para detectar actividades que no agregan valor y optimizar el uso de recursos",
            "C": "Para evaluar la eficiencia de cada etapa del proceso"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué es la estandarización dentro de la mejora continua?",
        "opciones": {
            "A": "Establecer criterios generales para la ejecución de las tareas",
            "B": "Definir y documentar la mejor forma de realizar una actividad y aplicarla de manera consistente",
            "C": "Determinar metas operativas para cada área del proceso"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Por qué es importante medir un proceso dentro de la mejora continua?",
        "opciones": {
            "A": "Para conocer los resultados del proceso y compararlos con los objetivos establecidos",
            "B": "Para documentar información del proceso para futuros análisis",
            "C": "Para registrar el comportamiento del proceso a lo largo del tiempo"
        },
        "respuesta": "A"
    },
    {
        "pregunta": "¿Qué papel juega el personal en la mejora continua de los procesos?",
        "opciones": {
            "A": "Ejecutar las actividades conforme a procedimientos establecidos",
            "B": "Supervisar el cumplimiento de normas y políticas internas",
            "C": "Participar activamente en la identificación, análisis y propuesta de mejoras"
        },
        "respuesta": "C"
    },
    {
        "pregunta": "¿Qué evidencia indica que el control del proceso aún es frágil?",
        "opciones": {
            "A": "Los resultados se mantienen estables únicamente mediante intervención constante",
            "B": "Los resultados presentan variaciones menores entre periodos",
            "C": "Los resultados cumplen los objetivos establecidos de forma regular"
        },
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuándo puede considerarse que una mejora ha sido correctamente implementada?",
        "opciones": {
            "A": "Cuando se observa una mejora inicial en los indicadores del proceso",
            "B": "Cuando la mejora se mantiene bajo condiciones normales de operación",
            "C": "Cuando el personal percibe el cambio como positivo"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿En qué momento la estandarización debe aplicarse correctamente?",
        "opciones": {
            "A": "Antes de realizar cualquier modificación al proceso",
            "B": "Después de validar que la mejora genera resultados consistentes",
            "C": "Principalmente cuando el proceso presenta desviaciones"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál de las siguientes acciones contribuye más a reducir los tiempos de ciclo en una línea de producción?",
        "opciones": {
            "A": "Incrementar el número de operarios en la línea",
            "B": "Balancear las operaciones entre las estaciones de trabajo",
            "C": "Optimizar el ritmo de trabajo individual"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué beneficio aporta un flujo de procesos bien definido?",
        "opciones": {
            "A": "Permite asignar responsabilidades de forma general",
            "B": "Reduce la necesidad de intervención correctiva frecuente",
            "C": "Facilita la identificación de actividades innecesarias o repetidas"
        },
        "respuesta": "C"
    }
]

# -----------------------------
# Estado inicial
# -----------------------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"
    st.session_state.preguntas_juego = []
    st.session_state.indice = 0
    st.session_state.puntos = 0

st.title("Preguntas sobre Procesos y Mejora Continua")
st.write("Ingeniería Industrial")

# -----------------------------
# Pantalla de inicio
# -----------------------------
if st.session_state.pantalla == "inicio":
    st.subheader("Reglas del juego")
    st.write("- 4 preguntas aleatorias")
    st.write("- Cada pregunta tiene opciones A, B y C")
    st.write("- 1 punto por respuesta correcta")

    if st.button("Estoy listo para jugar"):
        st.session_state.preguntas_juego = random.sample(preguntas, 4)
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.pantalla = "juego"
        st.rerun()

# -----------------------------
# Pantalla del juego
# -----------------------------
elif st.session_state.pantalla == "juego":
    p = st.session_state.preguntas_juego[st.session_state.indice]

    st.subheader(f"Pregunta {st.session_state.indice + 1} de 4")

    opciones_mostradas = [
        f"{letra}) {texto}" for letra, texto in p["opciones"].items()
    ]

    seleccion = st.radio(
        p["pregunta"],
        opciones_mostradas,
        key=f"pregunta_{st.session_state.indice}"
    )

    if st.button("Responder"):
        letra_elegida = seleccion[0]  # A, B o C

        if letra_elegida == p["respuesta"]:
            st.session_state.puntos += 1

        st.session_state.indice += 1

        if st.session_state.indice == 4:
            st.session_state.pantalla = "resultado"
            st.rerun()

# -----------------------------
# Pantalla de resultados
# -----------------------------
elif st.session_state.pantalla == "resultado":
    calificacion = (st.session_state.puntos / 4) * 10

    st.success(f"Puntos obtenidos: {st.session_state.puntos} / 4")
    st.success(f"Calificación final: {calificacion:.1f} / 10")

    if st.button("Jugar otra vez"):
        st.session_state.pantalla = "inicio"
        st.rerun()
       

