from parque_atracciones import Visitante, Atraccion, Ticket, Parque, AtraccionInfantil, MontañaRusa
from dataclasses import dataclass, field
from typing import List

def main():
    visitante= [
        Visitante(nombre="Diana", edad=20, altura=165, dinero=10000, tickets=[0]),
        Visitante(nombre="Liam", edad=15, altura=170, dinero=5000, tickets=[0]),
        Visitante(nombre="Hugo", edad=8, altura=120, dinero=9000, tickets=[0])
    ]
    atracciones=[ 
        Atraccion(nombre="AutosLocos", capacidad=10, duracion=10, estado=True, cola=[0]),
        Atraccion(nombre="CasaEmbrujada", capacidad=3, duracion=20, estado=True, cola=[0]),
        Atraccion(nombre="TobogandeAgua", capacidad=15, duracion=8, estado=True, cola=[0])
    ]
