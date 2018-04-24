#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':0,'t4':12}
    if not param:
        param = defult_param
    
    alpha167=dv.add_formula('alpha167','Ts_Sum(If(close_adj-Delay(close_adj,%s)>0,close_adj-Delay(close_adj,%s),%s),%s)'%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
    return alpha167
