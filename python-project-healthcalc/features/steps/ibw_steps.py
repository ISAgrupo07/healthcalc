from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.patient import Patient
from healthcalc.gender import Gender


@given('que introduzco una altura de {altura} cm')
def step_altura_cm(context, altura):
    context.altura_cm = float(altura)

@given('un género "{genero}"')
def step_genero(context, genero):
    if genero.lower() in ("hombre", "man", "m", "h"):
        context.genero = Gender.MALE
    elif genero.lower() in ("mujer", "woman", "w", "f"):
        context.genero = Gender.FEMALE
    else:
        context.genero = genero

@when('calculo el IBW')
def step_calcular_ibw(context):
    try:
        calc = HealthCalcImpl()
        persona = Patient(0.0, context.altura_cm / 100.0, context.genero, 30)
        context.resultado = calc.ibw(persona)
    except Exception:
        context.resultado = "error"

@then('el peso ideal debe ser {esperado:f}')
def step_resultado_ibw(context, esperado):
    assert round(context.resultado, 2) == round(esperado, 2)