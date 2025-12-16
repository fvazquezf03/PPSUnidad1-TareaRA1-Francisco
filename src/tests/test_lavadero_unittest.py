# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test 4: Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero._hacer_lavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
    """    
    def test1_estado_inicial_correcto(self):
        Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos. 
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
"""
 # -------------------------
    # Test 1: Estado inicial
    # -------------------------
    def test1_estado_inicial_inactivo(self):
        """Test 1: Verifica el estado inicial del lavadero."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)
     # -------------------------
    # Test 2: Error encerar sin secado
    # ------------------------
    """
    def test2_excepcion_encerado_sin_secado(self):
        Test 2: Comprueba que encerar sin secado a mano lanza ValueError
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero._hacer_lavado(False, False, True)
    """
  # -------------------------
    # Test 2: Error encerar sin secado
    # -------------------------
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Intentar encerar sin secado a mano lanza ValueError."""
        with self.assertRaises(ValueError) as context:
            self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=False, encerado=True)
        self.assertEqual(str(context.exception), "No se puede encerar el coche sin secado a mano")

    
    # -------------------------
    # Test 3: Error iniciar lavado si ya hay uno en curso
    # -------------------------
    def test3_lavado_mientras_ocupado(self):
        """Test 3: No se puede iniciar un lavado si ya hay uno en curso."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=False, encerado=False)
        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=True)

    # -------------------------
    # Test 4: Ingresos por prelavado a mano
    # -------------------------
    def test4_ingresos_prelavado(self):
        """Test 4: Lavado con prelavado a mano genera 6,50 € de ingresos."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=False, encerado=False)
        self.lavadero.avanzarFase()  # Cobro
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50)

    # -------------------------
    # Test 5: Ingresos por secado a mano
    # -------------------------
    def test5_ingresos_secado(self):
        """Test 5: Lavado con secado a mano genera 6,20 € de ingresos."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()  # Cobro
        self.assertAlmostEqual(self.lavadero.ingresos, 6.20)

    # -------------------------
    # Test 6: Ingresos por secado y encerado
    # -------------------------
    def test6_ingresos_secado_encerado(self):
        """Test 6: Lavado con secado y encerado genera 7,20 € de ingresos."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()  # Cobro
        self.assertAlmostEqual(self.lavadero.ingresos, 7.20)

    # -------------------------
    # Test 7: Ingresos prelavado + secado
    # -------------------------
    def test7_ingresos_prelavado_secado(self):
        """Test 7: Lavado con prelavado y secado genera 7,50 € de ingresos."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()  # Cobro
        self.assertAlmostEqual(self.lavadero.ingresos, 7.50)

    # -------------------------
    # Test 8: Ingresos completos (prelavado + secado + encerado)
    # -------------------------
    def test8_ingresos_completo(self):
        """Test 8: Lavado completo genera 8,70 € de ingresos."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()  # Cobro
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70)

    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
         
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas,
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
      
    
 
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()