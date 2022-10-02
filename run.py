from os import environ as env
from app import App


def main():
    params = {
        "mongo_host": env.get("MONGO_HOST", "localhost"),
        "mongo_port": int(env.get("MONGO_PORT", 27017)),
        "mongo_db": env.get("MONGO_DB", "mayaprotect")
    }
    
    app = App(params)
    app.run()
    

if __name__ == "__main__":
    main()
    