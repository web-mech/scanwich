.PHONY: install clean run dev-setup help

# Default Python interpreter
PYTHON := python3
VENV := venv

help:
	@echo "Available commands:"
	@echo "  make install    - Install scanwich in development mode"
	@echo "  make clean      - Remove build artifacts and virtual environment"
	@echo "  make run        - Run scanwich system monitor"
	@echo "  make dev-setup  - Set up development environment"

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip

install: $(VENV)/bin/activate
	$(VENV)/bin/pip install -e .

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf $(VENV)/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	@echo "Note: Configuration in ~/.scanwich is preserved"

run: install
	$(VENV)/bin/scanwich

dev-setup: install
	$(VENV)/bin/pip install pytest black flake8

# If OPENAI_API_KEY is not set, prompt for it
check-api-key:
	@if [ -z "$$OPENAI_API_KEY" ]; then \
		echo "OPENAI_API_KEY is not set. Please set it first:"; \
		echo "export OPENAI_API_KEY='your-api-key-here'"; \
		exit 1; \
	fi 