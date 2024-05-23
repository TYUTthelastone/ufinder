import module.Logger.logger as log
import httpx
import asyncio

async def request(url):
    async with httpx.AsyncClient() as client:
        client.follow_redirects = True
        r = await client.get(url)
        log.warn(url)
        log.info(r.text)
    
if __name__ == '__main__':
    log.init()
    log.info("begin")
    asyncio.run(request("http://www.qidian.com"))
    log.info("end")
