import numpy as np
import pandas as pd
import msvcrt
data=pd.read_csv('./data/ershoufang.csv',sep=',',header=0,encoding='utf-8')

# 用于程序在数据处理输出信息后暂停，方便用户观察
def return2main():
    print("               按任意键返回                          ")
    msvcrt.getwche()

#输入参数：地区信息（中文）
#输出参数： 无
#用途： 用于获取某个地区的二手房均价和单价均价
def avg_price_ershoufang(area_choose):
    global data
    data_ = data[data["地区"].isin([area_choose])]
    #print(data_)
    totalErshoufang = np.array(data_['总价'])
    priceErshoufang = np.array(data_['单价'])
    avgTotalErshoufang = np.average(totalErshoufang,keepdims=False)
    avgPriceErshoufang = np.average(priceErshoufang,keepdims=False)

    print(f"该地区的二手房总价均价为:{avgTotalErshoufang:.2f}万元")
    print(f"该地区的二手房单价均价为:{avgPriceErshoufang:.2f}万元")

    return2main()

#输入参数：data：在整体data上截取指定地区后的data huxingChoose: 用户选择的户型 huxingErshoufang: 该户型所有的二手房信息
#输出参数 hxCount：该户型在该地区的总数，mpCount：该户型装修为毛坯类型的个数,jianzCount：该户型装修为简装类型的个数,jingzCount：该户型装修为精装类型的个数
#用途：用于统计某户型的装修信息和指定户型信息
def zhuangxiu_percent(data,huxingChoose,huxingErshoufang):
    #data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8')
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

#输入参数：地区信息（中文）
#输出参数： 无
#用途：用于分析指定户型在该地区的信息
def huxing_percent(area_choose):
    #data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8')
    global data
    data_ = data[data["地区"].isin([area_choose])]
    huxingErshoufang = np.array(data_['户型'])
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
        hxCount,mpCount,jianzCount,jingzCount = zhuangxiu_percent(data_,huxingChoose,huxingErshoufang)
        
    huxingErshoufang[huxingErshoufang != huxingChoose] = 0
    huxingErshoufang[huxingErshoufang == huxingChoose] = 1 
    percent = np.sum(huxingErshoufang,keepdims=False) * 1.0 / huxingErshoufang.shape[0]
    print(f"该户型在该地区占比{percent:.2f}",end = ",")
    print(f"该户型在该地区共有{hxCount}套,其中毛坯房有{mpCount}套,简装房有{jianzCount}套,精装房有{jingzCount}套")
    return2main()

#输入参数：hx：用户指定的户型，data：数据 totalNum：该户型总共在该地区的数量
#输出参数：输出该户型在该地区的单价平均值
#用途：用于输出该户型在该地区的单价平均值

def ershoufang_hx_danjia(hx,data,totalNum):
    dataHuxing = data["户型"]
    dataPrice = data["单价"]
    danjiaAvg = 0

    for Huxing,Price in zip(dataHuxing,dataPrice):
        if Huxing == hx:
            danjiaAvg += Price

    return danjiaAvg * 1.0 / totalNum

#输入参数：hxChoose：用户指定的户型，data：数据
#输出参数：输出该户型在该地区前10关注度的链接
#用途：用于输出该户型在该地区前10关注度的链接
def ershoufang_top10_url_print(hxChoose,data):
    dataHxs = data["户型"]
    dataAttentions = data["关注度"]
    dataUrls = data["链接"]

    attentions = []
    Urls = [] 
    topUrls = []

    for hx,attention,url in zip(dataHxs,dataAttentions,dataUrls):
        if hx == hxChoose:
            attentions.append(attention)
            Urls.append(url)

    iters = 10 if len(Urls) >= 10 else len(Urls)

    for iter in range(iters):
        index = attentions.index(max(attentions))
        topUrls.append(Urls[index])
        attentions.pop(index)
        Urls.pop(index)
    
    return topUrls,iters

#输入参数：area_choose：用户选择的地区
#输出参数：无
#用途：用于分析该地区的关注度信息，得到平均关注度和关注度最高的单价平均值

def hot_huxing_analsy(area_choose):
    #data=pd.read_csv('./chongming.csv',sep=',',header=0,encoding='utf-8',index_col=None)
    global data
    data_ = data[data["地区"].isin([area_choose])]
    dataHuxing = data_["户型"]
    dataAttention = data_["关注度"]
    huxing_types = np.unique(dataHuxing)
    hxCountAll = []
    dataAttentionAvgAll = []

    for huxing_type in huxing_types:
        hxCount = 0
        dataAttentionAvg = 0
        for huxing,attention in zip(dataHuxing,dataAttention):
            if huxing == huxing_type:
                hxCount += 1
                dataAttentionAvg += attention
        if hxCount == 0:
            dataAttentionAvg = -1
        else : 
            dataAttentionAvg = dataAttentionAvg * 1.0 / hxCount
        dataAttentionAvgAll.append(dataAttentionAvg)
        hxCountAll.append(hxCount)

    attentionHotest = max(dataAttentionAvgAll)
    hxCountHotest = hxCountAll[dataAttentionAvgAll.index(max(dataAttentionAvgAll))]
    hxHotest = None

    for attentionAvg,hx,hxCount in zip(dataAttentionAvgAll,huxing_types,hxCountAll):
        if attentionAvg != -1:
            print(f"该地区{hx}户型平均关注度为{attentionAvg:.2f},该地区共有{hxCount}个该户型")
        else :
            print(f"该地区{hx}户型暂时没有,您可以关注其他地区相应房型或者关注该地区其他房型")
        if attentionAvg == attentionHotest:
            hxHotest = hx

    hotestHxPriceAvg = ershoufang_hx_danjia(hxHotest,data_,hxCountHotest)
    hotestTopAttentionUrls,nums = ershoufang_top10_url_print(hxHotest,data_)

    print(f"其中,{hxHotest}户型关注度最高,其在该地区的单价平均值为{hotestHxPriceAvg:.2f}元,为您列举了该户型{nums}个关注度最高的二手房链接:")
    for url in hotestTopAttentionUrls:
        print(url)
    return2main()

# huxing_percent()