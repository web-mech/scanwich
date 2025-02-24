import psutil
import time
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.process_data = []
        
    def get_process_info(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                process_info = proc.info
                processes.append({
                    'pid': process_info['pid'],
                    'name': process_info['name'],
                    'cpu_percent': process_info['cpu_percent'],
                    'memory_percent': process_info['memory_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return processes

    def get_system_metrics(self):
        return {
            'cpu_total': psutil.cpu_percent(interval=1),
            'memory_total': psutil.virtual_memory().percent,
            'timestamp': datetime.now().isoformat()
        } 