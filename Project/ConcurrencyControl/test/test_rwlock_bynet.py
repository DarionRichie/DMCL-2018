#-*- coding=utf8 -*-

import asyncio
import requests
import random
import time
API = "http://127.0.0.1:5000/"
MAX_NUMBER = 1000000
def generatURL(type,id,**args):
	url = API+type+'?id={}'.format(id)
	for each in args:
		url+=('&'+each+'='+args[each])
	return url

async def get(url):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, url)
    print(res.text)
    return res.text
    # return True if res.text=='success' else False

async def hello(i,value):
    # print("协程" + str(n) +"启动")
    #update = await get(generatURL('writebylock',i,name = str(i),value = str(i)))
    update = await get(generatURL('withdrawbylock',i,name = str('account1'),value = str(value)))
    # print("协程" + str(n) + "结束")
    # await hello2(n)
async def add(i,value):
    add  = await get(generatURL('addbylock',i,name = 'account'+str(i),value = str(value)))

if __name__ == "__main__":
    tasks = []
    addtasks=[]
    counts = 10
    for i in range(1, counts+1):
        tasks.append(hello(i,10))
        addtasks.append(add(i,counts*10))
    timestart = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(addtasks))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    timeend = time.time()
    print(timeend-timestart)


