# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 5, 't2': 10, 't3': 15} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无', 't3': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    5、10、15季度的每股息税前利润的平均值的和除以3
    """
    leonB = dv.add_formula('leonB', "(Ts_Mean(TTM(ebitps),%s)+Ts_Mean(TTM(ebitps),%s)+Ts_Mean(TTM(ebitps),%s))/3"%(params['t1'],params['t2'],params['t3']),
        is_quarterly=False, add_data=True)
    return leonB
