import re

f = open("Day5/input", "r")
lines = [line.replace('\n', '') for line in f]
f.close()

def get_stacks(stack_piles):
  stacks = {}
  columns = stack_piles.pop()
  stacks_num = int(columns[len(columns)-1])

  stack_piles.reverse()
  for i in range(1, stacks_num+1):
    stacks[i] = []
  for level in stack_piles:
    stack_no=1
    for i in range(1, len(level), 4):
      if level[i].isalpha():
        stacks[stack_no].append(level[i])
      stack_no += 1
  return stacks

def get_data():
  instructions = [re.split('move|from|to', l) for l in lines if 'move' in l]
  stacks = get_stacks([l for l in lines if 'move' not in l and l != ''])

  return (stacks, instructions)


def crate_mover_9000(stacks, move, fromm, to):
    for _ in range(move):
      stacks[to].append(stacks[fromm].pop())

def crate_mover_9001(stacks, move, fromm, to):
    stacks[to] = stacks[to] + stacks[fromm][-move::]
    del stacks[fromm][-move:]

def execute_instructions(crate_mover, stacks, instructions):
  for inst in instructions:
    move = int(inst[1])
    fromm = int(inst[2])
    to = int(inst[3])
    crate_mover(stacks, move, fromm, to)
  return stacks


def p1():
  stacks, instructions = get_data()
  arranged_stacks = execute_instructions(crate_mover_9000, stacks, instructions)
  print(''.join([arranged_stacks[stack_no][-1] for stack_no in list(arranged_stacks.keys()) ]))

def p2():
  stacks, instructions = get_data()
  arranged_stacks = execute_instructions(crate_mover_9001, stacks, instructions)
  print(''.join([arranged_stacks[stack_no][-1] for stack_no in list(arranged_stacks.keys()) ]))

def day5():
  p1()
  p2()
