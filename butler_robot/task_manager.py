from enum import Enum
import time


class RobotState(Enum):

    IDLE = 0

    GO_TO_KITCHEN = 1

    WAIT_KITCHEN_CONFIRM = 2

    GO_TO_TABLE = 3

    WAIT_TABLE_CONFIRM = 4

    RETURN_HOME = 5

    COMPLETED = 6


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

    def set_state(self, state):

        self.state = state

        print(f"\nSTATE --> {state.name}")

    def wait_for_confirmation(self, location):

        print(f"\nWaiting confirmation at {location}")

        response = input(
            "Confirm? (y/n): "
        )

        if response.lower() == "y":
            return True

        return False

    def deliver_order(self, table):

        self.set_state(RobotState.GO_TO_KITCHEN)

        self.navigator.navigate("kitchen")

        self.set_state(
            RobotState.WAIT_KITCHEN_CONFIRM
        )

        kitchen_confirm = self.wait_for_confirmation(
            "kitchen"
        )

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

        if not table_confirm:

            print("\nTable timeout")

            self.set_state(
                RobotState.RETURN_HOME
            )

            self.navigator.navigate("home")

            return

        self.set_state(
            RobotState.RETURN_HOME
        )

        self.navigator.navigate("home")

        self.set_state(
            RobotState.COMPLETED
        )


if __name__ == "__main__":

    robot = TaskManager()

    robot.deliver_order("table1")
