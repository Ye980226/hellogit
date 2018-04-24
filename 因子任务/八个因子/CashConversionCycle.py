#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    CashConversionCycle=dv.add_formula("CashConversionCycle","ARTDays+InventoryTDays-AccountsPayablesTDays",
	is_quarterly=False,
	add_data=True)
    return CashConversionCycle
