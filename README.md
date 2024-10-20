
What we do here:
```
# Optionally, specify your own session_state key for storing messages
msgs = StreamlitChatMessageHistory(key="special_app_key")

...

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,  # Always return the instance created earlier
    input_messages_key="question",
    history_messages_key="history",
)

...

    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"question": prompt}, config)
```

is similar to what we've done in the [Neo4j's Course](https://graphacademy.neo4j.com/courses/llm-fundamentals/3-intro-to-langchain/3.7-persist-memory/):



```
memory = ChatMessageHistory()

def get_memory(session_id):
    return memory

chat_chain = prompt | chat_llm | StrOutputParser()

chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)

...

    response = chat_with_message_history.invoke(
        {
            "context": current_weather,
            "question": question,
            
        }, 
        config={
            "configurable": {"session_id": "none"}
        }
    )
```

