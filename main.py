from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/sample')
async def smth():
    return 'Nothing here'



