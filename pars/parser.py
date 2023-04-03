from datetime import datetime
import os
from config import config
from loguru import logger 
from lexicon import LEXICON
from playwright.sync_api import sync_playwright, Page
from mangust228 import CaptchaAi



class Parser:
    def __init__(self, id_, cd):
        self.url = f"https://bangkok.kdmid.ru/queue/OrderInfo.aspx?id={id_}&cd={cd}"

    def parse_condition(self):
        with sync_playwright() as pw: 
            browser = pw.chromium.launch(headless=not config.debug)
            context = browser.new_context()
            logger.debug(f'Объект браузера создан')
            page = context.new_page()
            self._parse_page(page)


    def _parse_page(self, page: Page, retries:int=config.parsing.retries):
        response = page.goto(self.url)
        if response != 200 and retries <= 0:
            logger.debug(f'Ответ не 200! ухожу еще на попытку')
            self._parse_page(page, retries-1)
        else:
            self._solve_captcha(page)
            self._second_page(page)
            self._check_state(page)


    @staticmethod
    def _save_file(page: Page):
        path = datetime.today().strftime('%Y_%m_%d_%H-%M-%S') + '.html'
        if not os.path.exists('data'):
            os.mkdir('data')
        full_path = 'data/' + path
        with open(full_path, 'w') as file:
            file.write(page.content())
        logger.info(f'Файл записан {full_path}')



    def _check_state(self, page: Page):
        logger.debug(f'Перехожу на заключительную страницу')
        page.wait_for_load_state('networkidle')
        first_paragraph = page.inner_text('xpath=//td[@id="center-panel"]/p[1]').strip()
        if first_paragraph == LEXICON['bad_answer']:
            logger.debug(f'Опять двадцатьпять')
        else:
            logger.log('ALERT', 'ЗАПИСЫВАЙСЯ!!!')
            self._save_file(page)
        if config.debug:
            logger.log('ALERT', 'ok')

    def _second_page(self, page: Page):
        logger.debug(f'Перехожу на вторую страницу')
        page.wait_for_load_state('networkidle')
        page.click('xpath=//input[@alt="Записаться в очередь"]')


    def _solve_captcha(self, page: Page):
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(1000)
        for _ in range(config.parsing.retries):
            logger.debug(page.url)
            captcha_dom = page.locator('xpath=(//div[@class="inp"])[last()]/img')
            if not captcha_dom.is_visible():
                logger.debug(f'Капча кажись решена')
                break
            image = captcha_dom.screenshot()
            logger.debug(f'Сделал скрин капчи')
            solver = CaptchaAi(config.captcha.token)
            result = solver.solve_picture(image)
            logger.debug(f'capthcha решена = {result}')
            input_box = page.locator('xpath=(//input[@type="text"])[last()]')
            input_box.fill(result)
            page.click('xpath=(//input[@type="submit"])[last()]')