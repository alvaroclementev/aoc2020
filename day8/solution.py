"""
Solutions to Day 8 of Advent of Code by Alvaro Clemente
"""


def parse_input(filename="input.txt"):
    """
    The answers for a group are in a block (delimited by empty lines)
    For each group the answers for each person are in a line
    """
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def process_lines(lines):
    """
    The first 5 bits represent the row, FB as a binary number where F == 1 and B == 0
    The same can be applied to the last 3 elements which should be the column
    """
    ops = []
    for line in lines:
        op, num = line.split(" ", 1)
        num = int(num)
        ops.append((op, num))
    return ops


# Parsed input
lines = parse_input()
ops = process_lines(lines)

# Solution for #1
class DuplicatedInstructionException(Exception):
    pass


class VM:
    def __init__(self, instructions):
        self.instructions = instructions
        self._ic = 0
        self.accumulator = 0
        self._ran_instructions = set()

    def run_next(self):
        if self._ic < 0 or self._ic > len(self.instructions):
            # invalid state
            raise valueerror(
                f"invalid state {self._ic} for {len(self.instructions)} instructions"
            )
        elif self._ic == len(self.instructions):
            # do nothing, we are done
            return None

        # check for loops
        if self._ic in self._ran_instructions:
            raise DuplicatedInstructionException()
        else:
            self._ran_instructions.add(self._ic)

        op, value = self.instructions[self._ic]
        if op == "acc":
            self.accumulator += value
            self._ic += 1
        elif op == "jmp":
            self._ic += value
        elif op == "nop":
            self._ic += 1
        else:
            raise valueerror(op)
        return self._ic

    def run(self, raise_on_error=False):
        """
        run until an exception occurs or a None is returned
        """
        try:
            while True:
                res = vm.run_next()
                if res is None:
                    break
        except DuplicatedInstructionException as e:
            if raise_on_error:
                raise e
            print(
                f"duplicated instruction {self._ic} ({self.instructions[self._ic]}):"
                f" acc = {self.accumulator}"
            )
        except Exception as e:
            if raise_on_error:
                raise e
            print(f"{e}")
        return self.accumulator


vm = VM(ops)
print(vm.run())


# Solution for #2
# We try a brute-force approach, but most certainly we could make a graph and
# use graph properties to compute the min set of changes to make it acylcic
for i, (op_code, value) in enumerate(ops):
    # We modify a single instruction
    head = ops[:i].copy()
    if i < len(ops) - 1:
        tail = ops[i + 1 :].copy()
    else:
        tail = []
    if op_code == "nop":
        new_op_code = "jmp"
    elif op_code == "jmp":
        new_op_code = "nop"
    else:
        continue
    new_ops = head + [(new_op_code, value)] + tail
    vm = VM(new_ops)
    try:
        vm.run(raise_on_error=True)
    except DuplicatedInstructionException:
        continue
    except Exception as e:
        print(f"{e}")
        break
    else:
        # We found the correct change!
        print(vm.accumulator)
        break
