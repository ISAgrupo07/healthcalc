from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl


@given('que introduzco una altura de {altura} cm')
def step_altura_cm(context, altura):
    context.altura_cm = float(altura)

@given('un género "{genero}"')
def step_genero(context, genero):
    context.genero = genero

@when('calculo el IBW')
def step_calcular_ibw(context):
    try:
        calc = HealthCalcImpl()
        context.resultado = calc.ibw(context.altura_cm, context.genero)
    except Exception:
        context.resultado = "error"

@then('el peso ideal debe ser {esperado:f}')
def step_resultado_ibw(context, esperado):
    assert round(context.resultado, 2) == round(esperado, 2)