# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:40:52 2021

@author: Clara
"""

import time

io = {'x': 15, 'y': -2, 'z': -6}
europa = {'x': -5, 'y': -4, 'z': -11}
ganymede = {'x': 0, 'y': -6, 'z': 0}
callisto = {'x': 5, 'y': 9, 'z': 6}

moons = {
  'io': {
    'pos': io,
    'vel': {'x': 0, 'y': 0, 'z': 0}
  },
  'europa': {
    'pos': europa,
    'vel': {'x': 0, 'y': 0, 'z': 0}
  },
  'ganymede': {
    'pos': ganymede,
    'vel': {'x': 0, 'y': 0, 'z': 0}
  },
  'callisto': {
    'pos': callisto,
    'vel': {'x': 0, 'y': 0, 'z': 0}
  },
}

moon_pairs = set()
for i in moons:  # finds the combination of moon pairs --> there's probably a python library that does this better but hey ho.
  for j in moons:
    if (i is not j):
      k = sorted([i, j])
      moon_pairs.add(f"{k[0]}|{k[1]}")

def get_vel():
  for i in moon_pairs:
    (first, second) = i.split('|')
    for vector in ['x', 'y', 'z']:
      if moons[first]['pos'][vector] > moons[second]['pos'][vector]:
        moons[first]['vel'][vector]  -= 1
        moons[second]['vel'][vector]  += 1
      elif moons[first]['pos'][vector] < moons[second]['pos'][vector]:
        moons[first]['vel'][vector]  += 1
        moons[second]['vel'][vector]  -= 1

def get_pos():
  for i in moons:
    for vector in ['x', 'y', 'z']:
      moons[i]['pos'][vector] += moons[i]['vel'][vector]

def part_A():
  energy = 0
  for moon in moons:
    potential_energy = 0
    kinetic_energy = 0
    for vector in ['x', 'y', 'z']:
      potential_energy += abs(moons[moon]['pos'][vector])
      kinetic_energy += abs(moons[moon]['vel'][vector])
    energy += potential_energy * kinetic_energy
  return energy

for i in range(1000):
  get_vel()
  get_pos()

print('Part A: Total energy in the system =', part_A())

start = time.time()


def snapshot_system_axis(axis):
  assert axis in ['x', 'y', 'z']
  state = ""
  for index, moon in enumerate(moons):
    state += f"{moon}: "
    state += f"p{axis}: {moons[moon]['pos'][axis]}, "
    state += f"v{axis}: {moons[moon]['vel'][axis]}"
    if index != len(moons) - 1:
      state += ' | '
  return state

def get_sequence(axis):
  assert axis in ['x', 'y', 'z']
  positions = {}
  positions[snapshot_system_axis(axis)] = 0
  steps = 0

  while True:
    get_vel()
    get_pos()
    snapshot = snapshot_system_axis(axis)
    steps += 1
    if snapshot in positions:
      return steps - positions[snapshot]

    positions[snapshot] = steps

stepsX = get_sequence('x')
stepsY = get_sequence('y')
stepsZ = get_sequence('z')

def get_hcf(a, b): # Highest common factor
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

def get_lcm(a, b): # Lowest common multiple
  return (a * b) // get_hcf(a, b)

print('Part B: Number of steps =', get_lcm(stepsX, get_lcm(stepsY, stepsZ)))

print(time.time() - start, 'seconds')