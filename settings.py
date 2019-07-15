import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH=os.path.join(BASE_DIR,'db','db.json')
LOG_PATH=os.path.join(BASE_DIR,'log','access.log')
LOGIN_TIMEOUT=3

# 配置logging
standard_format='[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# log配置字典
LOGGING_DIC={
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format
        },
        'simple':{
            'format':simple_format
        },
    },
    'filters':{},
    'handlers':{
        # 打印到终端
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'simple'
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers,RotatingFileHandler',
            'formatter':'standard',
            'filename':LOG_PATH,
            'maxBytes':1024*1024*5,
            'backupCount':5,
            'encoding':'utf-8'
        },
    },
    'loggers':{
        '':{
        'handlers':['default','console'],
            'level':'DEBUG',
            'propagate':True
    }

    }
}
