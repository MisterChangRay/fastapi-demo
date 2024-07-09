from fastapi import Depends, FastAPI
import uvicorn
import pymysql
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler
from .dependencies import  get_token_header
from .controller import consoleController
from .controller import userController
from .scheduleService import test
from .orm.schemas import SessionLocal
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    version="v0.0.1"
    # dependencies=[Depends(get_token_header)]
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/version")
async def version():
    """获取当前服务版本

    Returns:
        _type_: _description_
    """
    logger.info("当前版本为: {}", app.version)
    return {"version": app.version}


app.include_router( consoleController.router)
app.include_router(
    userController.router,
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


logger.add("./logs/mylog.log", rotation="50 MB")



@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    # 增加计划任务, 每50s执行一次
    # scheduler.add_job(test, 'cron', second='*/50')
    # 每2分钟执行一次
    scheduler.add_job(test, 'cron', minute="*/2")
    
    scheduler.start()
    
# 入口函数
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(8078))