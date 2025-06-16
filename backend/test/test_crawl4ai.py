# -*- encoding: utf-8 -*-
"""
@Time    :   2025-06-16 18:34:45
@desc    :
@Author  :   ticoAg
@Contact :   1627635056@qq.com
"""

import asyncio

from crawl4ai import AsyncWebCrawler


async def main():
    """主函数，用于异步运行网页爬虫.

    此函数会创建一个 AsyncWebCrawler 实例，并使用它来爬取指定 URL 的内容，最后打印爬取结果的 Markdown 格式内容。
    """
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business")
        print(result.markdown)


if __name__ == "__main__":
    asyncio.run(main())
