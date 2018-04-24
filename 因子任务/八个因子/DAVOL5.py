#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5}
    if not param:
        param = defult_param
    
    DAVOL5=dv.add_formula("leon1","VOL%s-VOL120"%param['t1'],
	add_data=True,
	is_quarterly=False)
    
    return DAVOL5
