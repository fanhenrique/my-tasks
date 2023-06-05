count = 1

def find_missing(x):
  x.sort()
  difference = list(set(range(x[0], x[-1]+1)).difference(x))
  
  return difference[0] if len(difference) else x[-1]+1


def hash_timeline(hash_timeline, date):
  
  global count
  
  value = hash_timeline.get(date)

  if value is None:
    value = count
    hash_timeline[date] = count
    count += 1

  return value