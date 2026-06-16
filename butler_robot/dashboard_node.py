class Dashboard:

    def show(
        self,
        location,
        completed,
        timeout,
        cancelled
    ):

        print("\n================================")

        print(f"Current Location : {location}")

        print(f"Completed Orders : {completed}")

        print(f"Timeout Orders   : {timeout}")

        print(f"Cancelled Orders : {cancelled}")

        print("================================")


if __name__ == "__main__":

    dashboard = Dashboard()

    dashboard.show(
        location="home",
        completed=["table1", "table3"],
        timeout=["table2"],
        cancelled=[]
    )
