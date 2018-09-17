import pyagentx


class NetSnmpPlaypen(pyagentx.Updater):
    def update(self):
        self.set_INTEGER('1', 23)


class MyAgent(pyagentx.Agent):
    def setup(self):
        self.register('1.3.6.1.4.1.9999', NetSnmpPlaypen)


def main():
    pyagentx.setup_logging()
    try:
        a = MyAgent()
        a.start()
    except Exception as e:
        print('Unhandled exception:', e)
        a.stop()
    except KeyboardInterrupt:
        a.stop()


if __name__ == '__main__':
    main()
