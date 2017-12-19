"""
http://adventofcode.com/2017/day/18

This one isn't Py2 compatible sorry
"""
from collections import defaultdict
from queue import Queue, Empty


def int_or_regfetch(registers, i):
    # type: (dict, str) -> int
    # i could be an integer or a character referring to a register, unwrap either
    if i.isalpha():
        return registers[i]
    return int(i)


with open('18.in', 'r') as f:
    instructions = f.readlines()


# Part 1
registers = defaultdict(lambda: 0)
last_frequency = None
pointer = 0
while True:
    instr = instructions[pointer]
    cmd, *args = instr.strip().split(' ')

    if cmd == 'snd':
        if registers[args[0]]:
            last_frequency = registers[args[0]]
    elif cmd == 'set':
        registers[args[0]] = int_or_regfetch(registers, args[1])
    elif cmd == 'add':
        registers[args[0]] += int_or_regfetch(registers, args[1])
    elif cmd == 'mul':
        registers[args[0]] *= int_or_regfetch(registers, args[1])
    elif cmd == 'mod':
        registers[args[0]] %= int_or_regfetch(registers, args[1])
    elif cmd == 'rcv':
        if registers[args[0]] and last_frequency:
            break
    elif cmd == 'jgz':
        if registers[args[0]] > 0:
            pointer += int(args[1])
            continue

    pointer += 1

print(last_frequency)


# Part 2
class Program(object):
    def __init__(self, instructions, pid):
        self.instructions = instructions
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = pid
        self.receive_queue = Queue()
        self.pointer = 0

    @property
    def is_blocked(self):
        return self.instructions[self.pointer].startswith('rcv') and self.receive_queue.empty()

    def run_until_blocked(self):
        while True:
            instr = self.instructions[self.pointer]
            cmd, *args = instr.strip().split(' ')

            if cmd == 'snd':
                yield int_or_regfetch(self.registers, args[0])
            elif cmd == 'set':
                self.registers[args[0]] = int_or_regfetch(self.registers, args[1])
            elif cmd == 'add':
                self.registers[args[0]] += int_or_regfetch(self.registers, args[1])
            elif cmd == 'mul':
                self.registers[args[0]] *= int_or_regfetch(self.registers, args[1])
            elif cmd == 'mod':
                self.registers[args[0]] %= int_or_regfetch(self.registers, args[1])
            elif cmd == 'rcv':
                try:
                    self.registers[args[0]] = self.receive_queue.get_nowait()
                except Empty:
                    return
            elif cmd == 'jgz':
                if int_or_regfetch(self.registers, args[0]) > 0:
                    self.pointer += int_or_regfetch(self.registers, args[1])
                    continue

            self.pointer += 1


program_0 = Program(instructions, 0)
program_1 = Program(instructions, 1)
sent_from_1 = 0
while not (program_0.is_blocked and program_1.is_blocked):
    for msg in program_0.run_until_blocked():
        program_1.receive_queue.put(msg)
    for msg in program_1.run_until_blocked():
        sent_from_1 += 1
        program_0.receive_queue.put(msg)

print(sent_from_1)
