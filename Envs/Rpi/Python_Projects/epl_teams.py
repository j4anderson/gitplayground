#!/usr/bin/python3.2
# take an argument and respond:
# lets make it a little better

import sys

if len(sys.argv) == 2:
  team_name=sys.argv[1]
elif len(sys.argv) == 3:
  team_name=sys.argv[1]+" "+sys.argv[2]

if team_name == "Tottenham":
  print(team_name+" will win the EPL!")
else: 
  print(team_name+" will NOT win the EPL.")
