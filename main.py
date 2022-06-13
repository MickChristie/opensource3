from fastapi import FastAPI

app1 = FastAPI()

listofnum=[]


@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else."}


@app1.post("/numbers")
async def addNum(anewnum: str, count: int = 1):
    result = False
    message = "Not specified"
    if anewnum in num:
        nums[anewnum] = nums[anewnum] + count
        result = True
        message = f"Existing and added item(s): {anewnum}."
    else:
        result = True
        message = f"Successfully added: {anewnum}."
        nums[anewnum] = count

    return {"result": result, "message": message, "nums": nums}
  
@app1.get("numbers/sum")
async def sumNum():
  if len(listofnum) >= 1:
    print("The sum of all numbers entered so far is: " sum(listofnum))
  else:
    print("No values entered")
  return{"result:111"}
