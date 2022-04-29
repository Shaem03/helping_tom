import time
import json
import argparse

from websocket import create_connection


def is_prime(data):
    number = data["b"]
    if number == 1 or number == 0 or (number % 2 == 0 and number > 2):
        return False
    else:
        for i in range(3, int(number ** (1 / 2)) + 1, 2):
            if number % i == 0:
                return False
        return True


def is_even(data):
    number = data["b"]
    if number % 2 == 0:
        return True
    else:
        return False


class Analysis:
    def __init__(self, duration):
        self.base_url = "ws://209.126.82.146"
        self.port = 8080
        self.duration = duration

        self.ws = None
        self.blocks_info = []
        self.blocks = 0

    def connect(self):
        self.ws = create_connection(f'{self.base_url}:{self.port}')
        return self.ws.connected

    def start(self):
        start_time = time.time()
        for mysterious_data in self.ws:
            if time.time() > start_time + self.duration:
                break
            else:
                self.blocks_info.append(json.loads(mysterious_data))

    def get_summary(self):
        sorted_info = sorted(self.blocks_info, key=lambda x: x["b"], reverse=True)
        number_even_number = len(list(filter(is_even, self.blocks_info)))
        analysed_info = {
            "max_number": sorted_info[0]["b"],
            "min_number": sorted_info[-1]["b"],
            "first_number": self.blocks_info[0]["b"],
            "last_number": self.blocks_info[-1]["b"],
            "number_of_prime_numbers": len(list(filter(is_prime, self.blocks_info))),
            "number_of_even_numbers": number_even_number,
            "number_of_odd_numbers": len(self.blocks_info) - number_even_number
        }
        print(json.dumps(analysed_info, indent=4))
        if self.blocks < 100:
            self.restart()
            self.blocks += 1

    def restart(self):
        self.__init__(args["duration"])
        self.connect()
        self.start()
        self.get_summary()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helping Tome')
    parser.add_argument('-d', '--duration', help='Consume socket data duration in seconds', required=False, type=int,
                        default=60)

    args = vars(parser.parse_args())
    analyse = Analysis(args["duration"])
    analyse.connect()
    analyse.start()
    analyse.get_summary()
