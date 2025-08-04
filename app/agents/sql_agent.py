"""LangChain SQL Agent for Natural Language to SQL conversion."""

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

from app.core.config import settings
from app.core.database import get_database_connection

class NaturalLanguageToSQLAgent:
    """Agent that converts natural language questions to SQL queries."""
    
    def __init__(self):
        """Initialize the SQL agent with OpenAI and database connection."""
        
        # Initialize OpenAI LLM
        self.llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model=settings.OPENAI_MODEL,
            temperature=0  # Low temperature for consistent SQL generation
        )
        
        # Create database connection for LangChain
        engine = get_database_connection()
        self.db = SQLDatabase(engine)
        
        # Create SQL toolkit with tools for the agent
        toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
        
        # Create the SQL agent
        self.agent = create_sql_agent(
            llm=self.llm,
            toolkit=toolkit,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,  # Shows reasoning steps
            handle_parsing_errors=True  # Handle parsing errors gracefully
        )
    
    def query(self, question: str) -> str:
        """
        Convert natural language question to SQL and execute it.
        
        Args:
            question: Natural language question about the data
            
        Returns:
            Answer based on SQL query execution
        """
        try:
            result = self.agent.invoke({"input": question})
            # Extract the output from the result
            if isinstance(result, dict) and "output" in result:
                return result["output"]
            else:
                return str(result)
        except Exception as e:
            return f"Error processing question: {str(e)}"
    
    def get_table_info(self) -> str:
        """Get information about available tables and columns."""
        return self.db.get_table_info()