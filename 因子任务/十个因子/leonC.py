# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 3, 't2': 20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    三日的移动平均换手率的20日简单移动平均的值取相反数
    """
    leonC = dv.add_formula('leonC', "-1*Sma(Ts_Mean(turnover_ratio,%s),%s,1)"%(params['t1'],params['t2']),
        is_quarterly=False, add_data=True)
    return leonC
