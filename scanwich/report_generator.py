import os
import webbrowser
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    def __init__(self):
        self.reports_dir = Path.home() / '.scanwich' / 'reports'
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def generate_report(self, system_metrics, process_data, analysis):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Generate both MD and HTML reports
        md_content = self._generate_markdown(system_metrics, process_data, analysis)
        html_content = self._convert_to_html(md_content)
        
        # Save reports
        md_path = self.reports_dir / f'report_{timestamp}.md'
        html_path = self.reports_dir / f'report_{timestamp}.html'
        
        md_path.write_text(md_content)
        html_path.write_text(html_content)
        
        return str(md_path), str(html_path)

    def _generate_markdown(self, system_metrics, process_data, analysis):
        md = f"""# System Analysis Report
Generated: {system_metrics['timestamp']}

## System Metrics
- CPU Usage: {system_metrics['cpu_total']}%
- Memory Usage: {system_metrics['memory_total']}%

## Top Processes
| Process Name | PID | CPU % | Memory % |
|-------------|-----|-------|-----------|
"""
        for proc in process_data[:5]:  # Top 5 processes
            md += f"| {proc['name']} | {proc['pid']} | {proc['cpu_percent']:.1f} | {proc['memory_percent']:.1f} |\n"

        md += f"\n## AI Analysis\n{analysis}\n"
        return md

    def _convert_to_html(self, markdown_content):
        return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Scanwich Report</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css/github-markdown.min.css">
    <style>
        .markdown-body {{
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }}
    </style>
</head>
<body class="markdown-body">
    {self._md_to_html(markdown_content)}
</body>
</html>
"""

    def _md_to_html(self, md):
        try:
            import markdown
            return markdown.markdown(md, extensions=['tables'])
        except ImportError:
            # Fallback to basic HTML if markdown package is not installed
            return md.replace('\n', '<br>').replace('# ', '<h1>').replace('## ', '<h2>') 