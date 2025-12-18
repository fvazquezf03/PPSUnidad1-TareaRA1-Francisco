### **Código utilizado en los unnitest**:
- **Test 1**: este el código utilizado en el test 1

![alt text](image-10.png)

- **Test2**:este el código utilizado en el test 2

![alt text](image-11.png)

- **Test3**:este el código utilizado en el test 3

![alt text](image-12.png)

- **Test4-8**:este el código utilizado en el test 4-8

![alt text](image-13.png)

- **Test9-14**:este el código utilizado en el test 9-14

![alt text](image-14.png)

### **Apartado 3.** A partir de los resultados de los tests, se deben corregir también los problemas encontrados en el código hasta que todos los tests sean correctos.

1. El primer error que me he encontrado es en archivo unittest.py es el siguiente:
- **Causa**
El test llama a _hacer_lavado  el método correcto que hay que poner es sin guiones bajos  hacerLavado:

![alt text](image.png)

- **Solución**:
En el test test_lavadero_unittest.py hay que cambiar lo siguiente:

![alt text](image-1.png)

2. El segundo es error en el precio incorrecto:
- **Causa**: El test espera que un lavado con prelavado a mano y secado a mano costara 7,50 €, pero la  función _cobrar() estaba sumando mal y devolvía 7,70 €.

![alt text](image-2.png)

- **Solución**: Corregir los valores de la suma como vemos en la siguiente imagen:

![alt text](image-5.png)

3. El tercer error hay un error lógico en la secuencia de fases:

![alt text](image-4.png)

- **Solucción**: El flujo respete prelavado, rodillos, secado y encerado según las opciones seleccionadas:

![alt text](image-6.png)

## Para ejecutar las pruebas hay que hacer los siguientes pasos:
1. Hay que activar primero crear el ven  y despues activarlo

![alt text](image-8.png)


![alt text](image-9.png)


2. Ejecutar las pruebas:
```bash
PYTHONPATH=src pytest  tests/test_lavadero_unittest.py -v
```
![alt text](image-15.png)

- **Al terminar de corregir los fallos y a la hora de hacer los test tiene que salir que estan todas pasados**:

![alt text](image-7.png)


