#mPythonType:0
from mpython import *

Daylight_engine_start_x = None

Daylight_engine_start_y = None

Daylight_engine_start_wide = None

Daylight_engine_start_height = None

Daylight_engine_start_fillet = None

Daylight_engine_next_app = None

Daylight_engine_app_back_button = None

Daylight_engine_open_button = None

home_icon_edge = None

home_movement_y = None

home_icon_choosen_name = None

home_movement_x = None

Daylight_engine_dome_x = None

Daylight_engine_dome_y = None

Daylight_engine_dome_wide = None

Daylight_engine_dome_height = None

def initialize():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    oled.fill(0)
    Start = [0XFF,0X38,0X00,0X00,0X00,0X03,0X80,0X38,0XFF,0X38,0X00,0X00,0X00,0X0F,0XE0,0XFE, 0XFF,0X38,0X00,0X00,0X00,0X1E,0XF1,0XEF,0XE0,0X38,0X00,0X00,0X00,0X38,0X71,0X86, 0XE0,0X38,0XFC,0X3D,0X80,0X30,0X39,0X80,0XE0,0X38,0XFC,0X7F,0X80,0X30,0X39,0XE0, 0XFF,0X38,0X0E,0X63,0X80,0X30,0X38,0XFC,0XFF,0X38,0X3E,0X61,0X80,0X30,0X38,0X1E, 0XE0,0X38,0XFE,0X61,0X80,0X30,0X38,0X07,0XE0,0X39,0XCE,0X61,0X80,0X38,0X30,0X87, 0XE0,0X39,0X8E,0X73,0X80,0X3C,0XF1,0XC7,0XE0,0X3D,0XFE,0X3F,0X80,0X1F,0XE1,0XFE, 0XE0,0X1C,0XEE,0X1D,0X80,0X07,0XC0,0X78,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X73,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X3F,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1C,0X00,0X00,0X00,0X00,]
    oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
    oled.show()
    Daylight_engine_start_x = 0
    Daylight_engine_start_y = 0
    Daylight_engine_start_wide = 128
    Daylight_engine_start_height = 64
    Daylight_engine_start_fillet = 0
    Daylight_engine_next_app = 'null'
    # 返回按钮文案
    Daylight_engine_app_back_button = 'PY-'
    # 打开按钮文案
    Daylight_engine_open_button = 'TH-'
    # 图标大小变量
    home_icon_edge = 35
    # 桌面图标的y轴基准位置
    home_movement_y = 9
    # 选中app的名称（此变量是为了防止系统启动失败）
    home_icon_choosen_name = '暂未选择'
    # 桌面图标的x轴基准位置
    home_movement_x = 40
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'null'
    Daylight_engine_execute()
    WiFi()

wifi=wifi()

# 此程序使用了GxxkSystemBlockAPI（缩写GSBlockAPI）或此模块（插件）的修改版

import network

import ntptime

import time

def WiFi():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    oled.fill(0)
    oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
    oled.DispChar(str('       正在尝试连接 WiFi'), 0, 48, 1)
    oled.show()
    try:
        wifi.connectWiFi('TP-LINK_CD4A','13697295123')
        ntptime.settime(8, "time.windows.com")
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.DispChar(str('            配置成功'), 0, 48, 1)
        oled.show()
        time.sleep(2)
        Daylight_engine_dome_x = 0
        Daylight_engine_dome_y = 0
        Daylight_engine_dome_wide = 0
        Daylight_engine_dome_height = 0
        Daylight_engine_next_app = 'lockscreen'
        Daylight_engine_execute()
    except:
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.DispChar(str('            配置失败'), 0, 48, 1)
        oled.show()
        while not (button_a.is_pressed() or button_b.is_pressed()):
            if button_a.is_pressed():
                WiFi()
            elif button_b.is_pressed():
                lockscreen()

import framebuf

import font.dvsmb_21

import font.dvsmb_12

