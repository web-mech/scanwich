import time
import json
from openai import OpenAI

class AssistantAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        # Create an assistant specialized in system analysis
        self.assistant = self.client.beta.assistants.create(
            name="System Analyzer",
            description="Expert system analyzer focusing on performance and security analysis",
            model="gpt-4-turbo-preview",  # Most powerful model available
            tools=[{"type": "code_interpreter"}],  # Enables data analysis capabilities
        )

    def analyze_metrics(self, system_data, process_data):
        # Create a thread for this analysis
        thread = self.client.beta.threads.create()
        
        # Add the analysis request to the thread
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"""
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
            
            Feel free to use code interpretation to analyze patterns or create visualizations if helpful.
            """
        )
        
        # Run the analysis
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant.id
        )
        
        # Wait for completion
        while True:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run.status == 'completed':
                break
            time.sleep(1)  # Add small delay between checks
        
        # Get the response
        messages = self.client.beta.threads.messages.list(thread_id=thread.id)
        return messages.data[0].content[0].text.value