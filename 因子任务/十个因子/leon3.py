#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':20}
    if not param:
        param = defult_param
    
    leon3=dv.add_formula("leon3","-1*(high_adj-Delay(low_adj,%s)+(high_adj-low_adj))/2"%(param['t1']),
	add_data=True,
	is_quarterly=False)
    
    return leon3
