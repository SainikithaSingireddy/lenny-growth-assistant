# Design Specification

# UI Philosophy

The interface is designed for speed, clarity, and minimal cognitive load.

## Layout

Two-column responsive layout.

Left:
- Session history
- Chat messages
- Input box
- Model selector

Right:
- Artifact Viewer
- Markdown preview
- HTML preview

## Interaction States

- Empty chat
- Loading response
- Streaming tokens
- Error state
- Artifact generated

## Accessibility

- Keyboard accessible
- High contrast colors
- Responsive on laptop screens

## Design Decisions

- Chat-first interface
- Source citations always visible
- Artifact rendered beside conversation
- Provider badge shows Ollama or OpenAI