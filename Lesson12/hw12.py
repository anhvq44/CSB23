def enqueue_print_job(print_queue, new_item):
    print_queue.append(new_item)

def dequeue_print_job(print_queue):
    return print_queue.pop(0)


queue = []

enqueue_print_job(queue, "Document 1")
enqueue_print_job(queue, "Copy of TASK: Source Analysis")
enqueue_print_job(queue, "Vocab Set 1")

while queue:
    current_job = dequeue_print_job(queue)
    print(f"Printing: {current_job}")