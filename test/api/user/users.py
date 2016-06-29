data = [
    {
        "name": "test_get_users",
        "url": "/api/users/",
        "method": "get",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_get_users_admin",
        "url": "/api/users/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": [{"password": "00b93578e0284e8a4b92fec5f386cbb5", "created_at": "2016-06-17 10:23:27", "id": 1, "account": "admin", "updated_at": "2016-06-17 10:23:27", "token": "ADMIN@TOKEN", "type": 0, "name": "admin"}]
        }
    },
    {
        "name": "test_gen_user",
        "url": "/api/users/csv/",
        "method": "post",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_gen_user",
        "url": "/api/users/csv/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "files": {
            "users_file": "./api/user/users.csv"
        },
        "ignore": ["password", "repassword", "token", "err_msg"],
        "response_status": 200,
        "response_data": {
            "msg": {
                "error": [{
                    "name": "a", 
                    "account": "a",
                    "type": 1
                }, {
                    "account": "e", 
                    "name": "e", 
                    "type": 4
                }], 
                "success": [{
                    "account": "a", 
                    "name": "a", 
                    "id": 2, 
                    "type": 0
                }, {
                    "account": "b", 
                    "name": "b", 
                    "id": 3, 
                    "type": 1
                }, {
                    "account": "c", 
                    "name": "c", 
                    "id": 4, 
                    "type": 2
                }, {
                    "account": "d", 
                    "name": "d", 
                    "id": 5, 
                    "type": 3
                }]
            }
        }
    }
]
