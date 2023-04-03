import os
import dotenv
from configparser import ConfigParser
from loguru import logger
from pydantic import BaseSettings


dotenv.load_dotenv()

config_ini = ConfigParser()
config_ini.read('config/config.ini')

class Bot(BaseSettings):
    token: str = os.getenv('bot_token')
    my_id: int = os.getenv('my_id')

class Captcha(BaseSettings):
    token: str = os.getenv('captcha_token')

class Parsing(BaseSettings):
    retries: int = config_ini.getint("PARSING", "retries")

class Logs(BaseSettings):
    sink: str = config_ini.get('LOGS', 'path')
    level: str = config_ini.get('LOGS', 'level')
    rotation: str = config_ini.get('LOGS', 'rotation')
    format: str = config_ini.get('LOGS', 'format')
    compression: str = config_ini.get('LOGS', 'compression')

class Config(BaseSettings):
    debug: bool = config_ini.getboolean('DEFAULT', 'debug')
    alert: bool = config_ini.getboolean('DEFAULT', 'alert')
    logs: Logs = Logs()
    captcha: Captcha = Captcha()
    bot: Bot = Bot()
    parsing: Parsing = Parsing()

config = Config()

