# tests/test_lavadero_unittest.py

import unittest
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):

    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

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
    # Test 4-8: Comprobación de ingresos según opciones
    # -------------------------
    def test4_ingresos_prelavado(self):
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=False, encerado=False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50)

    def test5_ingresos_secado(self):
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 6.20)

    def test6_ingresos_secado_encerado(self):
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.20)

    def test7_ingresos_prelavado_secado(self):
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.50)

    def test8_ingresos_completo(self):
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70)

    # -------------------------
    # Test 9-14: Flujo de fases
    # -------------------------
    def test9_flujo_rapido_sin_extras(self):
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test10_flujo_con_prelavado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=False, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test11_flujo_con_secado(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test12_flujo_con_secado_encerado(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=True)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test13_flujo_prelavado_secado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test14_flujo_prelavado_secado_encerado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        self.assertEqual(fases_obtenidas, fases_esperadas)


if __name__ == '__main__':
    unittest.main()
