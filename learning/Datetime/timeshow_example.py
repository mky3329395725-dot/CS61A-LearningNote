import turtle
import datetime


def drawLine(draw):
    """绘制单段数码管"""
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(40)   # 向前画40像素（每段的长度）
    turtle.right(90)     # 右转90度，准备画下一段


def drawDigit(d):
    """根据数字绘制七段数码管"""
    # 七段数码管的绘制顺序（a-g段）
    drawLine(d in [2, 3, 4, 5, 6, 8, 9])          # a段
    drawLine(d in [0, 1, 3, 4, 5, 6, 7, 8, 9])    # b段
    drawLine(d in [0, 2, 3, 5, 6, 8, 9])          # c段
    drawLine(d in [0, 2, 6, 8])                   # d段
    turtle.left(90)                               # 调整方向，准备画竖段
    drawLine(d in [0, 4, 5, 6, 8, 9])             # e段
    drawLine(d in [0, 2, 3, 5, 6, 7, 8, 9])       # f段
    drawLine(d in [0, 1, 2, 3, 4, 7, 8, 9])       # g段
    turtle.left(180)                              # 调整方向，为下一个数字准备
    turtle.penup()
    turtle.forward(20)                            # 数字间的间隔


def drawDate(date_str):
    """遍历日期字符串，逐个绘制数字"""
    for char in date_str:
        drawDigit(int(char))   # 用 int() 替代 eval()，更安全


def main():
    turtle.setup(width=800, height=350, startx=200, starty=200)  # 窗口大小与位置
    turtle.penup()
    turtle.forward(-300)       # 调整起始绘制位置
    turtle.pensize(5)          # 画笔粗细
    turtle.hideturtle()        # 隐藏海龟图标
    turtle.speed(0)            # 最快速度（0=最快）

    # 获取当前日期，格式：YYYYMMDD
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    drawDate(current_date)

    turtle.done()              # 保持窗口打开


if __name__ == "__main__":
    main()