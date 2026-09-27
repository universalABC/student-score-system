# 学生成绩管理系统

一个简单的学生成绩管理后端系统，用于学习 AI 辅助软件开发流程。

## 技术栈

- Python 3.12
- FastAPI
- Pydantic v2
- SQLAlchemy 2.x
- MySQL 8
- Alembic
- OAuth2 Password Flow + JWT
- pytest

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv .venv
.venv\Scripts\activate

# 2. 安装依赖
pip install -e ".[dev]"

# 3. 复制环境变量文件并修改
cp .env.example .env

# 4. 运行测试
pytest

# 5. 启动服务
uvicorn app.main:app --reload
```

## Demo Branch 1
This is from feature/demo-1 branch.
