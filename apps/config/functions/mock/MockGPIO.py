class MockGPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    IN = 'IN'

    @staticmethod
    def setmode(mode):
        print(f"Mock setmode({mode}) called")

    @staticmethod
    def setup(channel, mode):
        print(f"Mock setup({channel}, {mode}) called")

    @staticmethod
    def output(channel, state):
        print(f"Mock output({channel}, {state}) called")

    @staticmethod
    def input(channel):
        print(f"Mock input({channel}) called")
        return False

    @staticmethod
    def cleanup():
        print("Mock cleanup() called")

    @staticmethod
    def setwarnings(flag):
        print(f"Mock setwarnings({flag}) called")