from webdriver_interface import WebdriverInterface


def main():
    wi = WebdriverInterface()
    wi.auth()
    wi.run_upload()
    wi.stop()


if __name__ == "__main__":
    main()
