# Scanwich 🥪

Scanwich is an AI-powered system monitoring tool that analyzes your system's processes and memory usage using OpenAI's GPT models to provide intelligent insights.

## Features

- Real-time system resource monitoring
- Process CPU and memory usage tracking
- AI-powered analysis of system behavior
- Automatic configuration management
- Easy-to-use command line interface

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Make (optional, for easier installation)

## Installation

### Using Make (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/web-mech/scanwich.git
   cd scanwich
   ```
2. Install dependencies:
   ```bash
   make install
   ```
3. Set up your OpenAI API key:
   - You can export your key in the environment:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - Alternatively, if you run Scanwich (or make run) without a key configured, you will be prompted to enter one.

### Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scanwich.git
   cd scanwich
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   Or, simply run the tool once, and you will be prompted to enter a key if one is not detected.

## Usage

### Basic Monitoring

Start Scanwich with default settings:


```bash
scanwich monitor
```

### Advanced Options

Monitor specific processes:

```bash
scanwich monitor --process-name "python,chrome"
```

Set custom refresh interval:

```bash
scanwich monitor --interval 5
```

Generate AI analysis report:

```bash
scanwich analyze --output report.txt
```

### Configuration

Edit the configuration file at `~/.scanwich/config.yaml`:
```yaml
refresh_rate: 2
processes_to_monitor: []
memory_threshold: 90
cpu_threshold: 80
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

