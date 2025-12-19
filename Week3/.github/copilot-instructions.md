# Copilot Instructions for Week3 FastAPI Project

## Project Overview
This is a FastAPI-based REST API for managing heroes, using SQLModel for ORM and SQLite for persistence. The main file is `firstapi.py`.

## Architecture & Data Flow
- **Single-file API**: All logic is in `firstapi.py`.
- **Models**: Hero entities are defined using SQLModel classes (`HeroBase`, `Hero`, `HeroPublic`, `HeroCreate`, `HeroUpdate`).
- **Database**: SQLite (`database.db`) is used, with SQLModel handling migrations and schema creation.
- **Session Management**: Dependency injection via FastAPI's `Depends` and `Annotated` for DB sessions.
- **Endpoints**:
  - `POST /heroes/`: Create a hero
  - `GET /heroes/`: List heroes (supports `offset` and `limit`)
  - `GET /heroes/{hero_id}`: Get hero by ID
  - `PATCH /heroes/{hero_id}`: Update hero
  - `DELETE /heroes/{hero_id}`: Delete hero

## Developer Workflows
- **Run the API**: `python3 firstapi.py` (ensure `sqlmodel` and `fastapi` are installed)
- **Database Initialization**: Tables are auto-created on startup via `@app.on_event("startup")`.
- **Testing**: No test files present; add tests in separate files if needed.
- **Debugging**: Use FastAPI's built-in error messages and HTTP status codes.

## Project-Specific Patterns
- **Model Validation**: Use `Hero.model_validate(hero)` for input validation.
- **Partial Updates**: PATCH uses `model_dump(exclude_unset=True)` and `sqlmodel_update()` for partial updates.
- **Session Dependency**: All DB operations use `SessionDep` (an `Annotated` FastAPI dependency).
- **Response Models**: Endpoints return public-facing models (`HeroPublic`) to avoid exposing secrets.

## External Dependencies
- `fastapi` and `sqlmodel` (install via `pip`)
- SQLite (no setup required; file is created automatically)

## Example Usage
```bash
pip install fastapi sqlmodel
python3 firstapi.py
```

## Key File
- `firstapi.py`: All API logic, models, and DB setup

---
**If you add new endpoints, models, or workflows, update this file to document patterns and conventions.**
