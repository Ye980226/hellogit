#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':2,'t3':20,'t4':2}
    if not param:
        param = defult_param
    
    leon4=dv.add_formula("leon4","((low_adj-Sma(open_adj,%s,%s))-(high_adj-Sma(open_adj,%s,%s)))/open_adj"%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
    return leon4
