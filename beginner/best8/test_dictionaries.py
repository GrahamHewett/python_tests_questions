#like js objects key value pairs

# class TestUM(unittest.TestCase):
#     def test_smallest_num(self):
# 	self.assertEqual(smallest_num(0o765, 0x11),
# 	"The smallest number is 17")
# 	self.assertEqual(smallest_num(0b110, 55),
# 	"The smallest number is 6")

def s_dic(my_dict):
	sorted_dict = my_dict.sort(key=lambda item: item.get("Name"))
	return sorted_dict
print(s_dic({"a": 1, "c": 2, "d": 4, "b": 3}))

car: -{
        age: 22,
        brand: "Subaru",
        color: "blue",
        gold rims: true,
        model: "Impreza",
        year: 2010
    },
    key: "gold rims",
    value: true