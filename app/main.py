from fastapi import FastAPI

app = FastAPI(title="学生成绩管理系统", version="0.1.0")


@app.get("/")
def health_check():
    """健康检查端点，用于确认服务是否正常启动。"""
    return {"status": "ok"}

# This is from feature/demo-2 branch
from fastapi import FastAPI