def lockscreen():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    while not (touchpad_t.is_pressed() and touchpad_h.is_pressed()):
        Flag_Time()
        oled.fill(0)
        display_font(font.dvsmb_21, (str(Flag_H)), 35, 17, False)
        display_font(font.dvsmb_21, (':'), 65, 17, False)
        display_font(font.dvsmb_21, (str(Flag_Min)), 75, 17, False)
        display_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 50, 40, False)
        oled.hline(50, 60, 30, 1)
        oled.show()
    Daylight_engine_dome_x = 64
    Daylight_engine_dome_y = 63
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'app'
    Daylight_engine_execute()

Daylight_engine_dome_wait = None

def Daylight_engine_execute():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    Daylight_engine_dome_wait = 5
    for count in range(7):
        oled.fill_rect(Daylight_engine_dome_x, Daylight_engine_dome_y, Daylight_engine_dome_wide, Daylight_engine_dome_height, 0)
        Daylight_engine_dome_x = (Daylight_engine_dome_x - Daylight_engine_start_x) // 2
        Daylight_engine_dome_y = (Daylight_engine_dome_y - Daylight_engine_start_y) // 2
        Daylight_engine_dome_wide = (Daylight_engine_start_wide + Daylight_engine_dome_wide) // 2
        Daylight_engine_dome_height = (Daylight_engine_start_height + Daylight_engine_dome_height) // 2
        Daylight_engine_dome_wait = Daylight_engine_dome_wait + 3
        oled.rect(Daylight_engine_dome_x, Daylight_engine_dome_y, Daylight_engine_dome_wide, Daylight_engine_dome_height, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            break
        time.sleep_ms(Daylight_engine_dome_wait)
    if Daylight_engine_next_app == 'app':
        app()
    elif Daylight_engine_next_app == 'lockscreen':
        lockscreen()
    elif Daylight_engine_next_app == 'WiFi':
        WiFi()
    elif Daylight_engine_next_app == 'Flag_Settings':
        Flag_Settings()
    elif Daylight_engine_next_app == 'Flag_Sample_program':
        Flag_Sample_program()

Flag_H = None

Flag_Min = None

Flag_S = None

Flag_Time_H = None

Flag_Time_Min = None

Flag_Time_S = None

def Flag_Time():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    Flag_H = str(time.localtime()[3])
    Flag_Min = str(time.localtime()[4])
    Flag_S = str(time.localtime()[5])
    Flag_Time_H = str(time.localtime()[3])
    Flag_Time_Min = str(time.localtime()[4])
    Flag_Time_S = str(time.localtime()[5])
    if len(Flag_Time_H) < 2:
        Flag_H = '0' + str(Flag_Time_H)
    else:
        Flag_H = Flag_Time_H
    if len(Flag_Time_Min) < 2:
        Flag_Min = '0' + str(Flag_Time_Min)
    else:
        Flag_Min = Flag_Time_Min
    if len(Flag_Time_S) < 2:
        Flag_S = '0' + str(Flag_Time_S)
    else:
        Flag_S = Flag_Time_S

select_app = None

chajian_ui = None

def app():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    select_app = 'Flag'
    chajian_ui = 1
    while not button_a.is_pressed():
        # 系统操作识别基础框架。
        # 请谨慎更改。
        if home_movement_x >= 20 and home_movement_x <= 80:
            if touchpad_y.is_pressed():
                home_movement_x = home_movement_x + 7
            elif touchpad_o.is_pressed():
                home_movement_x = home_movement_x + -7
        else:
            if home_movement_x <= 20:
                home_movement_x = 24
            elif home_movement_x >= 80:
                home_movement_x = 79
        oled.fill(0)
        oled.RoundRect(home_movement_x, home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.RoundRect((home_movement_x - 40), home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.DispChar(str(home_icon_choosen_name), 35, 49, 3)
        oled.show()
        # 判断app1所处位置
        # 判断app1所处位置
        if home_movement_x >= 0 and home_movement_x <= 46:
            home_icon_choosen_name = '示例程序'
            select_app = '示例程序'
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_Sample_program'
                Daylight_engine_execute()
        elif home_movement_x >= 47 and home_movement_x <= 75:
            home_icon_choosen_name = '设置'
            select_app = '设置'
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_Settings'
                Daylight_engine_execute()
        oled.show()
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'lockscreen'
    Daylight_engine_execute()

Flag_Settings_list_start = None

import gc

def Flag_Settings():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    Flag_Settings_list = [' ', '重连网络', '同步时间', '清理内存', '系统信息', ' ']
    print(Flag_Settings_list)
    try:
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar(str('                 设置'), 0, 0, 1)
            oled.RoundRect(0, 15, 128, 100, 10, 1)
            oled.DispChar(str(Flag_Settings_list[Flag_Settings_list_start]), 35, 30, 1)
            oled.show()
            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                Flag_Settings_list_start = Flag_Settings_list_start - 1
                time.sleep(0.5)
            if touchpad_o.is_pressed() and touchpad_n.is_pressed():
                Flag_Settings_list_start = Flag_Settings_list_start + 1
                time.sleep(0.5)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                if Flag_Settings_list_start == 1:
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_next_app = 'WiFi'
                    Daylight_engine_execute()
                elif Flag_Settings_list_start == 2:
                    try:
                        Daylight_engine_dome_x = 64
                        Daylight_engine_dome_y = 63
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'null'
                        Daylight_engine_execute()
                        oled.fill(0)
                        oled.DispChar(str('请稍等...'), 0, 0, 1)
                        oled.show()
                        ntptime.settime(8, "time.windows.com")
                        oled.fill(0)
                        oled.DispChar(str('成功'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                    except:
                        oled.fill(0)
                        oled.DispChar(str('失败'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                elif Flag_Settings_list_start == 3:
                    try:
                        Daylight_engine_dome_x = 64
                        Daylight_engine_dome_y = 63
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'null'
                        Daylight_engine_execute()
                        oled.fill(0)
                        oled.DispChar(str('请稍等...'), 0, 0, 1)
                        oled.show()
                        gc.enable()
                        gc.collect()
                        oled.fill(0)
                        oled.DispChar(str('成功'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                    except:
                        oled.fill(0)
                        oled.DispChar(str('失败'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                elif Flag_Settings_list_start == 4:
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_next_app = 'null'
                    Daylight_engine_execute()
                    oled.fill(0)
                    while not button_a.is_pressed():
                        oled.Bitmap(32, 12, bytearray(Start), 44.8, 12.6, 1)
                        oled.DispChar(str('Version：2.0 Stable'), 0, 32, 1)
                        oled.DispChar(str('By Can1425'), 0, 48, 1)
                        oled.show()
                    Daylight_engine_dome_x = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_next_app = 'Flag_Settings'
                    Daylight_engine_execute()
            if Flag_Settings_list_start < 1:
                Flag_Settings_list_start = 1
            if Flag_Settings_list_start > 4:
                Flag_Settings()
        Daylight_engine_dome_x = 0
        Daylight_engine_dome_y = 0
        Daylight_engine_dome_height = 0
        Daylight_engine_dome_wide = 0
        Daylight_engine_next_app = 'app'
        Daylight_engine_execute()
    except:
        Flag_Settings_list_start = 0
        Flag_Settings()

def Flag_Sample_program():
    global Daylight_engine_dome_wait, Flag_H, select_app, Daylight_engine_dome_x, Flag_Min, chajian_ui, Flag_Settings_list, Start, Daylight_engine_dome_y, Flag_S, Daylight_engine_dome_wide, Daylight_engine_dome_height, Flag_Time_H, Flag_Settings_list_start, Daylight_engine_start_x, Daylight_engine_next_app, Flag_Time_Min, Daylight_engine_start_y, Flag_Time_S, home_movement_x, Daylight_engine_start_wide, home_movement_y, home_icon_edge, Daylight_engine_start_height, Daylight_engine_start_fillet, home_icon_choosen_name, Daylight_engine_app_back_button, Daylight_engine_open_button
    oled.fill(0)
    while not button_a.is_pressed():
        oled.DispChar(str('Hello, world!'), 0, 0, 1)
        oled.DispChar(str('按 A 键返回'), 0, 16, 1)
        oled.show()
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_next_app = 'app'
    Daylight_engine_execute()

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]
initialize()
