import time
import webbrowser
from .process_monitor import SystemMonitor
from .analyzers.assistant_analyzer import AssistantAnalyzer
from .config_manager import ConfigManager
from .report_generator import ReportGenerator

def main():
    # Initialize components
    config = ConfigManager()
    api_key = config.setup_config()
    
    monitor = SystemMonitor()
    analyzer = AssistantAnalyzer(api_key)
    reporter = ReportGenerator()
    
    print("Scanwich is now monitoring your system...")
    
    while True:
        try:
            # Collect system and process data
            system_metrics = monitor.get_system_metrics()
            process_data = monitor.get_process_info()
            
            # Collect network data (system-wide)
            network_metrics = monitor.get_network_info()
            
            # Filter out None CPU usage values
            process_data = [p for p in process_data if p['cpu_percent'] is not None]
            
            # Sort and identify top CPU-consuming processes
            cpu_sorted = sorted(process_data, key=lambda x: x['cpu_percent'], reverse=True)
            top_cpu = cpu_sorted[:5]
            
            # Sort and identify top memory-consuming processes
            mem_sorted = sorted(process_data, key=lambda x: x['memory_percent'], reverse=True)
            top_mem = mem_sorted[:5]
            
            # Sort and identify processes with the most network connections
            net_sorted = sorted(process_data, key=lambda x: x['connections_count'], reverse=True)
            top_net = net_sorted[:5]
            
            # AI analysis (includes suspicious behavior or optimization suggestions)
            analysis = analyzer.analyze_metrics(system_metrics, process_data)

            # Generate and save reports (now including top metrics)
            md_path, html_path = reporter.generate_report(
                system_metrics, 
                process_data, 
                analysis, 
                network_metrics,
                top_metrics={
                    'cpu': top_cpu,
                    'memory': top_mem,
                    'network': top_net
                }
            )
            
            # Print only basic status information
            print(f"\nReports generated:")
            print(f"Markdown: {md_path}")
            print(f"HTML: {html_path}")
            webbrowser.open(html_path)
            # Wait before next analysis
            time.sleep(60)  # Adjust interval as needed
            
        except KeyboardInterrupt:
            print("\nScanwich monitoring stopped by user")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()