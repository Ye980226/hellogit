#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):

    ARTRate = dv.add_formula("ARTRate_J","TTM(oper_rev)/Ts_Mean(acct_rcv+notes_rcv-adv_from_cust,4)",
			add_data=True,
           is_quarterly=False)
    
    return ARTRate
