# mnesia_backend/base.py

from django.db.backends.base.base import BaseDatabaseWrapper
from .features import DatabaseFeatures
from .operations import DatabaseOperations
from .utils import call_mnesia

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'mnesia'
    display_name = 'Mnesia (Erlang)'

    def __init__(self, settings_dict, *args, **kwargs):
        super().__init__(settings_dict, *args, **kwargs)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.client = None
        self.creation = None
        self.introspection = None
        self.validation = None

    def get_connection_params(self):
        return {}

    def get_new_connection(self, conn_params):
        return "Connected (simulated)"

    def create_cursor(self, name=None):
        return MnesiaCursor()

    def init_connection_state(self):
        pass

    def is_usable(self):
        return True


class MnesiaCursor:
    def execute(self, query, params=None):
        print(f"Simulating: mnesia:read({query})")
        return call_mnesia(query)

    def fetchall(self):
        return [("Result", 1)]

    def close(self):
        pass
