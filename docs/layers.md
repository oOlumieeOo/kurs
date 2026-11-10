# Backend қабаттарының картасы (4-сабақ)

## Архитектуралық сызба

\\\mermaid
flowchart LR
    Client[Клиент / Браузер] --> Router[Router / routers]
    Router --> Schema[Schema / schemas]
    Router --> Service[Service / services]
    Service --> Repository[Repository / repositories]
    Repository --> Model[Model / models]
    Model --> DB[(PostgreSQL)]

    Core[Core: config, database] -.-> Router
    Core -.-> Service
    Core -.-> Repository
\\\

## Бір сұраныстың қабаттар бойынша саяхаты

| Қабат | 1-әрекет: Мұғалім тест құрады | 2-әрекет: Студент тест тапсырады |
| :--- | :--- | :--- |
| **Router** | POST /api/quizzes · рөл: teacher | POST /api/quizzes/{id}/attempts · рөл: student |
| **Schema** | QuizCreate -> QuizForTeacher | AttemptCreate -> AttemptRead |
| **Service** | Тест иесі мұғалім; тест жарияланбаған | Тест жарияланған; ұпай есептеу |
| **Repository** | QuizRepository.create | QuizRepository.add_attempt |
| **Model** | quizzes кестесі | attempts кестесі |
| **Қате -> HTTP** | атау 2 таңба -> 422; студент құрса -> 403 | тест жоқ -> 404; жауап саны қате -> 400 |

## Біздің келісім
- Router-де SQL жоқ, service-те HTTPException жоқ
- Құпиялар тек .env-те
