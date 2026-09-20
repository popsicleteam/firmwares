import blocklay


@blocklay.task("hi")
async def code1():
    print("hi3")


@blocklay.task("hi")
async def code2():
    print("hi4")
