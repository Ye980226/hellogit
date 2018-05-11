# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = 'leon' # 这里填下你的名字
default_params = {'t1': 5, 't2': 5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {'t1': '暂无', 't2': '暂无'} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    排序后的收盘价和排序后的成交量的5日的相关系数加上排序后的开盘价和排序后的成交量的5日的相关系数之后的和，进行排序然后再除以2，取平均数，然后取相反数
    """
    leon7 = dv.add_formula('leon7', "Rank((Corr(Rank(close_adj), Rank(volume), %s))+(Corr(Rank(open_adj), Rank(volume), %s)))* -0.5"%(params['t1'],params['t2']),
        is_quarterly=False, add_data=True)
    return leon7
