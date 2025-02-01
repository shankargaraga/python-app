import logging

logging.basicConfig(level=logging.DEBUG,
            filename="mylog.log",filemode='w',
            format="%(asctime)s - python-app:%(process)d - %(name)s - %(levelname)s - %(message)s")
logging.debug("Debug error occured in code")
logging.info("Info: admin logged in")
logging.warning("warning: less hard diskspace")
logging.error("Error: file is not found exception")
logging.critical("critical: app crashed")

username="ismart-shankar"
logging.info(f"{username} has loggin in")

try:
 a=10
 b=0
 c=a/b


except Exception as exec:
 logging.error("exception occured",exc_info=True)