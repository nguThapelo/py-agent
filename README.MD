# Homework Tutor

A chat tutor for South African school learners (Grades 4 to 12). It teaches through hints and questions and never gives the answer to the learner's own problem.

## Run it

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-key
```

Then:

```
python manage.py runserver
```

Open http://localhost:8000.

Optional settings: `TUTOR_MODEL` and `GUARD_MODEL` (both default to `gpt-4o-mini`), `DJANGO_DEBUG`, `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`. When `DJANGO_DEBUG=0` a secret key is required.

## How "never give the answer" is enforced

1. The tutor prompt ([agents/tutor.py](agents/tutor.py)) tells the model to give one hint or question at a time. It may explain a rule, or solve a different example with other numbers.
2. A second model call reviews every draft reply and blocks it if it reveals the answer to the learner's problem. A blocked draft is rewritten once.
3. If the rewrite is also blocked, or the reviewer fails or returns something unreadable, the learner gets a fixed message asking what they have tried. The draft is never shown.

This is strong but not a mathematical guarantee. Both layers are language models, and a reviewer can occasionally miss a leak. Test it with real learner questions before putting it in front of children, and read the failures.

## Privacy

Nothing is stored. The browser keeps the conversation in memory and sends the last 10 messages with each request. The server does not save or log chat content, and there are no accounts.

## Tests

```
python -m pytest tests
```

These use fake models, so they check the guard logic and need no API key. They do not measure how good the real models are at spotting leaks.
