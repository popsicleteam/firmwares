import asyncio

from blocklay import *

times = 1


async def snippet1():
    """
    # TOML document
    # 独立脚本，需要手动调用才会执行
    #
    pos = [x, y] # x 和 y 是在工作区的坐标（第一个积木）
    fold = false # 折叠积木，默认不折叠
    """
    print("nothing")


@task()
async def code1():
    global times
    """
    # 任务，启动时自动调用
    #
    pos = [x, y]
    """
    print("code1")
    call(block1)
    while True:
        times += 1
        await asyncio.sleep(1)


@task()
async def code2():
    """
    # 可以同时执行多个任务
    #
    pos = [x, y]
    """
    await asyncio.sleep(1)
    print("code3")


@task("hi")
async def code3():
    """
    # 广播任务，所有监听广播"hi"的任务都会被调用
    #
    pos = [x, y]
    """
    print("hi1")


@task("hi")
async def code4():
    """
    pos = [x, y]
    """
    print("hi2")


# 非可见代码
# 条件任务的判断条件
async def __flag1():
    return times > 5


@task(__flag1)
async def code5():
    global times
    """
    # 条件任务
    #
    pos = [x, y]
    """
    times = 0
    print("code5")


async def block1(opt1=None, arg1: int = 0, arg2: int = 0) -> None:
    """
    # 积木定义
    # 返回类型为 None 是一个普通积木
    # 返回类型为 str/int/float/bool 表示是一个内嵌积木
    # argx 是输入参数积木，可指定类型 str/int/float/bool，默认值分别是 ""/0/0.0/False
    # optx 是选项参数菜单，不指定类型，
    #
    pos = [x, y]
    fold = false
    protected = false # 保护积木，默认不保护，保护后积木过程不在工作区显示

    # [label] 是积木显示的文本表（多语言）
    # en 是积木默认显示的文本（英文）
    # zh-hans 是中文翻译
    # [] 选项参数，“|”后面是菜单选项值
    # {} 输入参数（必须为英文，函数声明参数），“:”后面的是显示文本，没有则用参数实际名
    [label]
    en = "block [opt1|1] {arg1} {arg2}"
    zh-hans = "积木 [opt1|1] {arg1:参数1} {arg2:参数2}"

    # [menu.opt1] 是选项参数菜单的菜单项
    # value 是选项值
    # label 是选项显示文本
    [[menu.opt1]]
      value = 1
      [menu.opt1.label]
        en = "menu item 1"
        zh-hans = "菜单选项1"

    [[menu.opt1]]
      value = 2
      [menu.opt1.label]
        en = "menu item 2"
        zh-hans = "菜单选项2"

    # [tip]是积木的提示文本表（多语言）
    [tip]
    en = "block demo"
    zh-hans = "积木演示"
    """
    await asyncio.sleep(1)
    broadcast("hi")
