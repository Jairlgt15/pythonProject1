# Created by JairG at 2/7/2022
# language:es

  Característica: Transferencia bancaria
    Como titular de una cuenta bancaria, deseo realizar una transferencia local segura
    para aumentar la confianza del banco
  Esquema del escenario: Transferencia entre cuentas del mismo banco
    Dado que Miguel tiene una cuenta de ahorros con <saldo_origen_inicial> dólares de saldo
    Y que Gabriel tiene otra cuenta de ahorros con <saldo_destino_inicial> dólares de saldo
    Cuando Miguel transfiere un monto de <monto> dólares a Gabriel
    Entonces Miguel tendrá <saldo_origen_final> dólares de saldo
    Y Gabriel tendrá <saldo_destino_final> dólares de saldo
    Ejemplos:
      | saldo_origen_inicial| saldo_destino_inicial | monto|saldo_origen_final | saldo_destino_final|
      | 100.00 | 10.00 | 50.00 | 50.00 | 60.00 |
      | 10.00 | 10.00 | 50.00 | 10.00 | 10.00 |
      |100.00 |10.00  |50.00  |49.00  |10.00  |






