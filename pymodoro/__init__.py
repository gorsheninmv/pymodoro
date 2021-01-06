import sys
import tomatonotifier
import tomatorunner


def main() -> None:
    app = sys.argv[1] if len(sys.argv) > 1 else ''

    if app == 'runner':
        tomatorunner.main()
    elif app == 'notifier':
        tomatonotifier.main()
    else:
        inner_main()


def inner_main() -> None:
    print('pymodoro!')
