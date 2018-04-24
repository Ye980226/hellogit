#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5}
    if not param:
        param = defult_param
    
    leon7=dv.add_formula("leon7","Rank((Corr(Rank(close_adj), Rank(volume), %s))+(Corr(Rank(open_adj), Rank(volume), %s)))* -0.5"%(param['t1'],param['t2']),
	add_data=True,
	is_quarterly=False)
    
    return leon7
