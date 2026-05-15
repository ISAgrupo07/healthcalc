Feature: Cálculo del peso corporal ideal (IBW)

  Como usuario
  Quiero calcular mi peso corporal ideal (IBW)
  Para tener una referencia de peso saludable

  Scenario: Cálculo correcto para un hombre
    Given que introduzco una altura de 180 cm
    And un género "hombre"
    When calculo el IBW
    Then el peso ideal debe ser 72.5

  Scenario: Cálculo correcto para una mujer
    Given que introduzco una altura de 165 cm
    And un género "mujer"
    When calculo el IBW
    Then el peso ideal debe ser 57.5

  Scenario: Altura por debajo del rango válido
    Given que introduzco una altura de 25 cm
    And un género "hombre"
    When calculo el IBW
    Then se muestra un error

  Scenario: Altura por encima del rango válido
    Given que introduzco una altura de 350 cm
    And un género "mujer"
    When calculo el IBW
    Then se muestra un error

  Scenario: Altura igual a cero
    Given que introduzco una altura de 0 cm
    And un género "hombre"
    When calculo el IBW
    Then se muestra un error

  Scenario: Género no reconocido
    Given que introduzco una altura de 170 cm
    And un género "otro"
    When calculo el IBW
    Then se muestra un error
