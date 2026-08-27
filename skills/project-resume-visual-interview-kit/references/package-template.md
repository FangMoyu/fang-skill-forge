# Package template

Use this reference when the user requests a complete saved package rather than only one paragraph or one answer. Adjust names and count to the project; the following is a recommended shape, not a mandatory claim about every project.

## Directory

Create a new, clearly named output directory. Keep generated artifacts separate from the source repository unless the user asks for repository changes.

```text
project-study-kit/
├── 00-start-here.md
├── 01-project-introduction.md
├── 02-business-diagram-guide.md
├── 03-resume-interview-handbook.md
├── 04-resume-claim-explanation.md
├── 05-verification-and-known-gaps.md
├── 06-practice-record.md
├── diagrams/
│   ├── index.html
│   ├── 01-<business-flow>.excalidraw
│   ├── 01-<business-flow>.svg
│   └── 01-<business-flow>.png
├── images/
│   └── <diagram-previews>.png
└── package-manifest.json
```

Use fewer files for a small request. Do not create empty files just to match this tree.

## Start-here document

State the primary project, any comparison project, target role, time budget, reading order, output location, and truthfulness boundary. Tell the reader which artifacts are source observations, which are personal work, and which remain proposed or unverified.

## Project introduction

Use this order:

1. one-sentence business purpose;
2. target user and the decision/problem being solved;
3. one concrete end-to-end user example;
4. primary project versus comparison-project capabilities;
5. main flow in business language;
6. data responsibilities and external dependencies;
7. failure and safety boundaries;
8. technology list with each technology's actual role;
9. 30-second, 90-second, and three-minute speaking outlines;
10. bounded resume draft.

If the project is a study, extension, or collaborative change, preserve that relationship framing. Do not convert a source observation into “I independently built” without a personal artifact.

## Business diagram guide

For each diagram explain:

- what user action or operational event starts it;
- what each business box means in plain language;
- what every branch label means;
- what data or decision moves across each arrow;
- why the sequence protects a user or system invariant;
- what the current source actually establishes;
- which steps are a proposed future path.

Use flowcharts for sequence/decisions and use-case or relationship diagrams for actor-to-capability views. Avoid putting package names, class names, method names, database table names, or framework jargon in business nodes. Keep technical source links in the accompanying Markdown, not in the diagram labels.

## Offline reader and manifest

An offline HTML reader is useful when the package contains multiple Markdown files and diagrams. It should use relative links inside the package, support switching documents, and make images open at readable size. Do not require a server or API key to read study materials.

The manifest should record file paths, sizes, hashes, and the checks that were actually run. It must state that artifact validation does not prove application runtime behavior.

## Delivery verification

Before copying to Desktop or another external location:

- confirm the destination is a new directory and will not overwrite an existing directory;
- validate all expected Markdown files, images, diagrams, and the offline reader;
- validate Excalidraw JSON type/version, unique IDs, arrow bindings, text font settings, and image rendering;
- validate local links and source line anchors where present;
- validate interview question numbering and answer sections;
- compare source and copied file hashes after copying.

Do not put real API keys, database passwords, or unredacted user conversations into diagrams, logs, manifests, or study documents.

