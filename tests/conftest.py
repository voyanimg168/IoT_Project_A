# # tests/conftest.py
# import threading
# import pytest
# from src.api_server import app  # adjust import to match your app

# @pytest.fixture(scope="session", autouse=True)
# def start_server():
#     t = threading.Thread(target=lambda: app.run(port=5000))
#     t.daemon = True
#     t.start()