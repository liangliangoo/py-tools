import multiprocessing

from api.router import app

if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    app.run()
