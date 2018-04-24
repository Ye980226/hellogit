#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    CashEquivalentPS = dv.add_formula("CashEquivalentPS","cash_cash_equ_end_period/capital_stk",
           is_quarterly=False,
           add_data=False)
    return CashEquivalentPS        

