#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':0,'t4':20}
    if not param:
        param = defult_param
    
    SBM=dv.add_formula("SBM_J","Ts_Sum(If(open<Delay(open,%s),Max(open-low,open-Delay(open,%s)),%s),%s)"%(param['t1'],param['t2'],param['t3'],param['t4']),
           add_data=True,is_quarterly=False)
    
    return SBM
