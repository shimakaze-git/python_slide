import asyncio
import time


async def hello_world(n=10):
    time.sleep(1)
    print("{}: Hello World!".format(n))


# call_hello_world1とcall_hello_world2には
# await構文がある

async def call_hello_world1():
    print("call_hello_world1()")
    await hello_world(1)

async def call_hello_world2():
    print("call_hello_world2()")
    await hello_world(2)

if __name__ == "__main__":

    # hello_world()
    # hello_world()単体では、警告が表示される

    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())

    print("-------------------------------------------")

    loop = asyncio.get_event_loop()
    loop.create_task(call_hello_world1())
    loop.run_until_complete(call_hello_world2())
