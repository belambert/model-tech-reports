# Speech and Audio

Technical reports for speech and audio models. This page currently focuses on
automatic speech recognition (ASR), including models that also do speech
translation. See the [README](README.md) for scope and conventions.

**Open-weight labs**
[NVIDIA](#nvidia) ·
[OpenAI](#openai) ·
[Alibaba (Qwen)](#alibaba-qwen) ·
[Mistral AI](#mistral-ai) ·
[Meta](#meta) ·
[Microsoft](#microsoft) ·
[Kyutai](#kyutai) ·
[Other Open Labs](#other-open-labs) ·
[Academic](#academic)

**Closed labs**
[Google](#google)

---

## NVIDIA

### FastConformer and TDT (Architecture)

These papers describe the encoder and decoder that the Parakeet and Canary
models are built on.

- 2023-04 · [Efficient Sequence Transduction by Jointly Predicting Tokens and Durations](https://arxiv.org/abs/2304.06795) (TDT)
- 2023-05 · [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084)

### Parakeet and Canary

- 2024-06 · [Less is More: Accurate Speech Recognition & Translation without Web-Scale Data](https://arxiv.org/abs/2406.19674) (Canary-1B)
- 2025-05 · [parakeet-tdt-0.6b-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) *(model card)*
- 2025-05 · [Granary: Speech Recognition and Translation Dataset in 25 European Languages](https://arxiv.org/abs/2505.13404). This is the training data for the v3 models.
- 2025-09 · [Canary-1B-v2 & Parakeet-TDT-0.6B-v3: Efficient and High-Performance Models for Multilingual ASR and AST](https://arxiv.org/abs/2509.14128)

### Nemotron Speech (Streaming ASR)

- 2025-12 · [nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b) *(model card)*
- 2026-05 · [nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) *(model card)*

## OpenAI

### Whisper

- 2022-12 · [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356)

## Alibaba (Qwen)

### Qwen ASR

- 2026-01 · [Qwen3-ASR Technical Report](https://arxiv.org/abs/2601.21337)
- 2026-09 · [Qwen-Audio-3.0-ASR Technical Report](https://arxiv.org/abs/2609.07549)

## Mistral AI

### Voxtral

- 2025-07 · [Voxtral](https://arxiv.org/abs/2507.13264)
- 2026-02 · [Voxtral Realtime](https://arxiv.org/abs/2602.11298)

## Meta

### wav2vec, MMS, and Omnilingual ASR

- 2020-06 · [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477)
- 2023-05 · [Scaling Speech Technology to 1,000+ Languages](https://arxiv.org/abs/2305.13516) (MMS)
- 2025-11 · [Omnilingual ASR: Open-Source Multilingual Speech Recognition for 1600+ Languages](https://arxiv.org/abs/2511.09690)

### Seamless (Speech Translation)

- 2023-08 · [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](https://arxiv.org/abs/2308.11596)
- 2023-12 · [Seamless: Multilingual Expressive and Streaming Speech Translation](https://arxiv.org/abs/2312.05187)

## Microsoft

### VibeVoice-ASR

- 2026-01 · [VIBEVOICE-ASR Technical Report](https://arxiv.org/abs/2601.18184)
- 2026-09 · [VibeVoice-ASR-Streaming Technical Report](https://arxiv.org/abs/2609.02812)

## Kyutai

### Kyutai STT

- 2025-09 · [Streaming Sequence-to-Sequence Learning with Delayed Streams Modeling](https://arxiv.org/abs/2509.08753)

## Other Open Labs

### FireRedASR (Xiaohongshu)

- 2025-01 · [FireRedASR: Open-Source Industrial-Grade Mandarin Speech Recognition Models from Encoder-Decoder to LLM Integration](https://arxiv.org/abs/2501.14350)

### Moonshine (Useful Sensors)

- 2024-10 · [Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://arxiv.org/abs/2410.15608)

## Academic

### OWSM (CMU)

- 2023-09 · [Reproducing Whisper-Style Training Using an Open-Source Toolkit and Publicly Available Data](https://arxiv.org/abs/2309.13876)

### Benchmarks

- 2025-10 · [Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation](https://arxiv.org/abs/2510.06961)

---

## Google

### Conformer and USM

- 2020-05 · [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
- 2023-03 · [Google USM: Scaling Automatic Speech Recognition Beyond 100 Languages](https://arxiv.org/abs/2303.01037)
