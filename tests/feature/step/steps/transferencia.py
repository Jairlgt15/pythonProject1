from behave import *

from src.clases.clasesBancarias import Cliente, CuentaDeAhorros

use_step_matcher("parse")


@step("que Miguel tiene una cuenta de ahorros con {saldo_origen_inicial:f} dólares de saldo")
def step_impl(context, saldo_origen_inicial):
    """
    :type context: behave.runner.Context
    :type saldo_origen_inicial: float
    """
    # Aquí realizamos el análisis.
    # Aquí creamos la petición de métodos que debe tener el sistema (pregunta a mirar video)
    context.clienteOrigen = Cliente("Miguel", CuentaDeAhorros(saldo_origen_inicial))
    # assert context.cliente.listar_saldos_de_cuentas()
    assert (context.clienteOrigen.listar_saldo_cuenta() == saldo_origen_inicial)


@step("que Gabriel tiene otra cuenta de ahorros con {saldo_destino_inicial:f} dólares de saldo")
def step_impl(context, saldo_destino_inicial):
    """
    :type context: behave.runner.Context
    :type saldo_destino_inicial: float
    """

    context.clienteDestino = Cliente("Gabriel", CuentaDeAhorros(saldo_destino_inicial))
    assert context.clienteDestino.listar_saldo_cuenta() == saldo_destino_inicial


@step("Miguel transfiere un monto de {monto:f} dólares a Gabriel")
def step_impl(context, monto):
    """
    :type context: behave.runner.Context
    :type monto: float
    """
    context.clienteOrigen.cuenta.transferir_cuenta(monto, context.clienteDestino)


@step("Miguel tendrá {saldo_origen_final:f} dólares de saldo")
def step_impl(context, saldo_origen_final):
    """
    :type context: behave.runner.Context
    :type saldo_origen_final: float
    """
    assert context.clienteOrigen.listar_saldo_cuenta() == saldo_origen_final


@step("Gabriel tendrá {saldo_destino_final:f} dólares de saldo")
def step_impl(context, saldo_destino_final):
    """
    :type context: behave.runner.Context
    :type saldo_destino_final: float
    """
    assert context.clienteDestino.listar_saldo_cuenta() == saldo_destino_final