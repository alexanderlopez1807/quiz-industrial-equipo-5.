import random
import streamlit as st

# Base de datos de preguntas
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
            "B": "Los resultados presentan variaciones menores",
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
        "pregunta": "¿Cuál de las siguientes acciones contribuye más a reducir los tiempos de ciclo?",
        "opciones": {
            "A": "Incrementar el número de operarios",
            "B": "Balancear las operaciones entre estaciones",
            "C": "Optimizar el ritmo individual"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué beneficio aporta un flujo de procesos bien definido?",
        "opciones": {
            "A": "Permite asignar responsabilidades generales",
            "B": "Reduce la intervención correctiva frecuente",
            "C": "Facilita identificar actividades innecesarias"
        },
        "respuesta": "C"
    }
]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pantalla_inicio():
    limpiar_pantalla()
    print("===================================================")
    print("JUEGO DE PREGUNTAS SOBRE PROCESOS Y MEJORA CONTINUA")
    print("Ingeniería Industrial")
    print("===================================================\n")
    print("Reglas:")
    print("- 4 preguntas aleatorias")
    print("- 1 punto por respuesta correcta")
    print("- Solo responder A,B o C en las preguntas")

    while True:
        listo = input("¿Estás listo para jugar? (si / no): ").strip().lower()
        if listo in ["si", "no"]:
            return listo == "si"
        else:
            print(" Por favor escribe 'si' o 'no'.")

def jugar():
    puntos = 0
    preguntas_seleccionadas = random.sample(preguntas, 4)

    for i, p in enumerate(preguntas_seleccionadas, 1):
        print(f"\nPregunta {i}: {p['pregunta']}")
        for clave, opcion in p["opciones"].items():
            print(f"{clave}) {opcion}")

        respuesta = input("Tu respuesta (A, B o C): ").upper()

        if respuesta == p["respuesta"]:
            print("✅ Correcto")
            puntos += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {p['respuesta']}")

    calificacion = (puntos / 4) * 10

    print("\n RESULTADOS FINALES")
    print(f"Puntos obtenidos: {puntos}/4")
    print(f"Calificación final: {calificacion:.1f}/10")

def main():
    while True:
        if not pantalla_inicio():
            print("\n Juego cancelado")
            break

        jugar()

        while True:
            repetir = input("\n¿Deseas jugar otra vez? (si / no): ").strip().lower()
            if repetir in ["si", "no"]:
                break
            else:
                print(" Escribe 'si' o 'no'.")

        if repetir != "si":
            print(" Gracias por jugar")
            break

main()

