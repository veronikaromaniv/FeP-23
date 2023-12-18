from fastapi import FastAPI, HTTPException
from Customer import Customer, OrderFacade

app = FastAPI()
order_facade = OrderFacade()


@app.post("/process_order/{order_data_path}")
def process_order(order_data_path: str):
    customer = Customer("1")

    order_facade = OrderFacade()
    order_facade.register_customer(customer)

    try:
        order_facade.process_order(order_data_path)
        return {"message": "Order processing complete"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
