class NoHaySaldoException(Exception):
    pass 

class UsuarioDesactivadoException(Exception):
    pass
    
class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
    
DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}


PRECIO_TICKET = 70
DESACTIVADO = "desactivado"
ACTIVADO = "activado"
    


class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    
    def obtener_precio_ticket(self):
        precio_total = PRECIO_TICKET
        if self.grupo_beneficiario is not None:
            descuento = DESCUENTOS[self.grupo_beneficiario] 
            precio_total = PRECIO_TICKET - ((PRECIO_TICKET * descuento)/100)
        return int(precio_total)
    
    def pagar_pasaje(self):
        ticket = self.obtener_precio_ticket()
        if self.saldo < ticket:
            raise NoHaySaldoException()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        self.saldo = self.saldo - ticket
        return self.saldo

    def cambiar_estado(self, estado):
        if estado != DESACTIVADO and estado != ACTIVADO:
            raise EstadoNoExistenteException()
        self.estado = estado
