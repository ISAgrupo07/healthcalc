from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.patient import Patient
from healthcalc.gender import Gender

@given('que introduzco una altura de {altura} metros')
def step_altura(context, altura):
    context.altura = float(altura)

@given('un peso de {peso} kg')
def step_peso(context, peso):
    context.peso = float(peso)

@when('calculo el BMI')
def step_calcular(context):
    try:
        calc = HealthCalcImpl()
        persona = Patient(context.peso, context.altura, Gender.MALE, 30)
        context.resultado = calc.bmi(persona)
    except Exception:
        context.resultado = "error"

@then('el resultado debe ser {esperado:f}')
def step_resultado(context, esperado):
    assert round(context.resultado, 2) == round(esperado, 2)