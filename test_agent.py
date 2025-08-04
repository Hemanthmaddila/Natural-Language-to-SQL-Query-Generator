"""Test the Natural Language to SQL Agent."""

from app.core.database import test_connection
from app.agents.sql_agent import NaturalLanguageToSQLAgent

def main():
    print("🔧 Testing database connection...")
    print(test_connection())
    
    print("\n🤖 Initializing AI Agent...")
    agent = NaturalLanguageToSQLAgent()
    
    print("\n📊 Database Schema:")
    print(agent.get_table_info())
    
    print("\n🧠 Testing Natural Language Query...")
    question = "How many products are there in total?"
    print(f"Question: {question}")
    answer = agent.query(question)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()