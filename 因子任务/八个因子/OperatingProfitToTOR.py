#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    OperatingProfitToTOR=dv.add_formula("OperatingProfitToTOR_J","TTM(oper_profit)/TTM(oper_rev)"
	,is_quarterly=True
	,add_data=True)
    return OperatingProfitToTOR