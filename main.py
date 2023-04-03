from loguru import logger
from utils import get_id_and_cd_request
from pars import Parser
logger.info("Start parsing")

@logger.catch()
def main():
    id_, cd = get_id_and_cd_request()
    parser = Parser(id_, cd)
    parser.parse_condition()

if __name__ == '__main__':
    main()