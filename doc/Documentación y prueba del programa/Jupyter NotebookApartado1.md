# Documentación de la clase Lavadero 

## 1. Definición de la clase y constantes de fase

Este bloque crea la clase `Lavadero` y define las 9 fases posibles del túnel de lavado mediante constantes.  
El uso de constantes con nombres descriptivos mejora la legibilidad y evita números mágicos en el código.


```python
class Lavadero:
    """
    Simula el estado y las operaciones de un túnel de lavado de coches.
    Cumple con los requisitos de estado, avance de fase y reglas de negocio.
    """
    FASE_INACTIVO = 0
    FASE_COBRANDO = 1
    FASE_PRELAVADO_MANO = 2
    FASE_ECHANDO_AGUA = 3
    FASE_ENJABONANDO = 4
    FASE_RODILLOS = 5
    FASE_SECADO_AUTOMATICO = 6
    FASE_SECADO_MANO = 7
    FASE_ENCERADO = 8
```

## 2. Constructor __init__

Inicializa todos los atributos privados del lavadero y llama a `terminar()` para dejarlo en estado inactivo desde el principio.


```python
    def __init__(self):
        """
        Constructor de la clase. Inicializa el lavadero.
        Cumple con el requisito 1.
        """
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar()
```

## 3. Propiedades (getters) de solo lectura

Permiten acceder a los atributos internos de forma segura usando @property.


```python
    @property
    def fase(self):
        return self.__fase

    @property
    def ingresos(self):
        return self.__ingresos

    @property
    def ocupado(self):
        return self.__ocupado
   
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    @property
    def encerado(self):
        return self.__encerado
```

## 4. Método terminar()

Restaura el lavadero al estado inicial cuando termina cualquier lavado.


```python
    def terminar(self):
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
```

## 5. Método hacerLavado()

Inicia un nuevo lavado con las opciones elegidas.  
Aplica las dos reglas de negocio principales:
- No se puede empezar si está ocupado
- El encerado solo es posible con secado a mano


```python
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo ciclo de lavado, validando reglas de negocio.
       
        :raises RuntimeError: Si el lavadero está ocupado (Requisito 3).
        :raises ValueError: Si se intenta encerar sin secado a mano (Requisito 2).
        """
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
       
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
       
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado
```

## 6. Método privado _cobrar()

Calcula el precio del lavado actual según las opciones y lo suma a los ingresos totales.


```python

    def _cobrar(self):
        """
        Calcula y añade los ingresos según las opciones seleccionadas (Requisitos 4-8).
        Precio base: 5.00€ (Implícito, 5.00€ de base + 1.50€ de prelavado + 1.00€ de secado + 1.20€ de encerado = 8.70€)
        """
        coste_lavado = 5.00
        
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.20 
            
        if self.__encerado:
            coste_lavado += 1.00 
            
        self.__ingresos += coste_lavado
        return coste_lavado
```

## 7. Método avanzarFase()

Controla el avance paso a paso del lavado, gestionando todas las ramas posibles según las opciones contratadas.


```python


    def avanzarFase(self):
       
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")

        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO 

            else:
                self.__fase = self.FASE_SECADO_MANO
        
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:

            self.terminar() 
        
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar() 
        
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}. El lavadero va a estallar...")
```

## 8. Métodos de impresión del estado

Permiten ver en pantalla el estado actual del lavadero de forma clara.


```python
    def imprimir_fase(self):
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")

    def imprimir_estado(self):
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")
```

## 9. Método auxiliar para pruebas (ejecutar_y_obtener_fases)

Función de apoyo para pruebas unitarias que ejecuta un lavado completo y devuelve la lista de fases visitadas.


```python
    # Esta función es útil para pruebas unitarias, no es parte del lavadero real
    # nos crea un array con las fases visitadas en un ciclo completo
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
        self.hacerLavado(prelavado, secado, encerado)  # Corregido: era self.lavadero
        fases_visitadas = [self.fase]
       
        while self.ocupado:
            if len(fases_visitadas) > 15:
                raise Exception("Bucle infinito detectado en la simulación de fases.")
            self.avanzarFase()
            fases_visitadas.append(self.fase)
           
        return fases_visitadas

```
