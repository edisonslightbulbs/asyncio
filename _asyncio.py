import asyncio
import datetime

#  example:

def display_date(end_time, loop):
    print(datetime.datetime.now())
    print(loop.time())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)   # delayed call
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

loop.run_forever()
loop.close()

