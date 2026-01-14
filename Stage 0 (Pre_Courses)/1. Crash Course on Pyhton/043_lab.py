class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
      
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      # OPTIMIZED LINE HERE
      machines[event.machine].discard(event.user)   # fix is here, we can use discard instead of remove (if user is there it will remove it if not it will just ignore it)
    # this fixes problem with chris being logged out without logging in first
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    # Ensure we only print machines that actually have active users
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

users = current_users(events)
generate_report(users)