import json

def main ():
    
    config_data = {}

    with open('config.json') as configFile:
        config_data = json.loads(configFile.read())

    print(config_data)



if __name__ == "__main__":
    main()