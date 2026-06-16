from collections import deque
import time


class NavigationNode:

    def __init__(self):
        self.current_location = "home"

    def navigate(self, destination):

        print(
            f"\nMoving from {self.current_location} to {destination}"
        )

        time.sleep(2)

        self.current_location = destination

        print(f"Reached {destination}")


class MultiOrderRobot:

    def __init__(self):

        self.navigator = NavigationNode()

        self.completed_orders = []

        self.timeout_orders = []

        self.cancelled_orders = []

    def deliver_orders(self, orders):

        queue = deque(orders)

        print("\n======== STARTING DELIVERY ========")

        # Home -> Kitchen
        self.navigator.navigate("kitchen")

        while queue:

            table = queue.popleft()

            # Scenario 7 - Skip cancelled table
            if table in self.cancelled_orders:

                print(
                    f"\nSkipping {table} (Cancelled)"
                )

                continue

            self.navigator.navigate(table)

            # Scenario 6 - Timeout table
            if table in self.timeout_orders:

                print(
                    f"\nTimeout at {table}"
                )

                continue

            print(
                f"\nDelivered successfully to {table}"
            )

            self.completed_orders.append(table)

        print("\nAll deliveries processed")

        # Required by Scenario 6 and Scenario 7
        self.navigator.navigate("kitchen")

        self.navigator.navigate("home")

        self.show_summary()

    def show_summary(self):

        print("\n==============================")

        print(
            f"Completed : {self.completed_orders}"
        )

        print(
            f"Timeout   : {self.timeout_orders}"
        )

        print(
            f"Cancelled : {self.cancelled_orders}"
        )

        print("==============================")


if __name__ == "__main__":

    robot = MultiOrderRobot()

    orders = [
        "table1",
        "table2",
        "table3"
    ]

    # ======================================
    # SCENARIO 5
    # ======================================

    #robot.deliver_orders(orders)

    # ======================================
    # SCENARIO 6
    # ======================================
    # ======================================

    # robot.timeout_orders = ["table1"]
    # robot.deliver_orders(orders)

    # ======================================
    # SCENARIO 7
    # Uncomment below and comment Scenario 5
    # ======================================

    robot.cancelled_orders = ["table2"]
    robot.deliver_orders(orders)
