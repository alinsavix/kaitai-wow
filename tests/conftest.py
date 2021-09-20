def pytest_addoption(parser):
    parser.addoption(
        "--diff-lines",
        action='store',
        default=200,
    )
