
Feature: NEWS2 score calculation
  As usuario
  I want calcular la puntuación NEWS2 de un paciente
  So that medir el deterioro fisiológico del paciente  

  Background:
    Given la calculadora clínica está iniciada

  @EdgeCase
  Scenario Outline: Verificación de múltiples cálculos con valores en puntos límite 
    Given que el paciente tiene una frecuencia respiratoria de <respiración> rpm
    And una saturación de oxígeno del <saturación> % 
    And el uso de soporte de oxígeno es <o2_suplemento>
    And una presión arterial sistólica de <presión_sis> mmHg
    And una frecuencia cardíaca de <pulso> lpm
    And el nivel de consciencia es "<consciencia>"
    And la temperatura corporal es de <temperatura> ºC
    When calculo la puntuación NEWS2
    Then el resultado debe ser <valor>

    Examples:
      | respiración | saturación | o2_suplemento | presión_sis | pulso | consciencia | temperatura | valor | nota                         |
      | 8           | 96         | false         | 115         | 70    | alerta      | 37.0        | 3     | Respiración <= 8 (+3)        |
      | 25          | 96         | false         | 115         | 70    | alerta      | 37.0        | 3     | Respiración >= 25 (+3)       |
      | 12          | 91         | false         | 115         | 70    | alerta      | 37.0        | 3     | Saturación <= 91 (+3)        |
      | 12          | 96         | true          | 115         | 70    | alerta      | 37.0        | 2     | Oxígeno suplementario (+2)   |
      | 12          | 96         | false         | 90          | 70    | alerta      | 37.0        | 3     | Tensión Sis <= 90 (+3)       |
      | 12          | 96         | false         | 220         | 70    | alerta      | 37.0        | 3     | Tensión Sis >= 220 (+3)      |
      | 12          | 96         | false         | 115         | 40    | alerta      | 37.0        | 3     | Pulso <= 40 (+3)             |
      | 12          | 96         | false         | 115         | 131   | alerta      | 37.0        | 3     | Pulso >= 131 (+3)            |
      | 12          | 96         | false         | 115         | 70    | cvpu        | 37.0        | 3     | Consciencia CVPU (+3)        |
      | 12          | 96         | false         | 115         | 70    | alerta      | 35.0        | 3     | Temperatura <= 35.0 (+3)     |
      | 12          | 96         | false         | 115         | 70    | alerta      | 39.1        | 2     | Temperatura > 39.0 (+2)      |
  
  @ErrorHandling
  Scenario Outline: Intento de cálculo con valores fuera de rangos biológicos para parámetros de NEWS2
    Given el valor de entrada de la métrica <metrica> es <valor>
    When calculo la puntuación NEWS2
    Then el sistema debe lanzar una excepción

    Examples:
      | metrica                 | valor  |
      | frecuencia respiratoria | -1     |
      | frecuencia respiratoria | 101    |
      | saturación oxígeno      | 105    |
      | presión sistólica       | 450    |
      | frecuencia cardíaca     | 350    |
      | temperatura             | 15     |
      | temperatura             | 55     |

  
  Scenario Outline: Verificación de múltiples cálculos exitosos 
    Given que el paciente tiene una frecuencia respiratoria de <respiración> rpm
    And una saturación de oxígeno del <saturación> % 
    And el uso de soporte de oxígeno es <o2_suplemento>
    And una presión arterial sistólica de <presión_sis> mmHg
    And una frecuencia cardíaca de <pulso> lpm
    And el nivel de consciencia es "<consciencia>"
    And la temperatura corporal es de <temperatura> ºC
    When calculo la puntuación NEWS2
    Then el resultado debe ser <valor>

    Examples:
        | respiración | saturación | o2_suplemento | presión_sis | pulso | consciencia | temperatura | valor |
        | 15          | 98         | False         | 120         | 75    | alert       | 37.0        | 0     |
        | 26          | 90         | True          | 80          | 140   | cvpu        | 34.0        | 20    |
        | 22          | 94         | False         | 105         | 115   | alert       | 37.0        | 6     |
        | 10          | 92         | False         | 95          | 45    | alert       | 35.5        | 7     |
        | 13          | 100        | False         | 200         | 100   | alert       | 38.5        | 2     |

        