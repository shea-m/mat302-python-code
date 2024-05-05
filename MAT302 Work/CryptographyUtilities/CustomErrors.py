class NullSolution(Exception):
    """Error to be raised when a DLP algorithm terminates without
    finding a solution"""
    def __init__(self, *args: object) -> None:
        # TODO: Choose better defaul message
        default_message = 'Solution does not exist'
        if not args: args = (default_message,)
        super().__init__(*args)

class InvalidKey(Exception):
    """Error raised when an invalid key is provided"""
    def __init__(self, *args: object) -> None:
        # TODO: Choose better defaul message
        default_message = 'Key not allowed, choose one in the key group'
        if not args: args = (default_message,)
        super().__init__(*args)

class OffCurve(Exception):
    """Error raised when a point is off an elliptic curve"""
    def __init__(self, *args: object) -> None:
        default_message = 'Point does not exist on the given curve'
        if not args: args = (default_message,)
        super().__init__(*args)

class NonSingular(Exception):
    """Error raised when curve is nonsingular"""
    def __init__(self, *args: object) -> None:
        default_message = 'Curve is nonsingular, addition not possible'
        if not args: args = (default_message,)
        super().__init__(*args)
