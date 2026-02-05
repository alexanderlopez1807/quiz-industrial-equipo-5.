import streamlit as st
import random

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(page_title="Quiz Ingeniería Industrial", layout="centered")

# ---------------- BASE DE PREGUNTAS ----------------
preguntas = [
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

# ---------------- SESSION STATE ----------------
if "inicio" not in st.session_state:
    st.session_state.inicio = False
    st.session_state.nombre = ""
    st.session_state.preguntas_juego = random.sample(preguntas, 4)
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.respuesta = None
    st.session_state.respondido = False

# ---------------- PANTALLA DE INICIO ----------------
if not st.session_state.inicio:
    st.title("Quiz de precesos y mejora continua")

    st.subheader("Reglas del juego")
    st.write("• 4 preguntas aleatorias")
    st.write("• Cada pregunta tiene opciones A, B y C")
    st.write("• 1 punto por respuesta correcta")

    st.session_state.nombre = st.text_input("Ingresa tu nombre:")

    if st.button("Estoy listo para jugar"):
        if st.session_state.nombre.strip() == "":
            st.warning("Debes ingresar tu nombre para comenzar")
        else:
            st.session_state.inicio = True
            st.rerun()

# ---------------- JUEGO ----------------
else:
    pregunta_actual = st.session_state.preguntas_juego[st.session_state.indice]

    st.subheader(f"Pregunta {st.session_state.indice + 1} de 4")
    st.write(pregunta_actual["pregunta"])

    st.session_state.respuesta = st.radio(
        "Selecciona tu respuesta:",
        list(pregunta_actual["opciones"].keys()),
        format_func=lambda x: f"{x}) {pregunta_actual['opciones'][x]}"
    )

    if st.button("Responder") and not st.session_state.respondido:
        if st.session_state.respuesta == pregunta_actual["correcta"]:
            st.success("✅ Respuesta correcta")
            st.session_state.puntaje += 1
        else:
            st.error(f"❌ Respuesta incorrecta. La correcta es {pregunta_actual['correcta']}")

        st.session_state.respondido = True

    if st.session_state.respondido:
        if st.button("Siguiente"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.session_state.respuesta = None

            if st.session_state.indice >= 4:
                calificacion = (st.session_state.puntaje / 4) * 10

                st.title(" Resultado final")
                st.write(f"**Nombre:** {st.session_state.nombre}")
                st.write(f"**Puntaje:** {st.session_state.puntaje} / 4")
                st.write(f"**Calificación final:** {calificacion:.1f} / 10")

                if st.button("Jugar otra vez"):
                    st.session_state.clear()
                    st.rerun()
            else:
                st.rerun()


