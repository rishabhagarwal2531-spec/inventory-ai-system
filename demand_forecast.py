def run_forecast(client):
    import pandas as pd
    from prophet import Prophet

    # load sales data
    sheet = client.open("inventory_data").worksheet("sales_log")
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    df.columns = df.columns.str.strip().str.lower()

    df = df.rename(columns={
        "date": "ds",
        "quantity_sold": "y"
    })

    df["ds"] = pd.to_datetime(df["ds"], errors='coerce')
    df["y"] = pd.to_numeric(df["y"], errors='coerce')

    df = df.dropna(subset=["ds", "y"])

    # load inventory
    inventory_sheet = client.open("inventory_data").worksheet("inventory")
    inventory_data = inventory_sheet.get_all_records()
    inventory_df = pd.DataFrame(inventory_data)

    inventory_df.columns = inventory_df.columns.str.strip().str.lower()

    results = []

    products = df["product_name"].unique()

    for product in products:
        product_df = df[df["product_name"] == product][["ds", "y"]]

        model = Prophet()
        model.fit(product_df)

        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)

        avg_demand = forecast["yhat"].tail(7).mean()

        stock = inventory_df[inventory_df["product_name"] == product]["current_stock"].values[0]

        days_left = stock / avg_demand if avg_demand > 0 else 0

        if days_left < 5:
            status = "URGENT REORDER"
        elif days_left < 10:
            status = "REORDER SOON"
        else:
            status = "OK"

        order_qty = int(avg_demand * 7)

        results.append({
            "product": product,
            "current_stock": stock,
            "avg_daily_demand": round(avg_demand, 2),
            "days_left": round(days_left, 2),
            "status": status,
            "recommended_order_qty": order_qty
        })

    return pd.DataFrame(results)