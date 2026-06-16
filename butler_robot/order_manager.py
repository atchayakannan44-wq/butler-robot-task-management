def optimize_route(tables):

    return sorted(tables)


if __name__ == "__main__":

    orders = [
        "table3",
        "table1",
        "table2"
    ]

    optimized = optimize_route(
        orders
    )

    print(
        "Optimized Route:",
        optimized
    )
