#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':10,'t2':10}
    if not param:
        param = defult_param
    
    leon2=dv.add_formula("leon2","-1*(close_adj-Ts_Mean(close_adj,%s))/Ts_Mean(close_adj,%s)*100"%(param['t1'],param['t2']),
	add_data=True,
	is_quarterly=False)
    
    return leon2
