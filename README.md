# Natural Language to SQL Query Generator

Ask questions in plain English, get SQL answers instantly! 

I built this because I got tired of writing SQL queries all the time. Now I can just ask "how many products do we have?" and it figures out the SQL for me.

## What it does

- Type questions in normal English
- AI converts them to SQL and runs the query
- Get instant answers from a real database with 1000+ products
- Works with PostgreSQL + real Kaggle e-commerce data

## Tech Stack

Python • FastAPI • PostgreSQL • LangChain • OpenAI • Docker

## Architecture

```
User Question → FastAPI → LangChain Agent → OpenAI → SQL Query → PostgreSQL → Results
```

The system has 4 main layers:
- **User Layer**: Web interface and API endpoints
- **AI Layer**: LangChain agent that converts English to SQL  
- **Data Layer**: PostgreSQL with real Kaggle e-commerce data
- **Infrastructure**: Docker containers for easy deployment

## Quick Setup

You'll need Python 3.11+, Docker, and an OpenAI API key.

```bash
# Clone and setup
git clone https://github.com/yourusername/nl-to-sql-generator.git
cd nl-to-sql-generator

# Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install stuff
pip install -r requirements.txt

# Setup environment (add your OpenAI key)
copy .env.example .env

# Start database
docker-compose up -d postgres

# Test it works
python test_agent.py
```

## How to use it

```python
from app.agents.sql_agent import NaturalLanguageToSQLAgent

agent = NaturalLanguageToSQLAgent()

# Just ask questions like this:
result = agent.query("How many products do we have?")
print(result)  # "There are 1000 products."

result = agent.query("Which category has the most stuff?")
print(result)  # Gets the answer automatically
```

## Example questions you can ask

- "How many products are in each category?"
- "What's the average price?"
- "Which products have the best reviews?"
- "Show me sales by month"
- "Find expensive items over $500"

## Database

1,000 real products from Kaggle with categories, prices, reviews, and 12 months of sales data.

## Web API

Run `uvicorn app.main:app --reload` then check `/docs` for the API interface.

## Project Structure

```
├── app/
│   ├── agents/         # 🤖 LangChain SQL agents (the AI brain)
│   ├── core/           # ⚙️ Config, database connections
│   ├── api/            # 🌐 FastAPI routes and endpoints  
│   ├── models/         # 📋 Data schemas and types
│   └── utils/          # 🔧 Helper functions
├── data/
│   ├── processed/      # 📊 Clean Kaggle dataset (CSV files)
│   ├── sample_data/    # 🗃️ Database initialization scripts
│   └── migrations/     # 📈 Database schema changes
├── scripts/            # 🔄 Data processing workflows
│   ├── download_data.py    # ⬇️ Download Kaggle data
│   └── process_kaggle_data.py # 🧹 Clean and transform data
├── tests/              # ✅ Unit tests and integration tests
├── frontend/           # 🎨 Web interface (future enhancement)
└── docker-compose.yml  # 🐳 Container orchestration
```

### Why this structure?

**Separation of concerns**: AI logic, database, and web layers are separate
**Scalable**: Easy to add new agents, APIs, or data sources
**Professional**: Follows Python packaging standards
**Docker-ready**: Everything containerized for consistent deployment

## How It Works

### Data Processing Workflow
```bash
# 1. Download real e-commerce data from Kaggle
python scripts/download_data.py

# 2. Clean and process into database format  
python scripts/process_kaggle_data.py

# 3. Start database and auto-load data
docker-compose up -d postgres
```

### AI Query Workflow
```
1. User asks: "How many products do we have?"
2. LangChain agent analyzes the database schema
3. OpenAI generates SQL: SELECT COUNT(*) FROM products;
4. Query executes against PostgreSQL
5. Results returned as: "There are 1000 products."
```

### Development Workflow
```bash
# Quick development cycle
python test_agent.py           # Test everything works
uvicorn app.main:app --reload  # Start web server  
# Visit http://localhost:8000/docs for API interface

# Code quality
black app/        # Format code
pytest tests/     # Run tests
```

## Environment Variables

Just edit your `.env` file:
- `OPENAI_API_KEY` - Get this from OpenAI
- `OPENAI_MODEL` - Use gpt-3.5-turbo (cheaper) or gpt-4 
- `DATABASE_URL` - Postgres connection (already set for Docker)

## Troubleshooting

**Database connection issues**: Make sure Docker is running and ports aren't conflicting
**OpenAI API errors**: Check your API key and quota limits
**Import errors**: Make sure you're in the virtual environment (`venv\Scripts\activate`)
**Port 5432 in use**: The docker-compose.yml uses port 5433 to avoid conflicts

## Contributing

Feel free to fork and submit PRs. This was a fun project to build!

## Key Design Decisions

**Real Data First**: Started with actual Kaggle dataset instead of toy examples
**AI-Driven Architecture**: Built around LangChain agent as the core component  
**Environment-Based Config**: Different settings for dev/staging/production
**Docker-Native**: Everything containerized for consistency
**Modular Design**: Easy to swap out components (different AI models, databases, etc.)

## What I learned

- LangChain is pretty cool for connecting AI to databases
- FastAPI makes building APIs super easy  
- Docker is great for not having to install Postgres locally
- Real data makes everything more interesting than toy examples
- Building AI agents requires thinking about error handling and edge cases
- PostgreSQL's automatic schema introspection is really powerful

---

Built with Python, FastAPI, PostgreSQL, LangChain, and OpenAI