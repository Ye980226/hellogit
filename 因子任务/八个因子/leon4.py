# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 20, 't2': 2, 't3': 20, 't4': 2} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无', 't3': '暂无', 't4': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    最低价减去开盘价N取10的指数移动平均减去最高价减去开盘价N取10的指数移动平均的差值除以开盘价
    """
    leon4 = dv.add_formula('leon4', "((low_adj-Sma(open_adj,%s,%s))-(high_adj-Sma(open_adj,%s,%s)))/open_adj"%(params['t1'],params['t2'],params['t3'],params['t4']),
        is_quarterly=False, add_data=True)
    return leon4
