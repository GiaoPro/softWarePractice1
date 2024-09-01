import numpy as np
import pandas as pd

def avg_price_ershoufang():
    data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8')
    avgPriceErshoufang = np.array(data['总价'])
    return np.average(avgPriceErshoufang,keepdims=False)

def zhuangxiu_percent(huxingChoose,huxingErshoufang):
    data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8')
    ZXErshoufang = np.array(data['装修'])
    mpCount = 0
    jianzCount = 0
    jingzCount = 0
    hxCount = 0
    for huxing,ZX in zip(huxingErshoufang,ZXErshoufang):
        if huxing == huxingChoose:
            hxCount += 1
            if ZX == "毛坯":
                mpCount += 1
            elif ZX == "简装":
                jianzCount += 1
            elif ZX == "精装":
                jingzCount += 1
    return hxCount,mpCount,jianzCount,jingzCount

def huxing_percent():
    data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8')
    huxingErshoufang = np.array(data['户型'])
    huxing_types = np.unique(huxingErshoufang)
    print("该地区包含以下户型:",end=" ")
    for huxing_type in huxing_types:
        print(huxing_type ,end = ' ')
    print("\n请选择您感兴趣的户型:",end=" ")
    huxingChoose = input()
    print("您是否需要知晓装修信息:(若是请输入是,否则输入否)",end = " ")
    ZXFlag = input()

    assert ZXFlag == '是' or ZXFlag == '否'
    assert np.isin(huxingChoose,huxing_types)

    if ZXFlag == '是':
        hxCount,mpCount,jianzCount,jingzCount = zhuangxiu_percent(huxingChoose,huxingErshoufang)
        print(f"该户型在该地区共有{hxCount}套,其中毛坯房有{mpCount}套,简装房有{jianzCount}套,精装房有{jingzCount}套")

    huxingErshoufang[huxingErshoufang != huxingChoose] = 0
    huxingErshoufang[huxingErshoufang == huxingChoose] = 1 
    percent = np.sum(huxingErshoufang,keepdims=False) * 1.0 / huxingErshoufang.shape[0]

    return percent

def hot_huxing_analsy():
    
    pass
huxing_percent()