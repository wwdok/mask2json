'''
lanhuage: python
Descripttion:  config read and write test
version: beta
Author: xiaoshuyui
Date: 2020-10-20 10:29:26
LastEditors: xiaoshuyui
LastEditTime: 2020-10-20 10:41:53
'''
import sys
sys.path.append('..')

import convertmask.utils.methods.configUtils as ccfg

print(ccfg.config_ROOT)

if __name__ == "__main__":
    cfg = ccfg.cfp
    print(cfg.sections())
    print(ccfg.getConfigParam(cfg,'log','show'))

