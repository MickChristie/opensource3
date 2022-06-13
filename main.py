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
    print("The sum of all numbers entered so far is: ", sum(listofnum))
  else:
    print("No values entered")
  return{"result:111"}

@app1.get("numbers/average")
async def averageNum():
  if len(listofnum) >= 1:
    print("The average of all numbers entered so far is: ", sum(listofnum)/len(listofnum))
  else:
    print("No values entered")
  return{"result:111"}

@app1.get("numbers/stddev")
async def stddevNum():
  if len(listofnum) >= 1:
    n = len(listofnum)
    mean= sum(listofnum)/len(listofnum)
    var = sum((x - mean)**2 for x in ls) / n
    standev = var ** 0.5
    print("The standard deviation of all numbers entered so far is: ",(standev) )
  else:
    print("No values entered")
  return{"result:111"}

