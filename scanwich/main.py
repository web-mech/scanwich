import time
import webbrowser
from .process_monitor import SystemMonitor
#from .analyzers.completion_analyzer import CompletionAnalyzer
from .analyzers.assistant_analyzer import AssistantAnalyzer
from .config_manager import ConfigManager
from .report_generator import ReportGenerator

def main():
    # Initialize components
    config = ConfigManager()
    api_key = config.setup_config()
    
    monitor = SystemMonitor()
    #analyzer = CompletionAnalyzer(api_key)
    analyzer = AssistantAnalyzer(api_key)
    reporter = ReportGenerator()
    
    print("Scanwich is now monitoring your system...")
    
    while True:
        try:
            # Collect system and process data
            system_metrics = monitor.get_system_metrics()
            process_data = monitor.get_process_info()
            
            # Filter out None values and then sort
            process_data = [p for p in process_data if p['cpu_percent'] is not None]
            process_data.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            # Get AI analysis
            analysis = analyzer.analyze_metrics(system_metrics, process_data)
            
            # Generate and save reports
            md_path, html_path = reporter.generate_report(system_metrics, process_data, analysis)
            
            # Print basic results to console
            print("\n=== System Analysis ===")
            print(f"Time: {system_metrics['timestamp']}")
            print(f"CPU Usage: {system_metrics['cpu_total']}%")
            print(f"Memory Usage: {system_metrics['memory_total']}%")
            
            # Open HTML report in browser
            webbrowser.open(f'file://{html_path}')
            print(f"\nReports generated:")
            print(f"Markdown: {md_path}")
            print(f"HTML: {html_path}")
            
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