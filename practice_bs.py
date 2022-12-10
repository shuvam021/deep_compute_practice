from basescript import BaseScript


class HelloWorld(BaseScript):
    def run(self):
        print("Hello world")

    def greet(self):
        print("Hello world !!!!!")


class Adder(BaseScript):
    DESC = "Adds numbers"

    def __init__(self):
        super(Adder, self).__init__()
        self.a = 10
        self.b = 20

    def define_args(self, parser):
        # optional arguments
        parser.add_argument("c", type=int, help="Number to add")

    def run(self):
        # self.log.info("Starting run of script ...")
        print(self.a + self.b + self.args.c)
        # self.log.info("Script is done")


if __name__ == "__main__":
    Adder().start()


# if __name__ == "__main__":
#     HelloWorld().start()
