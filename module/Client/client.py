import httpx
import asyncio
import module.Logger.logger as log
import playwright.async_api as pw
js="""
Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
"""
class Client():
    def __init__(self):
        pass
        
    async def run(self):
        self.pw = await pw.async_playwright().start()
        self.browser = await self.pw.webkit.launch(headless=True)
        device = self.pw.devices["iPhone 14 Pro"]
        self.context = await self.browser.new_context(**device)
        
    async def request(self, url) -> pw.Page:
        page = await self.context.new_page()
        await page.add_init_script(js)
        await page.goto(url)
        return page
        