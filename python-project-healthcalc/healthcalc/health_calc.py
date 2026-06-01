from healthcalc.basal_metabolic_index import BasalMetabolicIndex
from healthcalc.ideal_body_weight import IdealBodyWeight
from healthcalc.news2_interface import News2


class HealthCalc(BasalMetabolicIndex, IdealBodyWeight, News2):
    pass
