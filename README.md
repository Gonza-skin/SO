### RESPUESTAS

### 1. ¿Porque queue.Queue es apropiada para compartir trabajos?
   Queue es thread safe osea que sus operaciones  como put() o get() tiene un bloqueo interno
   y que varios hilos pueden sacar elementos a la vez
   sin que dos reciban el mismo documento ni se corrompa la estructura

### 2. ¿Que protege Lock y que pasaría sin el?
   Protege los datos compartidos y Actualizar con d(k) = d.get(k, 0) + 1 son para 
   leer, sumar y escribir, si dos hilos se se cruzan los dos pueden leer mismo valor y uno de los incrementos se pierde y
   sin lock el total podría dar menos de 24 y variaría entre ejecuciones

### 3. ¿Que cambiarias si cada documento tuviera que guardarse en un archivo real?
   pues escribir cada documento en un archivo distinto para que los hilos no compartan el mismo archivo
   o tambien usar with open(...) y manejar excepciones de E/S sin perder el proceso

LAS 4 IMAGENES DE LAS EJECUCIONES
### PRIMERA EJECUCION
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/1eb401d8-fd83-44e2-a54a-1d25b80300cf" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/de281636-d5db-4533-8db8-aceee2920dc5" />
### SEGUNDA EJECUCION
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/859f628d-f3c4-4d9c-8b72-622641f35650" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/e6234034-203a-46b1-8f8f-7e0db2e11114" />
### TERCERA EJECUCION
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/21e31760-b5b0-48a8-bfc6-09d3c94a33d7" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4e00eb27-276d-4cb3-86fd-f28ce7338974" />
### CUARTA EJECUCION
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/2517752c-f435-4fd2-99ab-493179aac44b" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/1d65ba3f-0a6f-43e9-aa3d-0160418bfae5" />










