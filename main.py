"""
This is just a simple implemetation of MQTT.
"""


# Import the main application
from app import application


def main() -> None:
    """
    The main entry point for the application.

    This function serves as the entry point for the application, calling the `application()`
    function from the 'app' module.
    It can be used to start the application and perform any necessary setup or configuration.

    Returns:
        None: This function does not return any value.

    Example:
        To run the application, simply call `main()` from your script.

    """
    application()


if __name__ == "__main__":
    # Run the main function.
    main()
