#!/usr/bin/python3.11

import random
import typing
import time

def gen_event() -> typing.Generator[tuple, None, None]:
    players = ["ChatGPT", "Claude", "Kimi", "Grok", "Deepseek",
           "Gemini", "Qwen", "Muse", "Perplexity", "Mistral"]

    actions = ["Thinking", "Crashing", "Coding", "Typing", "Generating",
               "Optimizing", "resoning", "Fixing", "Debuging", "Reading",
               "Hacking", "Hallucinating", "Frabricating", 
               "Token-burning", "Sleeping"]
    while 1:
        name = random.choice(players)
        job = random.choice(actions)
        yield (name, job)

def main() -> int:
    gen1 = gen_event()
    for i in range(1000):
        time.sleep(0.007)
        name, job = next(gen1)
        print(f"Event {i}:", name, "is", job)
    return(1)


def consume_event(name: list[str, str]) -> list:
    total = len(name)

    while total:
        random.shuffle(name)
        winner = name.pop()
        print(f"{winner} is removed")
        total -= 1
        yield name



def main1() -> int:
    gen1 = gen_event()
    name = []
    for i in range(10):
        name.append(next(gen1))
    print(name)
    for i in consume_event(name):
        print("\ncurrent list:\n", name)


    return(1)
    
if __name__ == "__main__":
#    _ = main()
    _ = main1()

