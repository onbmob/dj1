class DbRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.db_table == 'table_ps_price_1c':
            return 'status'
        if model._meta.db_table == 'test1':
            return 'default'
        # if model._meta.app_label == 'polls':
        #     return 'dj2local'
        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.db_table == 'table_ps_price_1c':
            return 'status'
        if model._meta.db_table == 'test1':
            return 'default'
        # if model._meta.app_label == 'polls':
        #     return 'dj2local'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in the Example app.
        if obj1._meta.app_label == 'polls' and obj2._meta.app_label == 'polls':
            return True
        # No opinion if neither object is in the Example app (defer to default or other routers).
        elif 'polls' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        # Block relationship if one object is in the Example app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        # if app_label == 'polls':
            # The Example app should be migrated only on the example_db database.
            # return db == 'dj2local'
        # elif db == 'dj2local':
            # Ensure that all other apps don't get migrated on the example_db database.
            # return False
        # if db == 'test1':
        #     return 'default'
        if db == 'status':
            return False

        # No opinion for all other scenarios
        return True