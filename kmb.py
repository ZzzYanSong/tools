import random
from serial.tools.list_ports import comports
from serial import Serial

"""
 github：https://github.com/ZzzYanSong/tools/
 kmb例子
 自动获取kmboxb COM端口
 常用例子已写出 可直接调用
 """

def km_Obtain_Com():
    try:
        num = random.randint(20, 30)
        # uart_class = list(serial.tools.list_ports.comports())
        uart_class = list(comports())
        if len(uart_class) <= 0:
            print("can't find the uart")
        else:
            for i in uart_class:
                uart_temp_str = str(i)
                uart_list = uart_temp_str.split()
                for j in uart_list:
                    # 查找"USB-SERIAL"的串口
                    if "USB-SERIAL" == j:
                        uart_num = uart_list[0]
                        # print(uart_num)
        return uart_num
    except:
        print("端口出错,检测到你未安装kmbox驱动")
#实例化kmbox
try:
    com = km_Obtain_Com()
    km = Serial(com, 115200)
except:
    print("km出现重复调用，不影响正常使用！")


#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓函数↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

def km_mose_leftDown(): #鼠标左键物理按下
    km.write(f"km.left(1)\r\n".encode('utf-8'))

def km_mouse_leftDown_software(): #鼠标左键软件按下
    km.write(f"km.left(2)\r\n".encode('utf-8'))

def km_mouse_leftUp(): #鼠标左键弹起
    km.write(f"km.left(0)\r\n".encode('utf-8'))

def km_mouse_rightDown(): #鼠标右键物理按下
    km.write(f"km.right(1)\r\n".encode('utf-8'))

def km_mouse_rightDown_software(): #鼠标右键软件按下
    km.write(f"km.right(2)\r\n".encode('utf-8'))

def km_mouse_rightUp(): #鼠标右键弹起
    km.write(f"km.right(0)\r\n".encode('utf-8'))

def km_mouse_move(x,y): #鼠标相对移动
    km.write(f"km.move({int(x)},{int(y)})\r\n".encode('utf-8'))

def km_mouse_moveto(x,y): #鼠标绝对移动
    km.write(f"km.moveto({int(x)},{int(y)})\r\n".encode('utf-8'))

def km_keyboard_down(key): #键盘按下 参数直接填写键 如km_keyboard_down('a')
    km.write(f"km.down('{key}')\r\n".encode('utf-8'))

def km_keyboard_up(key): #键盘弹起 参数直接填写键 如km_keyboard_up('a') 与km_keyboard_down 连用
    km.write(f"km.up('{key}')\r\n".encode('utf-8'))

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓示例↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

#示例 按下键盘的X按键
km_keyboard_down('x')
km_keyboard_up('x')

#示例 相对移动鼠标
km_mouse_move(30,50)
