# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    标准化的成交量和标准化的收盘价的5日相关系数取相反数
    """
    leon6 = dv.add_formula('leon6', "-1*Corr(Standardize(volume),Standardize(close_adj),%s)"%(params['t1']),
        is_quarterly=False, add_data=True)
    return leon6
