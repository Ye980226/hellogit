#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5}
    if not param:
        param = defult_param
    
    leon6=dv.add_formula("leon6","-1*Corr(Standardize(volume),Standardize(close_adj),%s)"%(param['t1']),
	add_data=True,
	is_quarterly=False)
    
    return leon6
