import json
import pygal_maps_world.maps
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    # 函数json.load()将json文件转换为python可以处理的格式，这里是一个列表
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']

        # 这里插入float的原因是value存在小数，而int函数不能直接将含有小数的字符串转换为整数，所以
        # 应该先转换成float形式，再转变成int形式（换句话说，int可以转换带小数的float函数，但是不能
        # 转换带小数的字符串）
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
