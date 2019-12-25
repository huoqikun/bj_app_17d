import yaml

data = {"search1":{
        "search2": "enn"
       ,"search3": "lala"
}

}

with open("./a.yml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)

