class Delegator(object):
    def __getattr__(self, called_method):
        def wrapper(*args, **kwargs):
            delegation_config = getattr(self, 'DELEGATED_METHODS', None)
            if not isinstance(delegation_config, dict):
                raise AttributeError(f"{self.__class__.__name__} object has not defined any delegation methods.")

            for delegate_object_str, delegate_methods in delegation_config.items():
                if called_method in delegate_methods:
                    break
                else:
                    raise AttributeError(f"{self.__class__.__name__} object has no attribute {called_method}")

            delegate_object = getattr(self, delegate_object_str, None)

            return getattr(delegate_object, called_method)(*args, **kwargs)
        return wrapper
