# FinBen: Financial Benchmark for Language Models

FinBen is a comprehensive benchmark suite designed to evaluate the performance of large language models (LLMs) in financial contexts. It provides a collection of tasks and datasets tailored to assess various aspects of financial reasoning and understanding.

## Features

- **Diverse Financial Tasks**: FinBen includes a wide range of tasks covering areas such as financial document analysis, quantitative reasoning, and domain-specific language understanding.

- **Standardized Evaluation**: The benchmark offers standardized metrics and evaluation protocols, enabling consistent and reproducible assessments of LLMs in financial applications.

- **Integration with Evaluation Frameworks**: FinBen is compatible with existing evaluation frameworks, facilitating seamless integration into model assessment pipelines.

## Installation

To set up the FinBen environment, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/The-FinAI/FinBen.git
   cd FinBen/finlm_eval/
   ```

2. **Create and Activate a Conda Environment**:

   ```bash
   conda create -n finben python=3.12
   conda activate finben
   ```

3. **Install Dependencies**:

   ```bash
   pip install -e .
   pip install -e .[vllm]
   ```

## Usage

### Logging into Hugging Face

Set your Hugging Face token as an environment variable:

```bash
export HF_TOKEN="your_hf_token"
```

### Model Evaluation

1. **Navigate to the FinBen Directory**:

   ```bash
   cd FinBen/
   ```

2. **Set the VLLM Worker Multiprocessing Method**:

   ```bash
   export VLLM_WORKER_MULTIPROC_METHOD="spawn"
   ```

3. **Run Evaluation**:

   ```bash
   lm-eval --model hf-causal-experimental \
           --model_args pretrained=Qwen/Qwen2.5-72B-Instruct,trust_remote_code=True \
           --tasks plutus \
           --num_fewshot 0 \
           --batch_size 8 \
           --output_path ./results/YourProject/YourModelName
   ```

**Important Notes**:

- **Few-Shot Settings**:
  - *0-shot*: Use `--num_fewshot 0` and direct results to a corresponding repository.
  - *5-shot*: Use `--num_fewshot 5` and direct results to a corresponding repository.

- **Model Variants**:
  - *Base Models*: Omit the `apply_chat_template` argument.
  - *Chat Models*: Include the `apply_chat_template` argument.

## Greek Financial Application: Plutus

FinBen has been extended to address the unique challenges of the Greek financial domain through the Plutus initiative. This extension recognizes the linguistic complexity of Greek and the scarcity of domain-specific datasets, aiming to improve LLM performance in Greek financial contexts.

### Plutus Components

- **Plutus-ben**: A Greek Financial Evaluation Benchmark encompassing five core financial NLP tasks:
  - Numeric Named Entity Recognition (NER)
  - Textual NER
  - Question Answering (QA)
  - Abstractive Summarization
  - Topic Classification

  These tasks facilitate systematic and reproducible assessments of LLMs in the Greek financial domain.

### Significance

The Plutus initiative addresses the absence of dedicated Greek financial benchmarks and specialized Greek finance LLMs. By focusing on a low-resource language in finance, Plutus highlights the need for specialized training to understand and generate Greek financial language with nuance and accuracy. This effort ensures that Greek finance is not left behind in the AI revolution.

## Contributing

We welcome contributions to FinBen. If you're interested in adding new tasks, improving existing ones, or providing feedback, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

We extend our gratitude to the developers of the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) for providing a robust framework that inspired and facilitated the development of FinBen.

---

*For more information, visit our [GitHub repository](https://github.com/The-FinAI/FinBen).*
