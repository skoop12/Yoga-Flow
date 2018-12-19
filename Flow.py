import random

class Pose:
    def __init__(self, name, transition_to=[]):
        self.name = name
        self.transition_to = transition_to

    def add(self, pose):
        self.transition_to.append(pose)

    def get_options(self):
        return self.transition_to

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

# Poses

chaturanga = Pose('Chaturanga')
down_dog = Pose('Down Dog')
chaturanga.add(down_dog)
half_way_lift = Pose('Half Way Lift', [chaturanga])
forward_fold = Pose('Forward Fold', [half_way_lift])
down_dog.add(forward_fold)
mountain = Pose('Mountain', [chaturanga])
triangle = Pose('Triangle')
warrior_two = Pose('Warrior II', [triangle])
triangle.add(warrior_two)
table_top = Pose('Table Top', [down_dog])
child = Pose('Childs Pose', [table_top, down_dog])
puppy = Pose('Puppy Pose', [table_top, down_dog])
cat_cow = Pose('Cat Cows', [puppy, table_top, down_dog])
table_top.add(cat_cow)
table_top.add(puppy)

start_poses = [child]
warm_up_poses = [down_dog, table_top, puppy, cat_cow]
hip_poses = []
arm_poses= []
tad_variation = []
chair_variation = []

class WarmUp:
    def __init__(self):
        self.start_pose = random.choice(start_poses)
        self.poses = [self.start_pose]

    def add_poses(self):
        num_poses = random.randint(1,5)
        current_pose = self.start_pose
        while num_poses > 0 and current_pose.get_options() != []:
            L = current_pose.get_options()
            test = random.choice(L)
            if test in warm_up_poses and test != self.poses[len(self.poses)-1]:
                self.poses.append(test)
                num_poses -= 1
                current_pose = test
            else:
                L.remove(test)

    def __str__(self):
        return_string = ''
        for x in self.poses:
            return_string += str(x) + ' --> '
        return return_string[:-5]

W = WarmUp()
W.add_poses()
print(W)
# def generate_flow():
#     pass
#
# def main():
#     generate_flow()
#
# if __name__ == '__main__':
#     main()
