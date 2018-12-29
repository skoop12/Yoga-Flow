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

# Poses ----------------------------------------------------

# Initialization Poses
down_dog = Pose('Down Dog')
chaturanga = Pose('Chaturanga', [down_dog])
half_way_lift = Pose('Half Way Lift', [chaturanga])
forward_fold = Pose('Forward Fold', [half_way_lift])
down_dog.add(forward_fold)
mountain = Pose('Mountain', [chaturanga])
forward_fold.add(mountain)

# Warm Up Poses
table_top = Pose('Table Top', [down_dog])
child = Pose('Childs Pose', [table_top, down_dog])
puppy = Pose('Puppy Pose', [table_top, down_dog])
cat_cow = Pose('Cat Cows', [puppy, table_top, down_dog])
table_top.add(cat_cow)
table_top.add(puppy)

# Sun A Poses
godess_backbend = Pose('Goddess Arm Backbend', [mountain, forward_fold])
waterfall_backbend = Pose('Waterfall Arm Backbend', [mountain, forward_fold])
open_twist = Pose('Open Arm Twist', [mountain, godess_backbend, waterfall_backbend, forward_fold])
heart_center = Pose('Hands at Heart Center', [mountain, forward_fold])
crouch_curl = Pose('Crouch and Curl', [forward_fold])
mountain.add(forward_fold)
mountain.add(godess_backbend)
mountain.add(waterfall_backbend)
mountain.add(open_twist)
mountain.add(heart_center)
godess_backbend.add(waterfall_backbend)
godess_backbend.add(open_twist)
waterfall_backbend.add(open_twist)

# Sun B Poses
chair = Pose('Chair', [mountain, forward_fold])
prayer_twist = Pose('Prayer Twist',[chair])
chair_plane = Pose('Chair With Airplane Arms',[chair, prayer_twist])
drinking_bird = Pose('Drinking Bird',[chair, chair_plane, heart_center])
chair_open_twist = Pose('Chair With Open Arm Twist',[chair])
chair.add(prayer_twist)
chair.add(chair_plane)
chair.add(drinking_bird)
chair.add(chair_open_twist)

low_lunge = Pose('Low Lunge', [chaturanga])
knee_to_nose = Pose('Knee to Nose', [low_lunge])
knee_to_elbows = Pose('Knew to Elbows')
leg_lift = Pose('Leg Lift', [knee_to_nose,knee_to_elbows,low_lunge])
knee_to_nose.add(leg_lift)
knee_to_elbows.add(leg_lift)

triangle = Pose('Triangle', [chaturanga])
warrior_two = Pose('Warrior II', [triangle, chaturanga])
pyramid = Pose('Pyramid', [low_lunge, forward_fold])
warrior_one = Pose('Warrior I', [warrior_two, chaturanga])
humble_warrior = Pose('Humble Warrior', [warrior_one])
extended_side = Pose('Extended Side Angle', [warrior_two])
half_moon = Pose('Half Moon', [warrior_two])
warrior_two.add(half_moon)
triangle.add(half_moon)
warrior_two.add(extended_side)
warrior_one.add(humble_warrior)
triangle.add(warrior_two)
low_lunge.add(warrior_two)
low_lunge.add(pyramid)
low_lunge.add(warrior_one)
pyramid.add(warrior_one)



start_poses = [child]
warm_up_poses = [down_dog, table_top, puppy, cat_cow]
sun_a_poses = [mountain, forward_fold, heart_center, half_way_lift, godess_backbend, waterfall_backbend, open_twist]
sun_a_end = [crouch_curl, chaturanga]


hip_poses = []
arm_poses= []
chair_variation = []

class Flow:
    def __str__(self):
        return_string = ''
        for x in self.poses:
            return_string += str(x) + ' --> '
        return return_string[:-5]

class WarmUp(Flow):
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

class SunA(Flow):
    def __init__(self):
        self.start_pose = mountain
        self.poses = [down_dog, forward_fold, self.start_pose]

    def add_poses(self):
        num_poses = random.randint(1,6)
        current_pose = self.start_pose
        while num_poses > 0 and current_pose.get_options() != []:
            L = current_pose.get_options()
            test = random.choice(L)
            if test in sun_a_poses and test != self.poses[len(self.poses)-1]:
                self.poses.append(test)
                num_poses -= 1
                current_pose = test
            else:
                L.remove(test)
        self.poses.append(random.choice(sun_a_end))

class SunB(Flow):
    def __init__(self):
        self.poses = [down_dog, forward_fold, chair]

    def add_poses(self):
        num_poses = random.randint(1,5)
        current_pose = chair
        while num_poses > 0 and current_pose.get_options() != []:
            L = current_pose.get_options()
            test = random.choice(L)
            if test != self.poses[len(self.poses)-1]:
                self.poses.append(test)
                num_poses -= 1
                current_pose = test
            else:
                L.remove(test)
        num_poses = random.randint(8,15)
        self.poses.append(down_dog)
        current_pose = leg_lift
        self.poses.append(current_pose)
        while num_poses > 0 and current_pose.get_options() != []:
            L = current_pose.get_options()
            test = random.choice(L)
            if test != self.poses[len(self.poses)-1]:
                self.poses.append(test)
                num_poses -= 1
                current_pose = test
            else:
                L.remove(test)



W = WarmUp()
W.add_poses()
A = SunA()
A.add_poses()
B = SunB()
B.add_poses()
print(W)
print(A)
print(B)

# def generate_flow():
#     pass
#
# def main():
#     generate_flow()
#
# if __name__ == '__main__':
#     main()
