# LLMs and VLMs

Technical reports for language, reasoning, code, vision-language, and omni
models. Speech models are on the [Speech and Audio](speech-and-audio.md)
page. See the [README](README.md) for scope and conventions.

**Open-weight labs**
[Google](#google) ·
[Alibaba (Qwen)](#alibaba-qwen) ·
[DeepSeek](#deepseek) ·
[Mistral AI](#mistral-ai) ·
[NVIDIA](#nvidia) ·
[Zhipu AI / Z.ai (GLM)](#zhipu-ai--zai-glm) ·
[Cohere](#cohere) ·
[Poolside](#poolside) ·
[Meta](#meta) ·
[Microsoft (Phi)](#microsoft-phi) ·
[Ai2](#ai2) ·
[Moonshot AI (Kimi)](#moonshot-ai-kimi) ·
[MiniMax](#minimax) ·
[Other Open Labs](#other-open-labs)

**Closed frontier labs**
[OpenAI](#openai) ·
[Anthropic](#anthropic)

---

## Google

### Gemma

- 2024-03 · [Gemma: Open Models Based on Gemini Research and Technology](https://arxiv.org/abs/2403.08295)
- 2024-04 · [RecurrentGemma: Moving Past Transformers for Efficient Open Language Models](https://arxiv.org/abs/2404.07839)
- 2024-06 · [CodeGemma: Open Code Models Based on Gemma](https://arxiv.org/abs/2406.11409)
- 2024-07 · [Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118)
- 2024-07 · [PaliGemma: A versatile 3B VLM for transfer](https://arxiv.org/abs/2407.07726)
- 2024-12 · [PaliGemma 2: A Family of Versatile VLMs for Transfer](https://arxiv.org/abs/2412.03555)
- 2025-03 · [Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786)
- 2025-06 · [Gemma 3n](https://ai.google.dev/gemma/docs/gemma-3n) *(model docs)*
- 2026-07 · [Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770)

### Gemini and PaLM (closed)

- 2022-04 · [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)
- 2023-05 · [PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403)
- 2023-12 · [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805)
- 2024-03 · [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/abs/2403.05530)
- 2025-07 · [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261)
- 2025-11 · [Gemini 3 Pro Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf) *(model card)*. Later cards are on the [DeepMind model cards page](https://deepmind.google/models/model-cards/).

## Alibaba (Qwen)

### Qwen LLMs

- 2023-09 · [Qwen Technical Report](https://arxiv.org/abs/2309.16609)
- 2024-07 · [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671)
- 2024-12 · [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115)
- 2025-01 · [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383)
- 2025-05 · [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- 2026-02 · [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5) *(blog)*

### Qwen Code and Math

- 2024-09 · [Qwen2.5-Coder Technical Report](https://arxiv.org/abs/2409.12186)
- 2024-09 · [Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement](https://arxiv.org/abs/2409.12122)
- 2026-02 · [Qwen3-Coder-Next Technical Report](https://arxiv.org/abs/2603.00729)

### Qwen Vision-Language and Omni

- 2023-08 · [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966)
- 2024-09 · [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191)
- 2025-02 · [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923)
- 2025-03 · [Qwen2.5-Omni Technical Report](https://arxiv.org/abs/2503.20215)
- 2025-09 · [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765)
- 2025-11 · [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)
- 2026-04 · [Qwen3.5-Omni Technical Report](https://arxiv.org/abs/2604.15804)

## DeepSeek

### DeepSeek LLMs

- 2024-01 · [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](https://arxiv.org/abs/2401.02954)
- 2024-01 · [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)
- 2024-05 · [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)
- 2024-12 · [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
- 2025-12 · [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556)
- 2026-04 · [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

### DeepSeek Reasoning and Math

- 2024-02 · [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
- 2025-01 · [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- 2025-04 · [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801)

### DeepSeek Coder

- 2024-01 · [DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence](https://arxiv.org/abs/2401.14196)
- 2024-06 · [DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence](https://arxiv.org/abs/2406.11931)

### DeepSeek Multimodal

- 2024-03 · [DeepSeek-VL: Towards Real-World Vision-Language Understanding](https://arxiv.org/abs/2403.05525)
- 2024-10 · [Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2410.13848)
- 2024-12 · [DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding](https://arxiv.org/abs/2412.10302)
- 2025-01 · [Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling](https://arxiv.org/abs/2501.17811)
- 2025-10 · [DeepSeek-OCR: Contexts Optical Compression](https://arxiv.org/abs/2510.18234)

## Mistral AI

- 2023-10 · [Mistral 7B](https://arxiv.org/abs/2310.06825)
- 2024-01 · [Mixtral of Experts](https://arxiv.org/abs/2401.04088)
- 2024-10 · [Pixtral 12B](https://arxiv.org/abs/2410.07073)
- 2025-06 · [Magistral](https://arxiv.org/abs/2506.10910)
- 2025-12 · [Introducing Mistral 3](https://mistral.ai/news/mistral-3/) *(blog)*. This covers Mistral Large 3 and Ministral 3.
- 2026-01 · [Ministral 3](https://arxiv.org/abs/2601.08584)

## NVIDIA

### Nemotron LLMs

- 2024-02 · [Nemotron-4 15B Technical Report](https://arxiv.org/abs/2402.16819)
- 2024-06 · [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704)
- 2024-07 · [Compact Language Models via Pruning and Knowledge Distillation](https://arxiv.org/abs/2407.14679) (Minitron)
- 2025-04 · [Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models](https://arxiv.org/abs/2504.03624)
- 2025-05 · [Llama-Nemotron: Efficient Reasoning Models](https://arxiv.org/abs/2505.00949)
- 2025-08 · [NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model](https://arxiv.org/abs/2508.14444)
- 2025-12 · [NVIDIA Nemotron 3: Efficient and Open Intelligence](https://arxiv.org/abs/2512.20856)
- 2026-04 · [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374)

### Nemotron Multimodal

- 2024-09 · [NVLM: Open Frontier-Class Multimodal LLMs](https://arxiv.org/abs/2409.11402)
- 2026-04 · [Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence](https://arxiv.org/abs/2604.24954)

## Zhipu AI / Z.ai (GLM)

### GLM LLMs

- 2022-10 · [GLM-130B: An Open Bilingual Pre-trained Model](https://arxiv.org/abs/2210.02414)
- 2024-06 · [ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools](https://arxiv.org/abs/2406.12793)
- 2025-08 · [GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models](https://arxiv.org/abs/2508.06471)
- 2026-02 · [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763)

### GLM Vision-Language

- 2023-11 · [CogVLM: Visual Expert for Pretrained Language Models](https://arxiv.org/abs/2311.03079)
- 2025-07 · [GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning](https://arxiv.org/abs/2507.01006)
- 2026-04 · [GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents](https://arxiv.org/abs/2604.26752)

## Cohere

### Command

- 2025-04 · [Command A: An Enterprise-Ready Large Language Model](https://arxiv.org/abs/2504.00698)

### Aya (Cohere Labs)

- 2024-02 · [Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model](https://arxiv.org/abs/2402.07827)
- 2024-05 · [Aya 23: Open Weight Releases to Further Multilingual Progress](https://arxiv.org/abs/2405.15032)
- 2024-12 · [Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier](https://arxiv.org/abs/2412.04261)
- 2025-05 · [Aya Vision: Advancing the Frontier of Multilingual Multimodality](https://arxiv.org/abs/2505.08751)
- 2026-03 · [Tiny Aya: Bridging Scale and Multilingual Depth](https://arxiv.org/abs/2603.11510)

## Poolside

### Laguna

- 2026-05 · [Introducing Laguna XS.2 and Laguna M.1](https://poolside.ai/blog/introducing-laguna-xs2-m1) *(blog)*
- 2026-05 · [Laguna M.1/XS.2 Technical Report](https://arxiv.org/abs/2605.27605)

## Meta

### Llama

- 2023-02 · [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
- 2023-07 · [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)
- 2023-08 · [Code Llama: Open Foundation Models for Code](https://arxiv.org/abs/2308.12950)
- 2024-07 · [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)
- 2025-04 · [The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) *(blog)*

### Chameleon

- 2024-05 · [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818)

## Microsoft (Phi)

- 2023-06 · [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) (phi-1)
- 2023-09 · [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
- 2024-04 · [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219)
- 2024-12 · [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)
- 2025-03 · [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
- 2025-04 · [Phi-4-reasoning Technical Report](https://arxiv.org/abs/2504.21318)
- 2026-03 · [Phi-4-reasoning-vision-15B Technical Report](https://arxiv.org/abs/2603.03975)

## Ai2

Ai2's reports are fully open: they release the data, code, and intermediate
checkpoints along with the weights.

### OLMo

- 2024-02 · [OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838)
- 2024-09 · [OLMoE: Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2409.02060)
- 2024-12 · [2 OLMo 2 Furious](https://arxiv.org/abs/2501.00656)
- 2025-12 · [Olmo 3](https://arxiv.org/abs/2512.13961)

### Tülu and Molmo

- 2024-09 · [Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models](https://arxiv.org/abs/2409.17146)
- 2024-11 · [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124)

## Moonshot AI (Kimi)

- 2025-01 · [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/abs/2501.12599)
- 2025-04 · [Kimi-VL Technical Report](https://arxiv.org/abs/2504.07491)
- 2025-07 · [Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534)
- 2025-10 · [Kimi Linear: An Expressive, Efficient Attention Architecture](https://arxiv.org/abs/2510.26692)
- 2026-02 · [Kimi K2.5: Visual Agentic Intelligence](https://arxiv.org/abs/2602.02276)

## MiniMax

- 2025-01 · [MiniMax-01: Scaling Foundation Models with Lightning Attention](https://arxiv.org/abs/2501.08313)
- 2025-06 · [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](https://arxiv.org/abs/2506.13585)
- 2026-05 · [The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence](https://arxiv.org/abs/2605.26494)

## Other Open Labs

### Hugging Face

- 2025-02 · [SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737)
- 2025-04 · [SmolVLM: Redefining small and efficient multimodal models](https://arxiv.org/abs/2504.05299)

### Tencent (Hunyuan)

- 2024-11 · [Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent](https://arxiv.org/abs/2411.02265)

### Xiaomi (MiMo)

- 2025-05 · [MiMo: Unlocking the Reasoning Potential of Language Model -- From Pretraining to Posttraining](https://arxiv.org/abs/2505.07608)
- 2025-06 · [MiMo-VL Technical Report](https://arxiv.org/abs/2506.03569)
- 2026-01 · [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780)
- 2026-04 · [MiMo-V2.5](https://mimo.xiaomi.com/mimo-v2-5/) *(blog)*
- 2026-09 · [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf)

---

## OpenAI

### GPT

- 2018-06 · [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) (GPT-1)
- 2019-02 · [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (GPT-2)
- 2020-05 · [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (GPT-3)
- 2022-03 · [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) (InstructGPT)
- 2023-03 · [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774)
- 2024-10 · [GPT-4o System Card](https://arxiv.org/abs/2410.21276)
- 2024-12 · [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720)
- 2025-08 · [OpenAI GPT-5 System Card](https://arxiv.org/abs/2601.03267)

### gpt-oss (open-weight)

- 2025-08 · [gpt-oss-120b & gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925)

## Anthropic

### Foundational Papers

- 2021-12 · [A General Language Assistant as a Laboratory for Alignment](https://arxiv.org/abs/2112.00861)
- 2022-04 · [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862)
- 2022-12 · [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)

### Claude Model and System Cards

- 2024-03 · [The Claude 3 Model Family: Opus, Sonnet, Haiku](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- 2025-05 · [System Card: Claude Opus 4 & Claude Sonnet 4](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf)
- 2025-11 · [System Card: Claude Opus 4.5](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)
- 2026-05 · [System Card: Claude Opus 4.8](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)
- All system cards are listed on [anthropic.com/system-cards](https://www.anthropic.com/system-cards).
