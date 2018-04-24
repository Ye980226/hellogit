#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':2,'t2':2,'t3':8}
    if not param:
        param = defult_param
    
    leon9=dv.add_formula("leon9","-1*Correlation(Rank(Ts_Mean(vwap,%s)),Rank(Ts_Mean((high_adj-low_adj)/2,%s)),%s)"%(param['t1'],param['t2'],param['t3']),
	add_data=True,
	is_quarterly=False)
    
    return leon9
