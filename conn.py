import math
import requests
import time
import aiohttp
import asyncio
import concurrent.futures

def get_url(filename):
	urls = []
	with open(filename, 'rt') as f:
		for line in f:
			urls.append(line.strip())
	return urls


def demo_sequential(url_list):
	ts = time.time()
	for url in url_list:
		s = time.time()
		res = requests.get(url)
		e = time.time()
		res.content
		print(res.status_code, url, e-s)
	print("total time in seq", time.time()-ts)


def demo_thread(url):
	s = time.time()
	res = requests.get(url)
	res.content
	e = time.time()
	print(res.status_code, url, e-s)


async def demo_async(session: aiohttp.ClientSession, url: str):
	s = time.time()
	async with session.get(url) as res:
		await res.read()
	print(res.status, url, time.time()-s)
	return await res.release()



if __name__ == '__main__':
	URL_LIST = ['https://facebook.com',
                'https://github.com',
                'https://google.com',
                'https://microsoft.com',
                'https://yahoo.com']


	print("*********************squential*********************************")
	demo_sequential(URL_LIST)
	print("\n")
	# threaded
	print("*********************threaded*********************************")
	th = time.time()
	tasks = []
	with concurrent.futures.ThreadPoolExecutor() as executer:
		for url in URL_LIST:
			future = executer.submit(demo_thread, url)
			tasks.append(future)
		for task in concurrent.futures.as_completed(tasks):
			pass

	print("thread done", time.time()-th)
	print("\n")

	## multi processes
	print("*********************multiprocess*********************************")
	th = time.time()
	tasks = []
	with concurrent.futures.ProcessPoolExecutor() as executer:
		for url in URL_LIST:
			future = executer.submit(demo_thread, url)
			tasks.append(future)
		for task in concurrent.futures.as_completed(tasks):
			pass
	print("multi-process done", time.time() - th)
	print("\n")
	print("*********************async*********************************")

	async def main(loop):
		async with aiohttp.ClientSession(loop=loop) as session:
			async_task = [demo_async(session, url) for url in URL_LIST]
			await asyncio.gather(*async_task)
	ts = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(loop))
	print("asyncio done in:", time.time()-ts)


