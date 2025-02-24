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
                # Gather base info
                process_info = proc.info
                
                # Count active network connections for this process (fallback measure for "network usage")
                connections_count = len(proc.net_connections())

                processes.append({
                    'pid': process_info['pid'],
                    'name': process_info['name'],
                    'cpu_percent': process_info['cpu_percent'],
                    'memory_percent': process_info['memory_percent'],
                    'connections_count': connections_count
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

    def get_network_info(self):
        """
        Retrieve system-wide network I/O counters (bytes/packets sent and received).
        """
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        } 