class QASMConfigException(Exception):

    def __str__(self):
        return "[ERROR] Error: QASMConfigError, Response: {0}".format(super().__str__())
