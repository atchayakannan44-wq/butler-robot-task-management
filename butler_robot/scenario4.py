from enum import Enum
import time


class RobotState(Enum):

    IDLE = 0

    GO_TO_KITCHEN = 1

    WAIT_KITCHEN_CONFIRM = 2

    GO_TO_TABLE = 3

    WAIT_TABLE_CONFIRM = 4

    RETURN_KITCHEN = 5

    RETURN_HOME = 6

    COMPLETED = 7

    CANCELLED = 8


class NavigationNode:

    def __init__(self):
        self.current_location = "home"

    def navigate(self, destination):

        print(f"\nMoving from {self.current_location} to {destination}")

        time.sleep(2)

        self.current_location = destination

        print(f"Reached {destination}")


class TaskManager:

    def __init__(self):

        self.state = RobotState.IDLE

        self.navigator = NavigationNode()

        self.cancel_requested = False

    def set_state(self, state):

        self.state = state

        print(f"\nSTATE --> {state.name}")

    def wait_for_confirmation(self, location):

        print(f"\nWaiting confirmation at {location}")

        response = input("Confirm? (y/n): ")

        return response.lower() == "y"

    def cancel_order(self):

        self.cancel_requested = True

        print("\nORDER CANCELLED")

    # Scenario 1,2,3
    def deliver_order(self, table):

        self.set_state(
            RobotState.GO_TO_KITCHEN
        )

        self.navigator.navigate("kitchen")

        self.set_state(
            RobotState.WAIT_KITCHEN_CONFIRM
        )

        kitchen_confirm = self.wait_for_confirmation(
            "kitchen"
        )

        # Scenario 2 & 3A
        if not kitchen_confirm:

            print("\nKitchen timeout")

            self.set_state(
                RobotState.RETURN_HOME
            )

            self.navigator.navigate("home")

            return

        self.set_state(
            RobotState.GO_TO_TABLE
        )

        self.navigator.navigate(table)

        self.set_state(
            RobotState.WAIT_TABLE_CONFIRM
        )

        table_confirm = self.wait_for_confirmation(
            table
        )

        # Scenario 3B
        if not table_confirm:

            print("\nTable timeout")

            self.set_state(
                RobotState.RETURN_KITCHEN
            )

            self.navigator.navigate("kitchen")

            self.set_state(
                RobotState.RETURN_HOME
            )

            self.navigator.navigate("home")

            return

        # Scenario 1
        self.set_state(
            RobotState.RETURN_HOME
        )

        self.navigator.navigate("home")

        self.set_state(
            RobotState.COMPLETED
        )

        print("\nDelivery Completed Successfully")

    # Scenario 4A
    def deliver_order_cancel_kitchen(self):

        self.set_state(
            RobotState.GO_TO_KITCHEN
        )

        self.cancel_order()

        if self.cancel_requested:

            self.set_state(
                RobotState.CANCELLED
            )

            self.set_state(
                RobotState.RETURN_HOME
            )

            self.navigator.navigate("home")

            return


if __name__ == "__main__":

    robot = TaskManager()

    # Uncomment ONE at a time

    # Scenario 1 / 2 / 3
    # robot.deliver_order("table1")

    # Scenario 4A
    robot.deliver_order_cancel_kitchen()
