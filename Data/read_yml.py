import yaml

with open("./value2.yml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)

    print("data{}".format(data))

    print("类型:{}".format(type(data)))