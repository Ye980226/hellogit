# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}
 
def run_formula(dv, params = default_params):
	'''
	应收账款周转率
	'''
	ARTRate = dv.add_formula("ARTRate_J","TTM(oper_rev)/Ts_Mean(acct_rcv+notes_rcv-adv_from_cust,4)",add_data=True,is_quarterly=False)
    
	return ARTRate
