# Importar la clase desde el otro archivo (módulo)
from lavadero import Lavadero

def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):
    """
    Simula el proceso de lavado para un vehículo con las opciones dadas.
    """
    print("--- INICIO: Prueba de Lavado con Opciones Personalizadas ---")
    print(f"Opciones solicitadas: [Prelavado: {prelavado}, Secado a mano: {secado_mano}, Encerado: {encerado}]")

    # 🔧 CLAVE: Resetear estado ANTES de cada prueba
    lavadero.terminar()

    try:
        lavadero.hacerLavado(prelavado, secado_mano, encerado)
        print("\nCoche entra. Estado inicial:")
        lavadero.imprimir_estado()

        print("\nAVANZANDO FASE POR FASE:")
        pasos = 0
        while lavadero.ocupado and pasos < 20:
            lavadero.avanzarFase()
            # 🔧 CORREGIDO: imprimir_fase() → imprimir_estado()
            print(f"Paso {pasos + 1}: ", end="")
            lavadero.imprimir_estado()
            pasos += 1
        
        print("\n----------------------------------------")
        print("Lavado completo. Estado final:")
        lavadero.imprimir_estado()
        print(f"Ingresos acumulados: {lavadero.ingresos:.2f}€")
        print("----------------------------------------")
        
    except ValueError as e:
        print(f"ERROR DE ARGUMENTO: {e}")
    except RuntimeError as e:
        print(f"ERROR DE ESTADO: {e}")
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")

if __name__ == "__main__":
    lavadero_global = Lavadero()
    
    # EJEMPLO 1: Todo activado
    print("\n=======================================================")
    print("EJEMPLO 1: Prelavado (S), Secado a mano (S), Encerado (S)")
    ejecutarSimulacion(lavadero_global, True, True, True)
    
    # EJEMPLO 2: Sin extras
    print("\n=======================================================")
    print("EJEMPLO 2: Sin extras (Prelavado: N, Secado a mano: N, Encerado: N)")
    ejecutarSimulacion(lavadero_global, False, False, False)

    # EJEMPLO 3: ERROR encerado sin secado
    print("\n=======================================================")
    print("EJEMPLO 3: ERROR (Encerado S, Secado a mano N)")
    ejecutarSimulacion(lavadero_global, False, False, True)

    # EJEMPLO 4: Solo prelavado
    print("\n=======================================================")
    print("EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)")
    ejecutarSimulacion(lavadero_global, True, False, False)  # 🔧 CORREGIDO: espacio añadido
