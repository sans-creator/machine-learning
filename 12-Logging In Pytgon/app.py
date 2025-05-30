import logging

#logging settings

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%M-%D %H:%M:%S',
handlers=[
    logging.FileHandler("app1.log"),
    logging.StreamHandler()
]
                    
)
logger=logging.getLogger("Arithematic App")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a} + {b}={result}")
    return result

def subs(a,b):
    result=a+b
    logger.debug(f"substracting {a} - {b}={result}")
    return result
def mutliply(a,b):
    result=a+b
    logger.debug(f"mutlipying {a}*{b}={result}")
    return result
add(10,15)
subs(15,10)
mutliply(10,20)