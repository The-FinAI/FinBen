<div align="center">

<h1>FinBen</h1>

<p><b>A Holistic Financial Benchmark for Large Language Models</b></p>

[![arXiv](https://img.shields.io/badge/arXiv-2402.12659-b31b1b.svg)](https://arxiv.org/abs/2402.12659)
[![Hugging Face Collection](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Collection-yellow?logo=huggingface)](https://huggingface.co/collections/TheFinAI/finben-and-pixiu-english-financial-evaluation-658f515911f68f12ea193194)
[![Leaderboard](https://img.shields.io/badge/%F0%9F%A4%97%20Space-Leaderboard-yellow?logo=huggingface)](https://huggingface.co/spaces/TheFinAI/Open-FinLLM-Leaderboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Paper](https://arxiv.org/abs/2402.12659) · [Data](https://huggingface.co/collections/TheFinAI/finben-and-pixiu-english-financial-evaluation-658f515911f68f12ea193194) · [Leaderboard](https://huggingface.co/spaces/TheFinAI/Open-FinLLM-Leaderboard)

</div>

## Overview

FinBen is a comprehensive benchmark suite designed to evaluate the performance of large language models (LLMs) in financial contexts. It provides a collection of tasks and datasets tailored to assess various aspects of financial reasoning and understanding, with evaluation run through the `lm-eval` command line (inspired by [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)). FinBen has also been extended to the Greek financial domain through **Plutus**.

### Features

- **Diverse Financial Tasks**: FinBen includes a wide range of tasks covering areas such as financial document analysis, quantitative reasoning, and domain-specific language understanding.
- **Standardized Evaluation**: The benchmark offers standardized metrics and evaluation protocols, enabling consistent and reproducible assessments of LLMs in financial applications.
- **Integration with Evaluation Frameworks**: FinBen is compatible with existing evaluation frameworks, facilitating seamless integration into model assessment pipelines.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/The-FinAI/FinBen.git
   cd FinBen/finlm_eval/
   ```

2. **Create and activate a Conda environment**

   ```bash
   conda create -n finben python=3.12
   conda activate finben
   ```

3. **Install dependencies**

   ```bash
   pip install -e .
   pip install -e .[vllm]
   ```

## Usage

### Log in to Hugging Face

Set your Hugging Face token as an environment variable:

```bash
export HF_TOKEN="your_hf_token"
```

### Model Evaluation

1. **Navigate to the FinBen directory**

   ```bash
   cd FinBen/
   ```

2. **Set the vLLM worker multiprocessing method**

   ```bash
   export VLLM_WORKER_MULTIPROC_METHOD="spawn"
   ```

3. **Run evaluation**

   ```bash
   lm-eval --model hf-causal-experimental \
           --model_args pretrained=Qwen/Qwen2.5-72B-Instruct,trust_remote_code=True \
           --tasks plutus \
           --num_fewshot 0 \
           --batch_size 8 \
           --output_path ./results/YourProject/YourModelName
   ```

**Important notes**

- **Few-shot settings**
  - *0-shot*: Use `--num_fewshot 0` and direct results to a corresponding repository.
  - *5-shot*: Use `--num_fewshot 5` and direct results to a corresponding repository.
- **Model variants**
  - *Base models*: Omit the `apply_chat_template` argument.
  - *Chat models*: Include the `apply_chat_template` argument.

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

## Resources on Hugging Face

| Resource | Type | Description |
| --- | --- | --- |
| [FinBen & PIXIU — English financial evaluation](https://huggingface.co/collections/TheFinAI/finben-and-pixiu-english-financial-evaluation-658f515911f68f12ea193194) | Collection | FinBen evaluation datasets and related models |
| [Open FinLLM Leaderboard](https://huggingface.co/spaces/TheFinAI/Open-FinLLM-Leaderboard) | Space | Leaderboard of LLMs evaluated on FinBen |

## Contributing

We welcome contributions to FinBen. If you're interested in adding new tasks, improving existing ones, or providing feedback, please open an issue or submit a pull request.

## Acknowledgments

We extend our gratitude to the developers of the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) for providing a robust framework that inspired and facilitated the development of FinBen.

## Citation

If you find FinBen useful, please cite our paper:

```bibtex
@misc{xie2024finben,
      title={FinBen: A Holistic Financial Benchmark for Large Language Models},
      author={Qianqian Xie and Weiguang Han and Zhengyu Chen and Ruoyu Xiang and Xiao Zhang and Yueru He and Mengxi Xiao and Dong Li and Yongfu Dai and Duanyu Feng and Yijing Xu and Haoqiang Kang and Ziyan Kuang and Chenhan Yuan and Kailai Yang and Zheheng Luo and Tianlin Zhang and Zhiwei Liu and Guojun Xiong and Zhiyang Deng and Yuechen Jiang and Zhiyuan Yao and Haohang Li and Yangyang Yu and Gang Hu and Jiajia Huang and Xiao-Yang Liu and Alejandro Lopez-Lira and Benyou Wang and Yanzhao Lai and Hao Wang and Min Peng and Sophia Ananiadou and Jimin Huang},
      year={2024},
      eprint={2402.12659},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.12659}
}
```

## License

The code in this repository is released under the [MIT License](LICENSE). Datasets and models on Hugging Face keep their own licenses, stated on each card.

---

<div align="center">

Built by [The Fin AI](https://thefin.ai) · [Hugging Face](https://huggingface.co/TheFinAI) · [GitHub](https://github.com/The-FinAI)

</div>
