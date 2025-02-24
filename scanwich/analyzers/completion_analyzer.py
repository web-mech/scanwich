from openai import OpenAI
import json

class CompletionAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def analyze_metrics(self, system_data, process_data):
        # Prepare the data for analysis
        analysis_prompt = f"""
        Analyze the following system metrics and process data for potential issues:
        
        System Metrics:
        {json.dumps(system_data, indent=2)}
        
        Top Processes:
        {json.dumps(process_data[:5], indent=2)}
        
        Please identify:
        1. Any unusual resource usage
        2. Potential performance issues
        3. Suspicious process behavior
        4. Recommendations for optimization
        """
        
        response = self.client.chat.completions.create(
            model="gpt-o1",
            messages=[
                {"role": "system", "content": "You are a system analysis expert focusing on performance and security."},
                {"role": "user", "content": analysis_prompt}
            ]
        )
        
        return response.choices[0].message.content 