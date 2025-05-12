# DSPy Implementation Speedrun

## Project Overview

This project is a "speedrun" exploration into various implementations and use cases of the **DSPy framework**. The primary goal is to rapidly prototype and document different ways DSPy can be leveraged for building and optimizing language model-based applications.

The focus is on practical examples, quick iterations, and learning through doing.

## Purpose

*   To serve as a personal collection of DSPy implementation patterns.
*   To quickly test and understand different DSPy features and modules.
*   To experiment with integrating DSPy with various language models and tools.
*   To document common challenges and solutions encountered during rapid DSPy development.

## Implementations Explored (Examples - Add your specific modules here)

This project aims to cover a range of DSPy functionalities. As the speedrun progresses, examples might include:

*   **Basic Signatures and Predictors:** Demonstrating core DSPy concepts.
*   **Few-shot Learning:** Using `dspy.Predict` with examples.
*   **Optimizers:** Exploring teleprompters like `BootstrapFewShot` or `MIPRO`.
*   **Modules:** Building custom DSPy modules.
*   **Retrieval Augmented Generation (RAG):** Simple RAG pipelines with `dspy.Retrieve`.
*   **Multi-hop Reasoning:** Implementing `ChainOfThought` or more complex reasoning patterns.
*   **Tool Use / Agents:** Integrating external tools or building simple agentic behaviors.
*   **Specific Model Integrations:** Showcasing DSPy with different LLMs (e.g., Gemini, OpenAI models, local models).
*   **Image Generation & Multimodal (if applicable):** As seen with the `ImagePredict` and `ImageGenerator` examples.

## Getting Started

### Prerequisites

*   Python 3.9+
*   [uv](https://github.com/astral-sh/uv) (for package management, as per `makefile`)
*   API keys for relevant services (e.g., Gemini, Fal AI) set up as environment variables or in a `.env` file (see `app/core/config.py`).

### Installation & Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repo-url>
    cd dspy-speedrun
    ```
2.  **Install dependencies:**
    The `makefile` uses `uv` for environment and package management.
    ```bash
    make install
    ```
    This will sync dependencies from `pyproject.toml`.

### Running the Application

The main entry point for examples can typically be run using:

```bash
make run
```

This command executes `app.main` as a module. Refer to the `makefile` for other available commands like linting, formatting, and cleaning.

## Contributing

As this is a personal speedrun project, direct contributions might not be the focus. However, feel free to fork, learn, and adapt any code for your own explorations!

---