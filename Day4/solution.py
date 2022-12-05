f=open("Day4/input", "r")
lines = [line.rstrip() for line in f]
f.close()

def get_sections():
  sections=[]
  ranges = [[s for s in l.split(',')] for l in lines ]
  for r in ranges:
    e1 = r[0].split('-')
    e2 = r[1].split('-')
    
    s1 = set(range(int(e1[0]) ,int(e1[1]) +1)) 
    s2 = set(range(int(e2[0]) ,int(e2[1]) + 1)) 
    
    sections.append((s1,s2))
  
  return sections

def p1():
  s=get_sections()
  print(len([sec for sec in s if sec[0].issubset(sec[1]) or sec[0].issuperset(sec[1])]))
  
  
def p2():
  s=get_sections()
  print(len([sec for sec in s if sec[0].intersection(sec[1]) ]))
  
def day4():
  p1()
  p2()
