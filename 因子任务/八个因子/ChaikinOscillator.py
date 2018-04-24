#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':3,'t2':10,'t3':10,'t4':6}
    if not param:
        param = defult_param
    
    ChaikinOscillator=dv.add_formula("ChaikinOscillator_J","(Ewma(AD,%s)-Ewma(AD,%s))/Pow(%s,%s)"%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
    return ChaikinOscillator
