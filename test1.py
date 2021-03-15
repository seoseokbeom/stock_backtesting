from TQQQ_UVXY_MDD import MDDGraph_one, MDDGraph_tow_combination
from datetime import date, timedelta, datetime
from getPortfolioGraph import getGraph, getGraphWithMdd

# print((datetime.now() - timedelta(1)).strftime('%Y-%m-%d'))
# MDDGraph_one('QQQ')
# MDDGraph_one('QQQ')
# MDDGraph_tow_combination('QQQ', 'UVXY', title='QQQ, UVXY 9:1')
# MDDGraph_one('TQQQ')
# MDDGraph_tow_combination('TQQQ', 'UVXY', title='TQQQ, UVXY 9:1')
# MDDGraph_tow_combination('TQQQ', 'UVXY', title='TQQQ, UVXY 8:2', ratio=(8, 2))
# MDDGraph_one('FNGU')
# MDDGraph_tow_combination('FNGU', 'UVXY', title='FNGU, UVXY 9:1')
# MDDGraph_tow_combination('FNGU', 'UVXY', title='FNGU, UVXY 8:2', ratio=(8, 2))

# getGraph(['FNGU', 'BTC-USD',  ['FNGU', 'BTC-USD', (8, 2)]])
# MDDGraph_tow_combination(
#     'FNGU', 'BTC-USD', title='FNGU, BTC-USD 8:2', rebalencing_ratio=(8, 2))

# getGraph(['FNGU', 'UVXY',  ['FNGU', 'UVXY', (8, 2)]])
# MDDGraph_tow_combination(
#     'FNGU', 'UVXY', title='FNGU, UVXY 8:2', rebalencing_ratio=(8, 2))
# getGraph(['FNGU',  ['FNGU', 'UVXY', (8, 2)]])
# getGraph(['FNGU', 'VIXM', ['FNGU', 'VIXM', (8, 2)]], Start="2020-07-01")
# getGraphWithMdd(
#     ['FNGU', 'UVXY',  ['FNGU', 'UVXY', (8, 2)]], Start="2019-01-01")
# getGraphWithMdd(
#     ['FNGU', 'GME',  ['FNGU', 'GME', (9, 1)]], Start="2021-01-01")
# getGraphWithMdd(
#     ['FNGU', 'BTC-USD', ['FNGU', 'BTC-USD', (5, 5)]], Start="2019-01-01")
getGraphWithMdd(
    ['FNGU', 'QQQ', ['FNGU', 'UVXY', (8, 2)]], Start="2018-02-01")
# getGraph(['VIXM'])
# getGraph(['FNGU'])
# MDDGraph_tow_combination(
#     'FNGU', 'VIXM', title='FNGU, VIXM 8:2', rebalencing_ratio=(8, 2))

# x = []
# for i, v in enumerate(['QQQ', 'SPY']):
#     x.append('tmpstring{}'.format(v))
# print(x)
# print(9/10)
