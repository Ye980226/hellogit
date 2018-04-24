#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5,'t3':5,'t4':5}
    if not param:
        param = defult_param
    
    leon8=dv.add_formula("leon8","-1*Rank(close_adj - Max(low_adj, Delay(low_adj,%s)))*Rank(Corr((Ts_Mean(volume,%s)),Ts_Mean(close_adj,%s), %s))"%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
    return leon8
