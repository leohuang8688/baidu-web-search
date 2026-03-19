# 🔍 Baidu Web Search Skill

**百度网页搜索技能 - 使用百度搜索 API 进行网络搜索**

---

## 📋 Overview

| Property | Value |
|----------|-------|
| **Name** | baidu-web-search |
| **Version** | 1.0.0 |
| **Author** | PocketAI for Leo |
| **License** | MIT |
| **Category** | Search |
| **Required Env Vars** | `BAIDU_API_KEY` (or `TAVILY_API_KEY`) |

---

## 🔐 Required Environment Variables

**This skill requires the following environment variables:**

| Variable | Description | Required | How to Get |
|----------|-------------|----------|------------|
| `BAIDU_API_KEY` | Baidu Search API key | ✅ Yes (if using Baidu) | https://ai.baidu.com/ |
| `TAVILY_API_KEY` | Tavily Search API key | ✅ Yes (if using Tavily) | https://app.tavily.com |
| `SEARCH_PROVIDER` | Search provider selection (`baidu` or `tavily`) | ❌ No | See provider selection below |

**Provider Selection Logic:**
- If `SEARCH_PROVIDER` is set to `tavily` or `baidu`, that provider is used.
- If `SEARCH_PROVIDER` is not set, Tavily is used when `TAVILY_API_KEY` is present, otherwise Baidu.

**Configuration:**
```bash
# Baidu (default when no Tavily key is present)
export BAIDU_API_KEY="your_baidu_api_key"

# Tavily (optional, used when key is present or SEARCH_PROVIDER=tavily)
export TAVILY_API_KEY="your_tavily_api_key"
export SEARCH_PROVIDER="tavily"  # optional, auto-detected from API key
```

---

## ✨ Features

- 🔍 **Baidu Web Search** - 使用百度搜索 API 进行网络搜索
- 🇨🇳 **Chinese Focus** - 专注于中文搜索结果
- 📊 **Customizable Results** - 可定制返回结果数量
- 🚀 **Easy Integration** - 易于集成到 OpenClaw

---

## ✨ Features

- 🔍 **Baidu Web Search** - 使用百度搜索 API 进行网络搜索
- 🇨🇳 **Chinese Focus** - 专注于中文搜索结果
- 📊 **Customizable Results** - 可定制返回结果数量
- 🚀 **Easy Integration** - 易于集成到 OpenClaw

---

## 🚀 Quick Start

### Installation

```bash
cd ~/.openclaw/workspace/skills
# Already installed at: baidu-web-search/
```

### Configuration

**Option 1: Using .env file (Recommended)**

```bash
# Copy the example .env file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use your favorite editor
```

**Option 2: Using environment variable**

```bash
export BAIDU_API_KEY="your_baidu_api_key"
```

### Basic Usage

```python
from src.baidu_search import baidu_search

# Search with default 10 results
result = baidu_search("人工智能 2026")
print(result)

# Search with custom result count
result = baidu_search("新能源汽车", count=5)
print(result)
```

### CLI Usage

```bash
# Search with default 10 results
python3 src/baidu_search.py "人工智能 2026"

# Search with custom result count
python3 src/baidu_search.py "新能源汽车" 5
```

---

## 📖 API Usage

### Python API

```python
from src.baidu_search import BaiduSearch, baidu_search

# Method 1: Simple search
result = baidu_search("OpenClaw AI", count=10)
print(result)

# Method 2: Using client
searcher = BaiduSearch(api_key="your_api_key")
results = searcher.search("OpenClaw", count=5)

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['abstract']}\n")
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BAIDU_API_KEY` | Baidu Search API key | ✅ Yes (if using Baidu) |
| `TAVILY_API_KEY` | Tavily Search API key | ✅ Yes (if using Tavily) |
| `SEARCH_PROVIDER` | Provider selection (`baidu` or `tavily`) | ❌ No |

### Getting Baidu API Key

1. Visit [Baidu AI Open Platform](https://ai.baidu.com/)
2. Create an account or login
3. Go to Console → Applications
4. Create a new application
5. Get your API Key

---

## 📁 Project Structure

```
baidu-web-search/
├── src/
│   └── baidu_search.py     # Main search client
├── SKILL.md                 # This file
└── README.md                # Documentation
```

---

## 🎯 Use Cases

### 1. News Search

```python
result = baidu_search("最新科技新闻 2026")
```

### 2. Research

```python
result = baidu_search("人工智能 医疗 应用")
```

### 3. Product Search

```python
result = baidu_search("智能手机 评测")
```

### 4. Local Search

```python
result = baidu_search("北京 美食 推荐")
```

---

## 📝 Response Format

### Search Result Structure

```json
{
  "title": "网页标题",
  "url": "网页链接",
  "abstract": "摘要内容"
}
```

### Example Output

```
🔍 Baidu Search Results for: 人工智能 2026

Found 10 results:

1. **2026 年人工智能发展趋势**
   URL: https://example.com/ai-trends-2026
   2026 年人工智能领域将呈现以下发展趋势...

2. **人工智能应用场景**
   URL: https://example.com/ai-applications
   人工智能在医疗、金融等领域的应用...
```

---

## ⚠️ Limitations

- **API Rate Limits:** Baidu and Tavily APIs have rate limits
- **API Key Required:** Must have a valid API key for the selected provider
- **Chinese Focus:** Baidu is best for Chinese language queries; Tavily provides broader multilingual coverage
- **Regional Restrictions:** Baidu may have regional restrictions

---

## 📞 Support

- **Baidu AI Docs:** https://ai.baidu.com/docs
- **API Reference:** https://ai.baidu.com/ai-doc/SEARCH

---

## 📄 License

MIT License - See LICENSE file for details.

---

**Happy Searching! 🔍**

---

*Last Updated: 2026-03-17*  
*Version: 1.0.0*  
*Author: PocketAI for Leo*
