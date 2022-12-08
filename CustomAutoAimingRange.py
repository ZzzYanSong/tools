import math
def linexy(x,y,len):#计算两点坐标距离 （敌人的x坐标，y坐标，自瞄范围半径） 简单说 三角函数取第三边长度

    """
     github：https://github.com/ZzzYanSong/
     由于模型要求最小截图大小的可以通过此方法实现自瞄范围设定！！
     原理：将处理好的敌人距离准心的相对移动参数传入计算出坐标距离准心的直线距离 判断与之设定的自瞄范围（圆形）的半径
     如果小于则返回真 否则则返回假
     代码中几个print可以删除
     调用实例：
     if (linexy(敌人X坐标, 敌人Y坐标, 设定的自瞄范围)):
        move(敌人X坐标,敌人Y坐标) #如果在自瞄范围内则移动鼠标执行自瞄
     else：
         pirnt（不在自瞄范围内）
         else部分可省略
     """
    result = math.sqrt(
        math.pow(x -0,2) +math.pow(y -0,2)) #计算坐标距离原点（准心）距离
    if(result<len): #如果距离小于自瞄范围半径则自瞄
        print("在自瞄范围，自瞄")
        print("敌人的相对坐标({},{})".format(x,y))
        print("敌人距离准心的直线距离:{}".format(result))
        return True
    else: #否则则不自喵
        print("未在自瞄范围，不自喵")
        print("敌人的相对坐标({},{})".format(x,y))
        print("敌人距离准心的直线距离:{}".format(result))
        return False



