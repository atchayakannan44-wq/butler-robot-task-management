import time


class NavigationNode:

    def __init__(self):
        self.current_location = "home"

    def navigate(self, destination):

        print(f"\nMoving from {self.current_location} to {destination}")

        time.sleep(2)

        self.current_location = destination

        print(f"Reached {destination}")


if __name__ == "__main__":

    robot = NavigationNode()

    robot.navigate("kitchen")

    robot.navigate("table1")

    robot.navigate("home")
