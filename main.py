from fastapi import FastAPI
app = FastAPI()


# uvicorn main:app --reload

@app.get('/')
async def root():
    return {"hello" : "team"}

@app.post("/goals")
async def postGoals():
    return {"hello" : "goals"}

@app.post("/meal")
async def postMeal():
    return {"hello" : "meal"}

@app.get('/daily_calories')
async def getDailyCalories():
    return {"hello" : "daily_calories"}

@app.get("/meal/day")
async def getAllMeals():
    return {"hello" : "meal days"}