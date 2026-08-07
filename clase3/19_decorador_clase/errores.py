import logging


class CapturarErrores:
    def __init__(self, valor_defecto=None):
        self.valor_defecto = valor_defecto

    def __call__(self, funcion):
        def envoltura(*args, **kwargs):
            try:
                return funcion(*args, **kwargs)
            except FileNotFoundError:
                logging.error(f"Error: El archivo no existe")
                return self.valor_defecto
            except PermissionError:
                logging.error(f"Error: No hay permisos para leer el archivo")
                return self.valor_defecto
            except Exception as e:
                logging.critical(f"Error inesperado en '{funcion.__name__}': {e}")
                return self.valor_defecto

        return envoltura
