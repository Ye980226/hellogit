# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    最高价减去20天前的最低价加上最高价减去当天的最低价的和除以2然后取相反数
    """
    leon5 = dv.add_formula('leon5', "-1*(high_adj-Delay(low_adj,%s)+(high_adj-low_adj))/2"%(params['t1']),
        is_quarterly=False, add_data=True)
    return leon5
