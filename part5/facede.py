#外观模式

class Cpu:

    def run(self):
        print("cpu开始运行")

    def stop(self):
        print("cpu停止运行")

class Disk:

    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")

class Memory:

    def run(self):
        print("插上内存")

    def stop(self):
        print("拔掉内存")

class Computer:

    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

computer = Computer()
computer.run()
computer.stop()
