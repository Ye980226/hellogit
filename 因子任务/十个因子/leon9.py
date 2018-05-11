# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 2, 't2': 2, 't3': 8} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无', 't3': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    平均股价的2日平均的排序值与最高价减去最低价除以2的2日平均的排序值的8日相关系数，然后取相反数
    """
    leon9 = dv.add_formula('leon9', "-1*Correlation(Rank(Ts_Mean(vwap,%s)),Rank(Ts_Mean((high_adj-low_adj)/2,%s)),%s)"%(params['t1'],params['t2'],params['t3']),
        is_quarterly=False, add_data=True)
    return leon9
