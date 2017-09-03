#coding=utf-8
__author__ = 'WyAtu'
import time
import os

#用于计算整个数据串的前4位
def cal_balance(bal):
    str_balance = '%04X' % (bal * 100)
    standard_balcnde = str_balance[2:] + str_balance[0:2]
    print "The money_data is:", standard_balcnde
    return standard_balcnde

#用于计算输入金额的对应数据串的校验位及之后的整个数据串
def cal_check_digit():
    clear = os.system("cls")
    while True:
        try:
            money_number = input('Please input the money:\n')
            top_four_number = cal_balance(money_number)
            data_string = raw_input('Please input the data_string:\n')
            check_string = top_four_number + data_string[4:30]
            container = []
            for n in range(2, len(check_string)+1, 2):
                for i in range(0, len(check_string)):
                    if n-2 <= i < n and i % 2 != 0:
                        container.append(check_string[i-1]+check_string[i])
            sum = 0
            for i in range(len(container)):
                add = int(container[i], 16)
                sum = sum + add
            str_sum = str(hex(sum))
            result_string = check_string + str_sum[-2:]
            print "the result data string is:\n"
            output_box(result_string)
            help()
        except Exception, e2:
            print e2
        else:
            break

#用于输出最后的结果数据串
def output_box(sen):
    screen_width = 60
    text_width = len(sen)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) // 2
    print ' ' * left_margin + '+' + '-' * box_width + '+'
    print ' ' * left_margin + '|' + ' ' * box_width + '|'
    print ' ' * left_margin + '|' + ' ' * 3 + sen + ' ' * 3 +  '|'
    print ' ' * left_margin + '|' + ' ' * box_width + '|'
    print ' ' * left_margin + '+' + '-' * box_width + '+', '\n'

#用于退出
def quit(option):
    if option == 'Q' or option == 'q':
        clear = os.system("cls")
        for num in range(5, 0, -1):
            print ("Thanks for your trust and use!\n"
                   "Written by WyAtu~ Goodbye!")
            if num != 1:
                sec = "seconds..."
            else:
                sec = "second..."
            print "Wait,the program will exit after", num, sec
            time.sleep(1)
            clear = os.system("cls")
        exit()
    else:
        cal_check_digit()

#用于获取帮助
def help():
    opt = raw_input("Now you have the following options:\n"
                    "1) Press 'H' to obtain help and more information.\n"
                    "2) Press ANY KEY(except 'H' and 'Q') to enter program.\n"
                    "3) Press 'Q' to exit.\n")
    if opt == 'H' or opt == 'h':
        clear = os.system("cls")
        print "HELP INFORMATION:\n" \
              "<1> Please input money After you press ANY KEY(except 'Q').\n" \
              "<2> How to exit the program?\n" \
              "    Press 'Q'.\n"
        opt = raw_input("OK,now you have the following options:\n"
                    "1) Press ANY KEY(except 'Q') to enter the program.\n"
                    "2) Press 'Q' to exit.\n")
        quit(opt)
        cal_check_digit()
    else:
        quit(opt)

while True:
    try:
        print ('Welcome to use this program!')
        help()
        cal_check_digit()
    except Exception, e1:
        print e1
    else:
        break
