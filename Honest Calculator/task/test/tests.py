from hstest import StageTest, CheckResult, WrongAnswer, dynamic_test, TestedProgram

msg = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are"]


def add_enter(txt):
    return "\n".join([txt, msg[0]])


def add_memory(txt):
    return "\n".join([txt, msg[4]])


data = [(("4 * 5.5", add_memory("22.0")), ("y", msg[5]), ("n", "")),
        (("11 * 11.1", add_memory("122.1")), ("y", msg[5]), ("n", "")),
        (("1 * 5", "\n".join([msg[9] + msg[6] + msg[7], add_memory("5.0")])), ("y", msg[5]), ("y", msg[0]),
         ("0 + M", "\n".join([msg[9] + msg[6] + msg[8], add_memory("5.0")])), ("y", msg[5]), ("n", "")),
        (("2 / M", "\n".join([msg[9] + msg[6], add_enter(msg[3])])), ("1 * M", "\n".join([msg[9] + "".join(msg[6:9]), add_memory("0.0")])), ("n", msg[5]), ("y", msg[0]),
         ("899 * 0", "\n".join([msg[9] + msg[8], add_memory("0.0")])), ("n", msg[5]), ("n", "")),
       ]  # (input data, msg sentence])


class HonestCalc(StageTest):
    @dynamic_test(data=data)
    def test(self, *items):
        pr = TestedProgram()
        output = pr.start()
        if msg[0] not in output:
            return CheckResult.wrong(f"Expected: ({msg[0]});\nFound:    ({output.strip()})")
        for item in items:
            output = pr.execute(item[0])
            if item[1] != output.strip():
                return CheckResult.wrong(f"Expected:\n{item[1]}\nFound:\n{output.strip()}")
        if not pr.is_finished():
            return CheckResult.wrong("Your program unnecessarily waiting for input.")
        return CheckResult.correct()


if __name__ == '__main__':
    HonestCalc().run_tests()
