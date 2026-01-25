---
name: tool-guide
description: Use this skill to determine which MCP tool or service to use for a specific task (search, documentation, browser automation).
user-invocable: false
---

# MCP Services Usage Guide

## 1. Documentation & Code Queries
*   **Context7**: Query latest library docs and code examples.
    *   *Use case*: Learning new frameworks (React Hooks, Vue Composition API).
    *   *Note*: Requires `resolve-library-id` first.
*   **DeepWiki**: Query GitHub repository documentation.
    *   *Use case*: Deep-diving into open source implementations, arch, contribution guides.

## 2. Information Search
*   **Exa**: **Primary** AI-powered web search.
    *   *Capabilities*: Real-time tech news, extract content from URLs.
*   **Tavily**: **Fallback** comprehensive search & data extraction.
    *   *Capabilities*: `search`, `extract`, `map` (site structure), `crawl`.

## 3. Browser Automation
*   **Playwright**: Browser control.
    *   *Use case*: Automate web operations, testing, form filling, screenshot analysis.
