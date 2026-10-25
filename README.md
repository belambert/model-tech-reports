# Model Tech Reports

A curated list of technical reports, blog posts, and model cards for major
foundation models, focused on open-weight models and recent releases. It also
covers the earlier foundational reports from the closed frontier labs.

**[Browse all releases in a sortable, filterable table →](https://belambert.github.io/model-tech-reports/)**

Or jump straight to a category: [LLMs and VLMs](https://belambert.github.io/model-tech-reports/llm.html) · [VLAs](https://belambert.github.io/model-tech-reports/vla.html) · [World Models](https://belambert.github.io/model-tech-reports/world-model.html) ·
[Image and Video](https://belambert.github.io/model-tech-reports/image-video.html) · [Speech and Audio](https://belambert.github.io/model-tech-reports/speech.html)

## Scope

- **Included:** Generative language models (base, chat, reasoning, code,
  vision-language, omni), plus major VLA, world, image, video, and speech
  models.
- **Excluded:** Embedding, reranker, and classifier models; most
  fine-tunes; papers that only describe a technique rather than a released
  model (these can go under a release's `related` links).
- **Recency:** Recent generations are covered in depth. Older generations
  appear only where they started a model family or set a lasting direction.

## Data

The data lives in `data/`, one YAML file per company. Each file lists the
company's model families, and each family lists its releases:

```yaml
company: Zhipu AI / Z.ai
openness: open                # open | closed | unknown

families:
  - name: GLM LLMs
    category: llm             # llm | vla | world-model | image-video | speech
    # openness: closed        # optional; overrides the company default
    releases:
      - name: GLM-5.2
        date: 2026-06         # YYYY-MM
        # openness, category  # optional; override the family
        # note: ...           # optional free text
        weights:              # optional; model pages, usually Hugging Face
          - https://huggingface.co/zai-org/GLM-5.2
        writeups:             # required; the first one is the main link
          - kind: blog        # report | blog | model-card | docs
            title: GLM-5.2
            url: https://z.ai/blog/glm-5.2
        related:              # optional; third-party analyses, technique papers
          - title: GLM-5.2 IndexShare Architecture Note
            author: Sebastian Raschka
            url: https://sebastianraschka.com/blog/2026/glm-5-2-indexshare.html
```

Conventions:

- A release is one model (or one set of models released together). All of its
  official write-ups go in `writeups`, with the fullest one first.
- Dates use the arXiv v1 submission date when there is one. Otherwise they
  use the release date.
- Prefer arXiv abstract links, and use each write-up's exact title.
- `report` is a full technical report or paper, including system cards
  published as papers. Use `blog`, `model-card`, or `docs` for everything
  else.

## Building

`scripts/build_site.py` validates the data and builds `_site/index.html` (all
releases), one `_site/<category>.html` page per category, and
`_site/reports.json`. CI runs it on every push and pull request, fails on
invalid data, and deploys `main` to GitHub Pages. To build locally:

    pip install -r requirements.txt
    python3 scripts/build_site.py && open _site/index.html

## TODO

- [ ] Audit each company's data file for missing releases, dead or wrong
  links, and stale openness values.
- [ ] Add Reflection AI's Beam (501B-A23B, announced 2026-10-05) once the
  weights and a technical report or model card are published.
- [ ] Link the Mistral Large 4 weights once Mistral releases them (announced
  for the end of October 2026).
- [ ] Add GLM-5.1 (2026-04), which has weights on Hugging Face but no
  release entry.
- [ ] Check whether Kimi k1.5 and Nemotron-4 15B are really open; no public
  weights were found.
- [ ] Find weights, if any exist, for Qwen-VLA, Qwen-RobotManip, π0.7, and
  GLM-5V-Turbo, and add notes.
- [ ] Re-check Qwen3.5-Omni (marked closed) and Qwen-Audio-3.0-ASR (marked
  unknown) for a weights release.
- [ ] Link official weights for π0 and π0.5, which currently point to
  LeRobot ports.
- [ ] Read the license text for releases whose Hugging Face license is
  `other`; their notes just say "a custom license".
- [ ] Keep parameter counts and notes manual; do not automate fetching them
  from the Hugging Face API.
