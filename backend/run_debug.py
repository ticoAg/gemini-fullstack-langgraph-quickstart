from agent import graph

state = graph.invoke(
    {
        "messages": [{"role": "user", "content": "女频短篇小说读者的用户画像"}],
        "max_research_loops": 3,
        "initial_search_query_count": 3,
    }
)
