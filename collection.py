from itertools import chain
from test_data import data


class CollectionMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        attrs["COLLECTION"] = name
        return super().__new__(mcs, name, bases, attrs)


class AccountInitException(Exception):
    pass


class Account(metaclass=CollectionMetaclass):

    def __init__(self, number: str, name: str, sessions: []):

        if not all([type(number) is str, len(number) == 13]):
            raise AccountInitException("Переданный параметр number не соответствует условиям")

        self.number = number
        self.name = name
        self.sessions = sessions  # расчет на то что у каждого пользователя есть хотя бы одна сессия

    @staticmethod
    def get_accounts_info(accounts: list) -> list:
        """
        Вернет информацию по каждому пользователю, полагая что данные в коллекции не отсортированы
        :param accounts: список аккаунтов
        :return: результат в виде списка
        """
        result = []
        for account in accounts:
            actions = list(chain.from_iterable([session.get("actions") for session in account.sessions]))
            # собираю actions из всех сессий

            action_types = ("read", "create", "update", "delete")

            result_actions = []
            for action_type in action_types:
                action_lst = sorted(
                    [action for action in actions if action.get("type") == action_type],
                    key=lambda action: action.get("created_at")) or []

                last = None
                if len(action_lst):
                    last = {"created_at": action_lst[-1].get("created_at")}

                result_actions.append({
                    "type": action_type,
                    "last": last,
                    "count": len(action_lst)
                })

            result.append({
                "number": account.number,
                "actions": result_actions
            })

        return result


if __name__ == '__main__':
    accounts = []
    for item in data:  # заполнение коллекции тестовыми данными
        accounts.append(Account(*item.values()))

    print(Account.get_accounts_info(accounts))
