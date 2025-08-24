import queue
import time
import threading

class Printer:
    def __init__(self):
        self.__print_list = queue.Queue()
        self.__pause_flag = threading.Event()
        self.__stop_flag = threading.Event()
        self.__worker = None
        
    def enqueue_print_job(self, item):
        self.__print_list.put(item)
        
    def  dequeue_print_job(self):
        if not self.__print_list.empty():
            return self.__print_list.get()
        return None
    
    def __str__(self):
        print("---- Danh sach in ----")
        for index, value in enumerate(list(self.__print_list.queue)):
            print(f"{index}. {value}")
        return ""
            
    def process_job(self):
        while not self.__print_list.empty():
            current_job = self.dequeue_print_job()
            print(f"Printing: {current_job}")
            time.sleep(2)
            
    def __print_worker(self):
        while not self.__stop_flag.is_set():
            if self.__pause_flag.is_set():
                time.sleep(0.2)
                continue
            job = self.dequeue_print_job()
            if job:
                print(f"Printing: {job}")
                time.sleep(2)
            else:
                time.sleep(0.5)
                
    def start(self):
        self.__stop_flag.clear()
        self.__pause_flag.clear()
        self.__worker = threading.Thread(target=self.__print_worker, daemon=True)
        self.__worker.start()
        
    def pause(self):
        self.__pause_flag.set()
        print("||Pause...")
        
    def resume(self):
        self.__pause_flag.clear()
        print("|>Resume printing...")
        
    def stop(self):
        self.__stop_flag.set()
        print("Stop printing...")
        
if __name__ == "__main__":
    printer = Printer()
    printer.enqueue_print_job("Văn bản 1")
    printer.enqueue_print_job("Văn bản 2")
    printer.enqueue_print_job("Văn bản 3")
    
    print(printer)
    
    printer.start()
    
    # pause 3s -> resume
    time.sleep(3)
    printer.pause()
    time.sleep(4)
    printer.resume()
    # chay them 4s -> dung
    time.sleep(4)
    printer.stop()