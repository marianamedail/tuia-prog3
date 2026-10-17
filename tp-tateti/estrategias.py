"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

import math
neg_inf = -math.inf
pos_inf = math.inf

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

    print(f"Jugador: {tateti.jugador}")
    
    return random.choice(acciones_disponibles)

def MINIMAX_max(tateti: Tateti, estado: List[List[str]]):
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)

    valor = neg_inf

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, MINIMAX_min(tateti, sucesor))
    return valor


def MINIMAX_min(tateti: Tateti, estado: List[List[str]]):
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)

    valor = pos_inf

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, MINIMAX_max(tateti, sucesor))
    return valor


def estrategia_minimax(tateti: Tateti, estado: List[List[str]]):
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """

    sucs = {}

    if tateti.jugador(estado) ==  JUGADOR_MAX:
        acciones = tateti.acciones(estado)

        for accion in acciones:
            value = MINIMAX_min(tateti, tateti.resultado(estado, accion))
            sucs[accion] = value

        return max(sucs, key = sucs.get)
    if tateti.jugador(estado) ==  JUGADOR_MIN:
        acciones = tateti.acciones(estado)

        for accion in acciones:
            value = MINIMAX_max(tateti, tateti.resultado(estado, accion))
            sucs[accion] = value
        return min(sucs, key = sucs.get)


# reached[root.state] = root.cost

'''
function MINIMAX(problema, estado) return acción
    if problema.JUGADOR(estado) == MAX:
        sucs ← {acción: MINIMAX-MIN(problema, problema.RESULTADO(estado, acción)) for acción in problema.ACCIONES(estado)}
        return max(sucs, key=sucs.get) # obtiene la clave con el mayor valor

    if problema.JUGADOR(estado) == MIN:
        sucs ← {acción: MINIMAX-MAX(problema, problema.RESULTADO(estado, acción)) for acción in problema.ACCIONES(estado)}
        return min(sucs, key=sucs.get) # obtiene la clave con el menor valor

# Calcula recursivamente el valor minimax de un estado MAX
function MINIMAX-MAX(problema, estado) return valor
    if problema.TEST-TERMINAL(estado) then
        return problema.UTILIDAD(estado,MAX)
    valor ← -∞
    forall acción in problema.ACCIONES(estado) do
        sucesor ← problema.RESULTADO(estado, acción)
        valor ← max(valor, MINIMAX-MIN(problema, sucesor)
    return valor

# Calcula recursivamente el valor minimax de un estado MIN
function MINIMAX-MIN(problema, estado) return valor
    if problema.TEST-TERMINAL(estado) then
        return problema.UTILIDAD(estado,MAX)
    valor ← +∞
    forall acción in problema.ACCIONES(estado) do
        sucesor ← problema.RESULTADO(estado, acción)
        valor ← min(valor, MINIMAX-MAX(problema, sucesor)
    return valor
'''

