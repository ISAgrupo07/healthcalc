from behave import then

@then('se muestra un error')
def step_error(context):
    assert context.resultado == "error"