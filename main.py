from webdriver_interface import WebdriverInterface

import sys


def main():
    wi = WebdriverInterface()
    # wi.auth()

    try:
        wi.run_upload()
    except KeyboardInterrupt:
        wi.stop()
        sys.exit(130)


if __name__ == "__main__":
    main()
