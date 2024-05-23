import module.Logger.logger as log
import httpx
import asyncio
import playwright.async_api as pw
import subprocess
import json

#输入Chrome浏览器所在路径
chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
debugging_port = "--remote-debugging-port=9222"

command = f"{chrome_path} {debugging_port}"

async def static_request(url):
    async with httpx.AsyncClient() as client:
        client.follow_redirects = True
        r = await client.get(url)
        log.warn(url)
        log.info(r.text)


async def dynamic_request(url):
    async with pw.async_playwright() as p:
        browser = await p.chromium.launch()
        #browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        #device = p.devices["Desktop Edge"]
        #log.info(device.keys())
        #context = await browser.new_context(**device)
        # context = browser.contexts[0]
        # cookies = await context.cookies()
        # with open("cookie","+wt") as fp:
        #     json.dump(cookies,fp)
        context = await browser.new_context()
        with open("cookie","+rt") as fp:
            cookie = json.load(fp)
            await context.add_cookies(cookie)
        page = await context.new_page()
        await page.goto(url)
        await asyncio.sleep(10.0)
        await page.screenshot(path=f'example.png')
        await context.close()
        await browser.close()
    
if __name__ == '__main__':
    log.init()
    log.info("begin")
    #subprocess.Popen(command, shell=True)
    asyncio.run(dynamic_request("http://www.qidian.com"))
    log.info("end")
