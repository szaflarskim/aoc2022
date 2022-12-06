f = open("Day6/input", "r")
lines = f.readlines()
f.close()


def get_marker_start(buffer_stream, marker_start=4):
  partial=[]
  for i, c in enumerate(buffer_stream, start=1):
    partial.append(c)
    if i >= marker_start and len(set(partial[-marker_start::1])) >= marker_start:
      return i

def get_packet_start(buffer_stream):
  return get_marker_start(buffer_stream, marker_start=4)

def get_message_start(buffer_stream):
  return get_marker_start(buffer_stream, marker_start=14)
  
def p1():
    print(get_packet_start(lines[0]))

def p2():
    print(get_message_start(lines[0]))

def day6():
    p1()
    p2()
