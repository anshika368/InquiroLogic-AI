import streamlit as st
from pathlib import Path
from langchain_classic.agents import AgentType
from langchain_community.utilities import SQLDatabase
import sqlite3
from langchain_community.agent_toolkits.sql.base import create_sql_agent

from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine    #used to map output from sql database
from langchain_groq import ChatGroq

st.set_page_config(page_title="InquiroLogic-AI | Smart SQL Assistant", page_icon="🤖")
st.title("🧠 InquiroLogic-AI")
st.markdown("*Intelligent SQL Assistant powered by Groq & LangChain*")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"
radio_opt=["Use sqlite3 databse","Use MySQL database"]

selected_opt=st.sidebar.radio(label="Select the database option",options=radio_opt)
if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input(label="Enter MySQL host",value="localhost")
    mysql_user=st.sidebar.text_input(label="Enter MySQL user",value="root")
    mysql_password=st.sidebar.text_input(label="Enter MySQL password",value="password",type="password")
    mysql_db=st.sidebar.text_input(label="Enter MySQL database name",value="testdb")

else:
    db_uri=LOCALDB

api_key=st.sidebar.text_input(label="Enter Groq API Key",type="password")

if not db_uri:
    st.info("Please select a database option from the sidebar.")
## LLM model initialization
if not api_key:
    st.info("Please enter your Groq API key to proceed.")
    st.stop()  # <--- THIS IS CRITICAL. It stops the script here until you type the key.

llm = ChatGroq(
    groq_api_key=api_key, 
    model_name="llama-3.1-8b-instant", 
    streaming=True
) 
@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        #connect to sqlite database
        dbfilepath=(Path(__file__).parent / "student.db").absolute()
        print(dbfilepath)
        creator=lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite://", creator=creator))
    elif db_uri==MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")) 
if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)

#toolkit (to interact with sql db)
toolkit=SQLDatabaseToolkit(db=db, llm=llm)
agent=create_sql_agent(llm=llm, toolkit=toolkit, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,handle_parsing_errors=True, max_iterations=30)
if "messages" not in st.session_state or st.sidebar.button("Clear Conversation"):
    st.session_state["messages"] =[{"role":"assistant","content":"How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
user_query=st.chat_input("Ask a question about the database")
if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)
    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)