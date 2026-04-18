# AI Lead Conversion Agent

Production-grade AI agent that captures, qualifies, and converts leads using multi-step planning and tool execution.

## Features
- Lead qualification (budget, intent, urgency)
- Context-aware responses
- Automated follow-ups
- Lead scoring (hot/warm/cold)
- API-first architecture

## Architecture
- Planner → decides next action
- Executor → runs tools
- Tools → extraction, reply, follow-up
- Memory → conversation tracking

## Tech Stack
- FastAPI
- Python
- LLM APIs (OpenAI / Gemini)
- SQLite (initial)
- Docker (deployment)

## Status
- In Development