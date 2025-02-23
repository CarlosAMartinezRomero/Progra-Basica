class cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def operar(self, monto):
        if monto: self.saldo += monto if monto > 0 else (self.saldo >= -monto and setattr(self, 'saldo', self.saldo + monto))
        print (f"saldo: {self.saldo}")
        
def main():
    c = cuenta(0)
    while (op := input("Monto (+ depósito, - retiro, 0 salir)")) != "0":
        c.operar(float(op))

main()
