"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        ValueError: Si no hay acciones disponibles
    """
    # INSTRUCCIONES:
    # 1. Eliminar la línea 'raise NotImplementedError...' de abajo
    # 2. Implementar el algoritmo minimax aquí
    # 3. La función debe retornar una tupla (fila, columna) con la mejor jugada

    # Validar que existan acciones disponibles en el estado actual
    acciones = tateti.acciones(estado)
    if not acciones:
        raise ValueError("No hay acciones disponibles")
    
    def minimax_max(problema: Tateti, estado: List[List[str]]) -> float:
        """Calcula recursivamente el valor minimax en un nodo MAX."""
        if problema.test_terminal(estado):
            return problema.utilidad(estado, JUGADOR_MAX)
        
        # Iniciar en -inf para buscar MAX
        valor = float("-inf")
        
        # Explorar acciones disponibles para MAX
        for accion in problema.acciones(estado):
            sucesor = problema.resultado(estado, accion)
            valor = max(valor, minimax_min(problema, sucesor))
        return valor

    def minimax_min(problema: Tateti, estado: List[List[str]]) -> float:
        """Calcula recursivamente el valor minimax en un nodo MIN."""
        #caso base: si el juego terminó, return utilidad respecto a MAX
        if problema.test_terminal(estado):
            return problema.utilidad(estado, JUGADOR_MAX)
        
        # Iniciar en +inf para buscar el MIN
        valor = float("inf")
        
        # Explorar acciones disponibles para MIN
        for accion in problema.acciones(estado):
            sucesor = problema.resultado(estado, accion)
            valor = min(valor, minimax_max(problema, sucesor))
        return valor

    # Algoritmo MINIMAX: determina la mejor acción según el jugador de turno
    if tateti.jugador(estado) == JUGADOR_MAX:
        # Calcular utilidad de cada sucesor evaluado por MIN
        sucs = {
            accion: minimax_min(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return max(sucs, key=sucs.get)

    if tateti.jugador(estado) == JUGADOR_MIN:
        # Calcular utilidad de cada sucesor evaluado por MAX
        sucs = {
            accion: minimax_max(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        # Retornar la acción con el menor valor
        return min(sucs, key=sucs.get)
    