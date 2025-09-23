import sys;
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(x,y): 
    return (int(x)+int(y))

@app.get("/sub")
def sub(x,y):
    return (int(x)-int(y))

# x = int(input("give the value of x : "))
# y = int(input("give the value of y : "))

if __name__ == "__main__":
    # x = sys.argv[1]
    # y = sys.argv[2]
    # print(add(x,y))
    uvicorn.run(app,host="0.0.0.0",port=3000)
