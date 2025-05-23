from fastapi import FastAPI


app = FastAPI()

@app.get("/users")
async def get_users():
    return {"user1": "Manish"}


@app.post("/postUserDataToTable")
def create_user(name: int):
    return {"Message": "User added successfully"}