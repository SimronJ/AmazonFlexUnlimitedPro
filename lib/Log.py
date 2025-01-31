class Log:
    @staticmethod
    def info(message: str):
        print(f"INFO: {message}", flush=True)

    @staticmethod
    def error(message: str):
        print(f"ERROR: {message}", flush=True)

    @staticmethod
    def notice(message: str):
        print(f"NOTICE {message}", flush=True)
