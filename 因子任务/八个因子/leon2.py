# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 10, 't2': 10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    收盘价减去10日移动平均的收盘价除以10日移动平均的收盘价乘100然后取相反数
    """
    leon2 = dv.add_formula('leon2', "-1*(close_adj-Ts_Mean(close_adj,%s))/Ts_Mean(close_adj,%s)*100"%(params['t1'],params['t2']),
        is_quarterly=False, add_data=True)
    return leon2
