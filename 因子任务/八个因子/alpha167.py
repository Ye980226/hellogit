# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 12} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    如果今天收盘价大于前一天收盘价，取值为今天收盘价与前一天收盘价的差，否则取0，将值按12天移动加总
    """
    alpha167 = dv.add_formula('alpha167', "Ts_Sum(If((close_adj-Delay(close_adj,1))>0,close_adj-Delay(close_adj,1),0),%s)"%(params['t1']),
        is_quarterly=False, add_data=True)
    return alpha167
