# Simple agent built with LangGraph

## In order to start the program:

1. Add OPENAI_API_KEY env var to .env file.

2. Create python virtual environment:

```bash
    conda create --name llm_agent
```

3. Activate the virtual environment:

```bash
    conda activate llm_agent
```

4. Install dependencies:

```bash
    pip install -r requirements.txt
```

5. Run the program (model tempreture can be set with --temperature flag)

```bash
    python3 main.py --temperature 0.8
```