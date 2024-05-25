from webdriver_interface import WebdriverInterface

import sys


def main():
    wi = WebdriverInterface()
    wi.auth()
    wi.run_upload()


if __name__ == "__main__":
    main()
