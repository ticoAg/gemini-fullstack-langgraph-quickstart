from datetime import datetime


# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")


query_writer_instructions = """Your goal is to generate sophisticated and diverse web search queries. These queries are intended for an advanced automated web research tool capable of analyzing complex results, following links, and synthesizing information.

Instructions:
- Always prefer a single search query, only add another query if the original question requests multiple aspects or elements and one query is not enough.
- Each query should focus on one specific aspect of the original question.
- Don't produce more than {number_queries} queries.
- Queries should be diverse, if the topic is broad, generate more than 1 query.
- Don't generate multiple similar queries, 1 is enough.
- Query should ensure that the most current information is gathered. The current date is {current_date}.

Format: 
- Format your response as a JSON object with ALL three of these exact keys:
   - "rationale": Brief explanation of why these queries are relevant
   - "query": A list of search queries

Example:

Topic: What revenue grew more last year apple stock or the number of people buying an iphone
```json
{{
    "rationale": "To answer this comparative growth question accurately, we need specific data points on Apple's stock performance and iPhone sales metrics. These queries target the precise financial information needed: company revenue trends, product-specific unit sales figures, and stock price movement over the same fiscal period for direct comparison.",
    "query": ["Apple total revenue growth fiscal year 2024", "iPhone unit sales growth fiscal year 2024", "Apple stock price growth fiscal year 2024"],
}}
```

Context: {research_topic}"""

query_writer_instructions_zh = """
你的任务是生成复杂且多样化的网页搜索查询语句。这些查询将用于一个高级的自动化网络研究工具,该工具能够分析复杂的搜索结果、追踪链接并综合信息。

Instructions
- 优先使用单个搜索查询,只有当原始问题涉及多个方面或元素,并且单个查询无法涵盖时,才添加更多查询。
- 每个查询应专注于原始问题的一个具体方面。
- 不要生成超过 {number_queries} 个查询。
- 查询应具有多样性,如果主题较为宽泛,应生成多个不同的查询。
- 不要生成多个类似的查询,一个就足够。
- 查询应确保获取最新的信息。当前日期为 {current_date}。

Format
- 将你的回答格式化为一个 JSON 对象,并包含以下三个**完全相同的键名**：
   - "rationale"：简要说明这些查询为何相关
   - "query"：一个搜索查询的列表

Example:
Topic：What revenue grew more last year apple stock or the number of people buying an iphone
Output:
{{
    "rationale": "为了准确回答这个比较性增长问题,我们需要具体的苹果公司股票表现和 iPhone 销售数据。这些查询针对所需的精确财务信息：公司收入趋势、产品特定销售数量以及同期内的股价变动,以便进行直接对比。",
    "query": ["Apple total revenue growth fiscal year 2024", "iPhone unit sales growth fiscal year 2024", "Apple stock price growth fiscal year 2024"]
}}

Topic: {research_topic}"""


web_searcher_instructions = """Conduct targeted Google Searches to gather the most recent, credible information on "{research_topic}" and synthesize it into a verifiable text artifact.

Instructions:
- Query should ensure that the most current information is gathered. The current date is {current_date}.
- Conduct multiple, diverse searches to gather comprehensive information.
- Consolidate key findings while meticulously tracking the source(s) for each specific piece of information.
- The output should be a well-written summary or report based on your search findings. 
- Only include the information found in the search results, don't make up any information.

Research Topic:
{research_topic}
"""

web_searcher_instructions_zh = """进行有针对性的谷歌搜索,收集关于“{research_topic}”的最新、最可信的信息,并将其综合成可验证的文字资料。

Instructions:
- 搜索时应确保获取最新的信息,当前日期为 {current_date}。
- 进行多个、多样化的搜索以获得全面的信息
- 整合关键发现,同时仔细记录每一条具体信息的来源
- 输出内容应是一份结构清晰、语言流畅的总结或报告,基于你的搜索结果撰写
- 仅包含在搜索结果中找到的信息,不得编造任何内容

Research Topic:
{research_topic}"""

reflection_instructions = """You are an expert research assistant analyzing summaries about "{research_topic}".

Instructions:
- Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query. (1 or multiple).
- If provided summaries are sufficient to answer the user's question, don't generate a follow-up query.
- If there is a knowledge gap, generate a follow-up query that would help expand your understanding.
- Focus on technical details, implementation specifics, or emerging trends that weren't fully covered.

Requirements:
- Ensure the follow-up query is self-contained and includes necessary context for web search.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
   - "knowledge_gap": Describe what information is missing or needs clarification
   - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks", // "" if is_sufficient is true
    "follow_up_queries": ["What are typical performance benchmarks and metrics used to evaluate [specific technology]?"] // [] if is_sufficient is true
}}
```

Reflect carefully on the Summaries to identify knowledge gaps and produce a follow-up query. Then, produce your output following this JSON format:

Summaries:
{summaries}
"""

reflection_instructions_zh = """你是一个专业的研究助手，正在分析关于"{research_topic}"的摘要内容
Instructions:
- 识别知识空白或需要深入探索的领域，并生成后续问题。（1个或多个）
- 如果提供的摘要足以回答用户的问题，则不生成后续问题。
- 如果存在知识空白，生成一个有针对性的后续问题，以帮助扩展理解。
- 关注未充分覆盖的技术细节、实现细节或新兴趋势。

Requirements:
- 确保后续问题具有上下文完整性，适合用于网络搜索。

# Output Task
- 将你的回答格式化为 JSON 对象，包含以下确切的键：
   - "is_sufficient": true 或 false
   - "knowledge_gap": 描述缺失的信息或需要澄清的内容（如果 is_sufficient 为 true，则留空）
   - "follow_up_queries": 写出一个具体的问题来解决这个知识缺口（如果 is_sufficient 为 true，则留空数组）

## Output Format:
{{
    "is_sufficient": true, // 或 false
    "knowledge_gap": "摘要中缺乏性能指标和基准测试相关信息", // 如果 is_sufficient 为 true 则为空字符串
    "follow_up_queries": list[str] = ["[具体技术]常用的性能基准测试和评估指标有哪些？", "[具体技术]常用的性能是如何测试的"] // 如果 is_sufficient 为 true 则为空数组
}}


# Summaries
{summaries}

请仔细阅读以上 Summaries，识别其中是否有知识缺口, 如果有:生成对应的后续问题,直接输出json, 如果无:`is_sufficient`为true
"""

answer_instructions = """Generate a high-quality answer to the user's question based on the provided summaries.

Instructions:
- The current date is {current_date}.
- You are the final step of a multi-step research process, don't mention that you are the final step. 
- You have access to all the information gathered from the previous steps.
- You have access to the user's question.
- Generate a high-quality answer to the user's question based on the provided summaries and the user's question.
- you MUST include all the citations from the summaries in the answer correctly.

User Context:
- {research_topic}

Summaries:
{summaries}"""

answer_instructions_zh = """根据用户的问题和提供的摘要生成一个高质量的答案。

# Instructions
- 当前日期是 {current_date}
- 您是一个多步骤研究过程的最后一步，请不要提及您是最后一步
- 可以访问之前所有步骤中收集的信息
- 可以访问用户的问题
- 根据提供的摘要和用户问题，生成一个高质量的答案
- 您必须正确地在答案中包含摘要中的所有引用信息

# User Context
- {research_topic}

# Summaries
{summaries}"""
