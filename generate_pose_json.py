import os
import json

# Create openpose_json folder
dst = "assets/test/openpose_json"
os.makedirs(dst, exist_ok=True)

# Create placeholder pose keypoints for each person
# OpenPose format: 25 keypoints x 3 (x, y, confidence)
# For dummy data, use random positions with high confidence
pose_template = {
    "people": [
        {
            "pose_keypoints_2d": [
                # 25 keypoints in OpenPose format
                256.0, 100.0, 0.9,  # 0: Nose
                240.0, 80.0, 0.9,   # 1: Neck
                220.0, 60.0, 0.8,   # 2: RShoulder
                200.0, 40.0, 0.8,   # 3: RElbow
                180.0, 30.0, 0.7,   # 4: RWrist
                280.0, 60.0, 0.8,   # 5: LShoulder
                300.0, 40.0, 0.8,   # 6: LElbow
                320.0, 30.0, 0.7,   # 7: LWrist
                230.0, 150.0, 0.9,  # 8: MidHip
                210.0, 200.0, 0.8,  # 9: RHip
                190.0, 260.0, 0.8,  # 10: RKnee
                185.0, 320.0, 0.7,  # 11: RAnkle
                250.0, 200.0, 0.8,  # 12: LHip
                270.0, 260.0, 0.8,  # 13: LKnee
                275.0, 320.0, 0.7,  # 14: LAnkle
                245.0, 90.0, 0.9,   # 15: REye
                265.0, 90.0, 0.9,   # 16: LEye
                240.0, 85.0, 0.8,   # 17: REar
                270.0, 85.0, 0.8,   # 18: LEar
                230.0, 120.0, 0.7,  # 19: LBigToe
                235.0, 120.0, 0.7,  # 20: LSmallToe
                225.0, 125.0, 0.6,  # 21: LHeel
                280.0, 120.0, 0.7,  # 22: RBigToe
                285.0, 120.0, 0.7,  # 23: RSmallToe
                275.0, 125.0, 0.6,  # 24: RHeel
            ]
        }
    ]
}

# Create JSON files for each person
for i in range(1, 7):
    person_name = f"person{i}"
    json_file = os.path.join(dst, f"{person_name}_keypoints.json")
    with open(json_file, 'w') as f:
        json.dump(pose_template, f, indent=2)
    print(f"✅ Created {person_name}_keypoints.json")

print("✅ All pose JSON files created!")
