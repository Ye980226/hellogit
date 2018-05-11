# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    如果开盘价小于前一天开盘价，取开盘价和最低价差与开盘价和前一天开盘价的差的最大值否则取0，然后移动加总20天的值
    """
    SBM = dv.add_formula('SBM', "Ts_Sum(If(open<Delay(open,1),Max(open-low,open-Delay(open,1)),0),%s)"%(params['t1']),
        is_quarterly=False, add_data=True)
    return SBM
