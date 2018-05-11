# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params = default_params):
	'''
	现金转换周期
	'''
	CashConversionCycle=dv.add_formula("CashConversionCycle","ARTDays+InventoryTDays-AccountsPayablesTDays",
	is_quarterly=False,
	add_data=True)
	return CashConversionCycle
