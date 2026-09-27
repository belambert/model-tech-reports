# Model Tech Reports

A curated list of technical reports for major foundation models, focused on
open-weight models and recent releases. It also covers the earlier
foundational reports from the closed frontier labs.

## Pages

| Page                                                  | Covers                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------ |
| [LLMs and VLMs](llms.md)                              | Language, reasoning, code, vision-language, and omni models              |
| [VLAs and World Models](vla-and-world-models.md)      | Vision-language-action (robotics) models and world models                |
| [Image and Video Generation](image-and-video.md)      | Text-to-image, image editing, and video generation models                |
| [Speech and Audio](speech-and-audio.md)               | Speech recognition (ASR) and speech translation models                   |

## Scope

- **Included:** Generative language models (base, chat, reasoning, code,
  vision-language, omni), plus major VLA, world, image, video, and speech
  models.
- **Excluded:** Embedding, reranker, and classifier models; most
  fine-tunes; papers that only describe a technique rather than a released
  model.
- **Recency:** Recent generations are covered in depth. Older generations
  appear only where they started a model family or set a lasting direction.

## Conventions

- Each page is organized by **company → model family → date** (oldest
  first). Open-weight labs come first, then closed labs.
- Dates are `YYYY-MM` and use the arXiv v1 submission date when there is one.
  Otherwise they use the release date.
- Links go to the arXiv abstract page where one exists. Otherwise they go to
  the official PDF, model card, or blog post. Entries marked *(blog)* or
  *(model card)* aren't full technical reports.

## Contributing

To add a report, put it on the right page under its company and model
family, in date order, using this format:

    - YYYY-MM · [Exact Paper Title](https://arxiv.org/abs/XXXX.XXXXX)

Prefer arXiv abstract links. Use the paper's exact title, and mark entries
that aren't full technical reports with *(blog)* or *(model card)*.
