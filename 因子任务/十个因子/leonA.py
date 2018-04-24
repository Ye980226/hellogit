#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':2,'t3':3,'t4':10}
    if not param:
        param = defult_param
    
    leonA=dv.add_formula("leonA","-1*Corr(Standardize(volume),Standardize((Ts_Mean(close_adj,%s)+Ts_Mean(close_adj,%s)+Ts_Mean(close_adj,%s))/3),%s)"%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
    return leonA
