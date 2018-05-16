# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 10} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    成交的排列与收盘价的排列取10天的协方差再取相反数
    """
    leon5 = dv.add_formula('leon5', "-1*Covariance(Rank(volume),Rank(close_adj),%s)"%(params['t1']),
        is_quarterly=False, add_data=True)
    return leon5
