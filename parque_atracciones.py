from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Visitante:
    nombre: str
    edad: int
    altura: int
    dinero: int
    tickets: List[str] = field(default_factory=list)
    
    def __init__(self, nombre: str, edad: int, altura: int, dinero: int, tickets: list["Ticket"] = [])->None:
        self.nombre: nombre
        self.edad: edad
        self.altura: altura
        self.dinero: dinero
        self.tickets: tickets
        
    def comprar_ticket(self, atraccion)->None:
        if atraccion.estado != True:
            return print(f"La atracción {atraccion.nombre} se encuentra en mantenimiento.")
        
        if hasattr(atraccion, 'verificar_restricciones') and not atraccion.verificar_restricciones(self):
            print(f"El usuario no puede comprar el ticket para la atracción {atraccion.nombre}, no cumple con las condiciones.")

        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(len(self.tickets) + 1, atraccion.nombre)
            self.tickets.append(ticket)
            atraccion.ticket_vendido()
            print(f"Visitante:{self.nombre} compró ticket para {atraccion.nombre}.")
        else:
            print(f"Visitante:{self.nombre} no tiene dinero suficiente para ticket de la atracción: {atraccion.nombre}.")

    
    def entregar_ticket(self, atraccion)->None:
         for ticket in self.tickets:
            if ticket.atraccion == atraccion.nombre:
                self.tickets.remove(ticket)
                print(f"Visitante:{self.nombre} entregó un ticket, Atracción elegida:{atraccion.nombre}.")

    
    def hacer_cola(self, atraccion)->None:
        if hasattr(atraccion, 'verificar_restricciones') and not atraccion.verificar_restricciones(self):
            print(f"Visitante:{self.nombre} no cumple con las condiciones para: {atraccion.nombre}.")

        if self in atraccion.cola:
            print(f"Visitante:{self.nombre}, Atracción actual:{atraccion.nombre}.")

        if self.entregar_ticket(atraccion):
            atraccion.cola.append(self)
            print(f"Visitante:{self.nombre} está en cola de:{atraccion.nombre}.")


    
@dataclass
class Atraccion:
    nombre: str
    capacidad: int
    duracion: int
    estado: bool
    cola: List[str] = field(default_factory=list)
    
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool=True, cola: list["Visitante"]=[])->None:
        self.nombre: nombre
        self.capacidad: capacidad
        self.duracion: duracion
        self.estado: estado
        self.cola: cola
        
    def iniciar_ronda(self)->None:
        if self.estado != True:
            print(f"{self.nombre} no se encuentra disponible.")
        
        if not self.cola:
            print(f"No hay visitantes en la cola para la atracción {self.nombre}.")


    def registrar_ticket_vendido(self) -> None:
        self.tickets_vendidos += 1

    
    def comenzar_mantenimiento(self)->None:
        self.estado = False
        print(f"La atracción:{self.nombre} está fuera de servicio por mantenimiento, vuelva más tarde.")

    
    def finalizar_mantenimiento(self)->None:
        self.estado = True
        print(f"La atracción:{self.nombre} vuelve a estar activa, recuerde subir con cuidado.")

@dataclass   
class Ticket:
    numero: int
    atraccion: str
    precio: int
    fecha_compra: datetime
    
    def __init__(self, numero: int, atraccion: str, precio: int, fecha_compra: datetime)->None:
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra.datetime.now()

@dataclass        
class Parque:
    nombre: str
    juegos: List[str] = field(default_factory=list)
    
    def __ini__(self, nombre: str, juegos: list["Atraccion"]=[])->None:
        self.nombre = nombre
        self.juegos = juegos
        
    def consultar_juegos_activos(self)->None:
        return [juego.nombre for juego in self.juegos if juego.estado == True]
    
    def cobrar_ticket(self, visitante:Visitante, atraccion:Atraccion)->None:
        if visitante.dinero >= atraccion.precio:
            visitante.comprar_ticket(atraccion)
        else:
            print(f"No le alcanza el dinero para entrar en: {atraccion.nombre}.")
            
    def resumen_de_ventas(self, dia: datetime)->None:
        ingresos_T: int = 0
        print("Ventas en el dia")
        
        for juego in self.juegos:
            ganado = juego.tickets_vendidos * juego.precio
            ingresos_T += ganado
            print(f"El {juego.nombre} recaudó el final del día: {juego.tickets_vendidos} - {ganado}")
        
        print(f"Ingresos totales del día: ${ingresos_T}")
        
@dataclass
class AtraccionInfantil(Atraccion):
    def verificar_restricciones(self, visitante: Visitante) -> bool:
        if visitante.edad <= 10:
            return True
        else:
            print(f"Visitante: {visitante.nombre} tiene más de 10 años, por ende no puede subir a: {self.nombre}.")
            return False

@dataclass
class MontañaRusa(Atraccion):
    velocidad_maxima: int
    altura_maxima: int
    extension: int
    
    def _init_(self, nombre: str, capacidad: int, duracion: int, precio: float, velocidad_maxima: int, altura_maxima: int, extension: int) -> None:
        super()._init_(nombre, capacidad, duracion, precio)
        self.velocidad_maxima: velocidad_maxima
        self.altura_maxima: altura_maxima
        self.extension: extension

    def verificar_restricciones(self, visitante: Visitante) -> bool:
        if visitante.altura >= 140:
            return True
        else:
            print(f"Visitante:{visitante.nombre} no tiene estatura requerida, mide menos de 140 cm, no puede subir a: {self.nombre}.")
            return False



    

        