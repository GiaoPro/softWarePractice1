#! /usr/local/bin/python3
from analyze import Analsy
import os
import sys
import analsy as a
import ershoufang_prediction as module

area_list = ["浦东", "闵行" , "宝山","徐汇" ,"普陀","洋浦" ,"长宁","松江" ,"嘉定"   ,"黄浦"  ,"静安"  ,"虹口" ,"青浦","奉贤" ,"金山" ,"崇明" ]
area_dict = {"宝山" : "baoshan" , "长宁" : "changning" , "崇明" : "chongming" ,"奉贤" : "fengxian" ,
            "虹口" : "hongkou" ,"黄浦" : "huangpu" ,"嘉定" : "jiading" ,"静安" : "jingan" ,
            "金山" : "jinshan" ,"闵行" : "minxing" ,"浦东" : "pudong" ,"普陀" : "putuo" ,
            "青浦" : "qingpu","松江" : "songjiang" ,"徐汇" : "xuhui" ,"洋浦" : "yangpu" }
def restart():
    os.system("python ./main.py") #当前程序所在位置
    sys.exit()  #结束当前程序

def clear_screen():
    os.system("cls") # linux/mac

def area_view(area_choose):
    print(f"              \033[1;36m欢迎来到{area_choose}地区二手房分析预测系统！！\033[0m")
    print("                    \033[0;30m请选择以下服务\033[0m")
    print(f"""
                    \033[1;30m0. 退出{area_choose}地区二手房分析预测系统\033[0m
                    \033[1;30m1. 二手房单价估计\033[0m
                    \033[1;30m2. 该地区二手房均价\033[0m
                    \033[1;30m3. 该地区二手房户型装修/关注度分析\033[0m
                    \033[1;30m4. 对应户型二手房在该地区分析\033[0m
        """)
    print("请输入服务对应编号获取服务:",end = " ")

    type = int(input())

    if type == 0:
        clear_screen()
        view_init()
    elif type == 1:
        clear_screen()
        module.price_pred(area_choose)
        clear_screen()
        area_view(area_choose)
    elif type == 2:
        clear_screen()
        a.avg_price_ershoufang(area_dict[area_choose])
        clear_screen()
        area_view(area_choose)
    elif type == 3:
        clear_screen()
        a.hot_huxing_analsy(area_dict[area_choose])
        clear_screen()
        area_view(area_choose)
    elif type == 4:
        clear_screen()
        a.huxing_percent(area_dict[area_choose])
        clear_screen()
        area_view(area_choose)


def view_init():
    print("              \033[1;36m欢迎来到上海地区二手房分析预测系统！！\033[0m")
    print("                    \033[0;30m请选择您想购买二手房地区\033[0m")
    print("""                                   
                        \033[1;30m浦东 \033[0m\033[1;30m闵行 \033[0m\033[1;30m宝山 \033[0m\033[1;30m徐汇\033[0m
                        \033[1;30m普陀 \033[0m\033[1;30m洋浦 \033[0m\033[1;30m长宁 \033[0m\033[1;30m松江\033[0m
                        \033[1;30m嘉定 \033[0m\033[1;30m黄浦 \033[0m\033[1;30m静安 \033[0m\033[1;30m虹口\033[0m
                        \033[1;30m青浦 \033[0m\033[1;30m奉贤 \033[0m\033[1;30m金山 \033[0m\033[1;30m崇明\033[0m
                                                                        输入 退出 退出系统
        """)

    area_choose = input("在此输入要查询区域：")

    if area_choose not in area_list and area_choose != "退出":
        print("\033[4;31m警告:该区域不在查询范围内\033[0m")
        clear_screen()
        restart()
    elif area_choose != "退出":
        clear_screen()
        area_view(area_choose)
    else:
        exit()

view_init()
Ana = Analsy()
Ana.get_analysis_result()