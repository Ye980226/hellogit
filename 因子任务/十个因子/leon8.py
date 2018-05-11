# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 5, 't2': 5, 't3': 5, 't4': 5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无', 't3': '暂无', 't4': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    收盘价减去最低价与前五日最低价的最大值的排序乘上成交量五日平均和收盘价五日平均的五日相关系数的排序，然后取相反数
    """
    leon8 = dv.add_formula('leon8', "-1*Rank(close_adj - Max(low_adj, Delay(low_adj,%s)))*Rank(Corr((Ts_Mean(volume,%s)),Ts_Mean(close_adj,%s), %s))"%(params['t1'],params['t2'],params['t3'],params['t4']),
        is_quarterly=False, add_data=True)
    return leon8
