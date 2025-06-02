class SingletionCpu:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletionCpu.__instance is not None:
            SingletionCpu.__instance = None
        return SingletionCpu.__instance

    def __init__(self, t):
        if SingletionCpu.__instance is not None:
            raise Exception("This class is a singleton! a process runing in cpu")
        else:
            SingletionCpu.__instance = self
            self.t = t
            print(f"process created! time: {self.t}")

    def __del__(self):
        del(self)
        print("process end.")


def run(p, n):
    print(f"{n} is runing.")
    if(p.t == 0):
        p.__del__()
        return
    else:
        SingletionCpu.getInstance()
    for i in range(0, 2):
        if(p.t == 0):
            p.__del__()
            return
        else:
            p.t = p.t-1
        print(f"time: {p.t}")


def processCpu():

    p1 = SingletionCpu(8)
    run(p1, "p1")
    p2 = SingletionCpu(6)
    run(p2, "p2")
    p3 = SingletionCpu(4)
    run(p3, "p3")

    run(p1, "p1")
    run(p2, "p2")
    run(p3, "p3")
    run(p1, "p1")
    run(p2, "p2")
    run(p1, "p1")

    # p4 = SingletionCpu(8)
    # p5 = SingletionCpu(8)


if __name__ == '__main__':
    processCpu()
