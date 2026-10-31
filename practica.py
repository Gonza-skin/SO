import threading
import queue
import time
import random

NOMBRES = ["GONZA_SKIN", "ALE_BOLA8", "JACI_JACINTO-CUY", "PEDRO_NEGRO-XD"]
TAMANOS = {doc_id: random.randint(1, 5) for doc_id in range(1, 25)}

def cargar_cola():
    p = queue.Queue()
    for doc_id, tam in TAMANOS.items():
        p.put((doc_id, tam))
    return p

def ejecutar_hilos():
    trabajos = cargar_cola()
    resultados = {}
    tamano_total = {}
    asignacion = []
    lock = threading.Lock()

    def trabajador(nombre):
        while True:
            try:
                doc_id, tam = trabajos.get_nowait()
            except queue.Empty:
                break

            time.sleep(tam * 0.1) 

            with lock:
                resultados[nombre] = resultados.get(nombre, 0) + 1
                tamano_total[nombre] = tamano_total.get(nombre, 0) + tam
                asignacion.append((doc_id, tam, nombre))

    inicio = time.perf_counter()
    hilos = [threading.Thread(target=trabajador, args=(nombre,))
             for nombre in NOMBRES]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
    duracion = time.perf_counter() - inicio
    return resultados, tamano_total, asignacion, hilos, duracion


def ejecutar_secuencial():
    trabajos = cargar_cola()
    inicio = time.perf_counter()
    while True:
        try:
            _, tam = trabajos.get_nowait()
        except queue.Empty:
            break
        time.sleep(tam * 0.1)
    return time.perf_counter() - inicio


resultados, tamano_total, asignacion, hilos, t_hilos = ejecutar_hilos()
print("asignacion de los 24 documentos")
for doc_id, tam, nombre in sorted(asignacion):
    print(f"Documento {doc_id:2d} (tamaño {tam}) -> {nombre}")

print("totales del grupo")
for nombre in NOMBRES:
    print(f"{nombre}: {resultados.get(nombre, 0)} documentos | "
          f"tamaño total: {tamano_total.get(nombre, 0)}")
print("total procesado:", sum(resultados.values()))

ids = [d for d, _, _ in asignacion]
assert sum(resultados.values()) == 24, "verificacion 1 la suma no es 24"
assert len(ids) == len(set(ids)) == 24, "verificacion 2 IDs repetidos o faltantes"
assert not any(h.is_alive() for h in hilos), "verificacion 3 hay hilos vivos"
print("verificacion")

t_sec = ejecutar_secuencial()
print(f"tiempo: {t_sec:.2f} s | 4 hilos: {t_hilos:.2f} s "
      f"| aceleracion: {t_sec / t_hilos:.2f}x")