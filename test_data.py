"""
Тестовые данные
"""
from datetime import datetime

data = [
    {
        'number': '7800000000001',
        'name': 'Пользователь № 1',
        'sessions': [
            {
                'created_at': datetime.strptime('2016-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2016-01-01T01:21:13', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2025-01-01T01:20:01', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2012-01-01T01:21:13', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.strptime('2012-01-01T01:33:59', '%Y-%m-%dT%H:%M:%S'),
                    }
                ],
            },
            {
                'created_at': datetime.strptime('2016-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2044-01-01T01:20:01', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2011-01-01T01:21:13', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.strptime('2031-01-01T01:33:59', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.strptime('2011-01-01T01:33:59', '%Y-%m-%dT%H:%M:%S'),
                    }
                ],
            }
        ]
    },
    {
        'number': '7800000000002',
        'name': 'Пользователь 2',
        'sessions': [
            {
                'created_at': datetime.strptime('2016-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('2001-01-01T01:20:01', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.strptime('1994-01-01T01:21:13', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.strptime('2019-01-01T01:33:59', '%Y-%m-%dT%H:%M:%S'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.strptime('2016-01-01T01:33:59', '%Y-%m-%dT%H:%M:%S'),
                    }
                ],
            }
        ]
    },
]
