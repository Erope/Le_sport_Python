from login_info import *
from sign import *
from run import *
from wxpusher import *
info = {}
selfinfo = {}
def menu():
    print('1. 查看活动列表')
    print('2. 报名活动')
    print('3. 抢占活动')
    print('4. 学生签到')
    print('5. 活动GPS状态')
    print('6. 签到活动')
    print('7. 速跑(不建议使用)')
    print('8. 正常跑')
    print('9. 补签昨日(非常危险)')


if __name__ == '__main__':
    info = login()
    print('欢迎您，' + info['data']['profile']['realname']+'\n请遵守学校相关规定，此程序仅供学习研究，感谢您的使用。')
    config_header_get['authorization'] = 'Bearer ' + info['data']['token']
    config_header_post['authorization'] = 'Bearer ' + info['data']['token']
    selfinfo = self_info()
    print('您来自: ' + selfinfo['data']['organizationName'])
    q = True
    while q:
        menu()
        choice = input()
        if choice == '1':
            act_list = get_act_list()
            show_act_list_info(act_list)
        elif choice == '2':
            print('请输入活动ID，多个请按,分割')
            id = input()
            sign_act(id,False)
        elif choice == '3':
            print('请输入活动ID，多个请按,分割')
            id = input()
            sign_act(id,True)
        elif choice == '4':
            show_today_act(today_act())
        elif choice == '5':
            print('请输入活动ID')
            id = input()
            show_gps_info(get_act_gps_info(int(id)))
        elif choice == '6':
            print('请输入活动ID')
            id = input()
            act_sign_gps(id, True)
        elif choice == '7':
            print('速跑开始')
            r_text = start()
            end(r_text)
        elif choice == '8':
            print('跑步开始')
            print('将会延迟：{} 秒后提交跑步结果'.format(config_Rundelay))
            r_text = start()
            sleep(config_Rundelay)
            end(r_text)
        elif choice == '9':
            print('速跑开始')
            r_text = start()
            end(r_text, True)
    # 暂时不测试获取活动id，直接指定