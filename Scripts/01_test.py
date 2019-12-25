import os,sys,pytest
sys.path.append(os.getcwd())
from Base.getData import GetData

import yaml


# def get_data():
#     sum = []
#
#     with open("./Data" + os.sep + "value.yml","r",encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#         for i in data.values():
#             sum.append(tuple(data.values(i)))
#     return sum


sum = []

    # with open("./Data" + os.sep + "value.yml","r",encoding="utf-8") as f:
    #     data = yaml.safe_load(f)
data = GetData.get_yml_data("value2.yml")
for i in data.values():
    sum.append(tuple(i.values()))


class TestWhat:
    @pytest.mark.parametrize("a,b,c",sum)
    def test_jj(self,a,b,c):
        assert a+b==c








