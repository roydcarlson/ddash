import threading, sys

is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as queue
else:
    import queue as queue

def console(q,lock):
    while 1:
        input()
        with lock:
            cmd = input('ddash> ')

        q.put(cmd)
        if cmd == 'quit':
            break

def who(lock):
    with lock:
        print "You are someone"

def exit(lock):
    with lock:
        print "Exiting ddash."

def invalid_input(lock):
    with lock:
        print "Unknown command."

def main():
    cmd_actions = {'who': who, 'exit':exit}
    cmd_queue = queue.Queue()
    stdout_lock = threading.Lock()

    dj = threading.Thread(target=console, args=(cmd_queue, stdout_lock))
    dj.start()

    while 1:
        cmd = cmd_queue.get()
        if cmd == 'quit':
            break
        action = cmd_actions.get(cmd,invalid_input)
        action(stdout_lock)

main()


