class NullSolution(Exception):
    """Error to be raised when a DLP algorithm terminates without
    finding a solution"""
    def __init__(self, *args: object) -> None:
        # TODO: Choose better defaul message
        default_message = 'Solution does not exist'
        if not args: args = (default_message,)
        super().__init__(*args)