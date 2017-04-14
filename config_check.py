'''
}
    "status": "UP",
    "diskSpace": {
        "status": "UP",
        "total": 1056753999872
                 845403199897.6,
        "free": 1048994672640,
        "threshold": 10485760
    },
    "redis": {
        "status": "UP",
        "version": "2.8.19"
    },
    "db": {
        "status": "UP",
        "database": "MySQL",
        "hello": 1
    },
}
'''

check_service = {'status': 'UP'}
check_diskSpace = {'status': 'UP', 'total': 0, 'free': 845403199897, 'threshold': 0}
check_redis = {'status': 'UP', 'version': '2.8.19'}
check_db = {'status': 'UP', 'database': 'MySQL', 'hello': 1}

check_dics = [check_service, check_diskSpace, check_redis, check_db]