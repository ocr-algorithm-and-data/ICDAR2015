import re
import os

test_image_dir = "TestSet"
test_txt = "Challenge4_Test_Task3_GT.txt"
test_tags = "test.tags"

train_image_txt = "TrainingSet"
train_tags = "TrainingSet/train.tags"


def create_tags(txt_file, tags_file):
    with open(txt_file, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        re_match_obj = re.match(r'(.*png), "(.*)"\n', line)
        image_path = os.path.join(test_dir, re_match_obj.group(1))
        gt = re_match_obj.group(2)
        new_lines.append("{} {}\n".format(image_path, gt))
    with open(tags_file, "w") as f:
        f.write("".join(new_lines))

        
create_tags(test_txt, test_tags)
