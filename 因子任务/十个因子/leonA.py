# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 1, 't2': 2, 't3': 3, 't4': 10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无', 't3': '暂无', 't4': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    标准化的成交量与标准化的收盘价的1日2日3日的移动平均的和除以3的10天的相关系数
    """
    leonA = dv.add_formula('leonA', "-1*Corr(Standardize(volume),Standardize((Ts_Mean(close_adj,%s)+Ts_Mean(close_adj,%s)+Ts_Mean(close_adj,%s))/3),%s)"%(params['t1'],params['t2'],params['t3'],params['t4']),
        is_quarterly=False, add_data=True)
    return leonA
