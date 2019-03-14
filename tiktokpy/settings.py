class Settings:

    http_prefix = 'https'

    url_api = 'api2.musical.ly'
    url_api16 = 'api2-16-h2.musical.ly'

    urls = {

        'login': (url_api, 'passport/user/login/'),
        'user_info': (url_api16, '/aweme/v1/user/'),

        'search_human': (url_api16, '/aweme/v1/discover/search/'),
        'search_ht':  (url_api16, '/aweme/v1/challenge/search/'),

        'followers_list':  (url_api, 'aweme/v1/user/follower/list/'),
        'followings_list':  (url_api16, 'aweme/v1/user/following/list/'),

        'like':  (url_api16, '/aweme/v1/commit/item/digg/'),

        'follow': (url_api16, '/aweme/v1/commit/follow/user/'),
        'posts': (url_api16, '/aweme/v1/aweme/post/'),

        'comments_list':  (url_api16, '/aweme/v1/comment/list')

    }

    base_headers = {
        ':method': 'GET',
        ':authority': 'api2-16-h2.musical.ly',
        ':scheme': 'https',
        ':path': '',
        'Host': 'api2.musical.ly',
        'User-Agent': 'TikTok 10.3.0 rv:103005 (iPhone; iOS 12.1.4; ru_RU) Cronet',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'x-tt-token': '03a10395e47f188137e97a9938874fd779c376b666aea7d55b3e9c9d077f14982e3c21395181d3fcc9c5e0125b719ef6ed6',
        'sdk-version': '1',
        'X-Khronos': '',
        'X-Pods': '',
        'X-Gorgon': '',
        'Cookie': ''
    }

    query_string = {
        'version_code': '10.3.0',
        'pass-region': '1',
        'pass-route': '1',
        'language': 'ru',
        'app_name': 'musical_ly',
        'vid': 'C6A5896B-9B12-42FA-B43C-123749A77B5F',
        'app_version': '10.3.0',
        'carrier_region': 'RU',
        'is_my_cn': '0',
        'channel': 'App Store',
        'mcc_mnc': '25001',
        'device_id': '6659342247706494469',
        'tz_offset': '10800',
        'account_region': 'RU',
        'sys_region': 'RU',
        'aid': '1233',
        'screen_width': '1125',
        'openudid': 'c8128daffab809a0b644b01ea05c56b31bd4c47e',
        'os_api': '18',
        'ac': 'WIFI',
        'os_version': '12.1.4',
        'app_language': 'ru',
        'tz_name': 'Europe/Moscow',
        'device_platform': 'iphone',
        'build_number': '103005',
        'device_type': 'iPhone9,4',
        'iid': '6664943549341927173',
        'idfa': 'FA987C16-742A-4D4C-9D6C-50DF6EC1003F',
        'mix_mode': '1',
        'ts': '',
    }

    login_data = {
        'username': None,
        'password': None,
        'email': None,
        'mobile': None,
        'account': None,
        'captcha': None
    }

    cookies = {
        # '_ga': 'GA1.2.262510379.1551614599',
        # 'install_id': '6664943549341927173',
        # 'ttreq': '1$52521590916e709995e6a855f299a3a9870c7b1b',
        # 'sid_guard': 'bd9718ba26d2032ac873e2c4b48ad0f3%7C1551810102%7C21600%7CWed%2C+06-Mar-2019+00%3A21%3A42+GMT',
        # 'uid_tt': 'a2a74e3b33d716546c8e11fb47f79917',
        #'_ga':'GA1.2.262510379.1551614599',
        #'guard': 'a10395e47f188137e97a9938874fd779%7C1551814641%7C5184000%7CSat%2C+04-May-2019+19%3A37%3A21+GMT',

        'uid_tt': '91c80eb90e69bbace74f3b5c9d107ee5bad984852311250976b23062e9e2ea41',
        'sid_tt': 'a10395e47f188137e97a9938874fd779',
        'sessionid': 'a10395e47f188137e97a9938874fd779',
        'install_id': '6664943549341927173',
        'odin_tt':  'ad759d0a3df0a77bc360d3dc3d5a2fca10ec5c1944bb4ac228c64702728500c755d6816b785b58ceb9eac6cd6b87046be5350c9263068ded493643985024e051'
        #'odin_tt':
        #'916a2f229cb2f3b1ead5e3a36d9473dd2c9938c6cc9e8665fc57d16a00cd3bcd2f4cc55a5d941e298ccf4c9e011a37f3efe9000bf8b87ee932f99232ec2ae626',
        #'ttreq':'1$52521590916e709995e6a855f299a3a9870c7b1b',
        # 'odin_tt': '118466cbd00308c540dbd46ca38131811718b3984b0d3837d1d18a70dd3a540cd8abd7519010d0ea69653c2e150c249564aae29ba3c81b4473e095ca8e7332ea'
    }





