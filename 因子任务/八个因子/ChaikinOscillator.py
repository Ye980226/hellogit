# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1':3,'t2':10,'t3':10,'t4':6} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1':'暂无','t2':'暂无','t3':'暂无','t4':'暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}
    
def run_formula(dv, params = default_params):
	'''
	佳庆指标，该指标基于AD曲线的指数移动均线计算得到
	'''
	ChaikinOscillator=dv.add_formula("ChaikinOscillator_J","(Ewma(AD,%s)-Ewma(AD,%s))/Pow(%s,%s)"%(param['t1'],param['t2'],param['t3'],param['t4']),
	add_data=True,
	is_quarterly=False)
    
	return ChaikinOscillator
