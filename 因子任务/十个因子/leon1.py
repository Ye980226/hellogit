#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':20}
    if not param:
        param = defult_param
    
    leon1=dv.add_formula("leon1","Corr(Abs(close_adj-high_adj),high_adj-low_adj,%s)"%param['t1'],
	add_data=True,
	is_quarterly=False)
    
    return leon1
