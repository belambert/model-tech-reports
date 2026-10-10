# Model Tech Reports

A curated list of technical reports, blog posts, and model cards for major
foundation models, focused on open-weight models and recent releases. It also
covers the earlier foundational reports from the closed frontier labs.

**[Browse all releases in a sortable, filterable table →](https://belambert.github.io/model-tech-reports/)**

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

`scripts/build_site.py` validates the data and builds `_site/index.html` and
`_site/reports.json`. CI runs it on every push and pull request, fails on
invalid data, and deploys `main` to GitHub Pages. To build locally:

    pip install -r requirements.txt
    python3 scripts/build_site.py && open _site/index.html
