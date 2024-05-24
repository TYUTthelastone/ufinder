import module.Logger.logger as log
import module.Client.client as client
import asyncio

async def run():
    c = client.Client()
    await c.run()
    page = await c.request("http://www.qidian.com")
    log.info(await page.content())

if __name__ == '__main__':
    log.init()
    log.info("begin")
    #subprocess.Popen(command, shell=True)
    asyncio.run(run())
    log.info("end")
