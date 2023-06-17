import bpy
import re
import datetime
print("=== Start at",datetime.datetime.now().strftime('%X'),"===")

#1:CGSS 2:CGSS motion 3:SIFAS 4:starlit season motion
dic_sel = 4

dic_cgss = {
"Position":"全ての親",
"Hip":"下半身","Root":"上半身0","Neck":"首","Head":"頭","Waist":"上半身1","Chest":"上半身2",

"Shoulder_L":"左肩","Arm_L":"左腕","Elbow_L":"左ひじ","Wrist_L":"左手首",
"Thigh_L":"左足","Knee_L":"左ひざ","Ankle_L":"左足首","Toe_L":"左つま先",

"Thumb_01_L":"左親指０","Thumb_02_L":"左親指１","Thumb_03_L":"左親指２",
"Iindex_01_L":"左人指１","Index_02_L":"左人指２","Index_03_L":"左人指３",
"Middle_01_L":"左中指１","Middle_02_L":"左中指２","Middle_03_L":"左中指３",
"Ring_01_L":"左薬指１","Ring_02_L":"左薬指２","Ring_03_L":"左薬指３",
"Pinky_01_L":"左小指１","Pinky_02_L":"左小指２","Pinky_03_L":"左小指３",

"Shoulder_R":"右肩","Arm_R":"右腕","Elbow_R":"右ひじ","Wrist_R":"右手首",
"Thigh_R":"右足","Knee_R":"右ひざ","Ankle_R":"右足首","Toe_R":"右つま先",

"Thumb_01_R":"右親指０","Thumb_02_R":"右親指１","Thumb_03_R":"右親指２",
"Iindex_01_R":"右人指１","Index_02_R":"右人指２","Index_03_R":"右人指３",
"Middle_01_R":"右中指１","Middle_02_R":"右中指２","Middle_03_R":"右中指３",
"Ring_01_R":"右薬指１","Ring_02_R":"右薬指２","Ring_03_R":"右薬指３",
"Pinky_01_R":"右小指１","Pinky_02_R":"右小指２","Pinky_03_R":"右小指３",

"Eye_L":"左目","Eye_R":"右目"
}

dic_cgss_mot = {
"Position":"センター",
"Hip":"下半身","Root":"グルーブ","Neck":"首","Head":"頭","Waist":"上半身","Chest":"上半身2",

"Shoulder_L":"左肩","Arm_L":"左腕","Elbow_L":"左ひじ","Wrist_L":"左手首",
"Thigh_L":"左足","Knee_L":"左ひざ","Ankle_L":"左足首","Toe_L":"左つま先",

"Thumb_01_L":"左親指０","Thumb_02_L":"左親指１","Thumb_03_L":"左親指２",
"Iindex_01_L":"左人指１","Index_02_L":"左人指２","Index_03_L":"左人指３",
"Middle_01_L":"左中指１","Middle_02_L":"左中指２","Middle_03_L":"左中指３",
"Ring_01_L":"左薬指１","Ring_02_L":"左薬指２","Ring_03_L":"左薬指３",
"Pinky_01_L":"左小指１","Pinky_02_L":"左小指２","Pinky_03_L":"左小指３",

"Shoulder_R":"右肩","Arm_R":"右腕","Elbow_R":"右ひじ","Wrist_R":"右手首",
"Thigh_R":"右足","Knee_R":"右ひざ","Ankle_R":"右足首","Toe_R":"右つま先",

"Thumb_01_R":"右親指０","Thumb_02_R":"右親指１","Thumb_03_R":"右親指２",
"Iindex_01_R":"右人指１","Index_02_R":"右人指２","Index_03_R":"右人指３",
"Middle_01_R":"右中指１","Middle_02_R":"右中指２","Middle_03_R":"右中指３",
"Ring_01_R":"右薬指１","Ring_02_R":"右薬指２","Ring_03_R":"右薬指３",
"Pinky_01_R":"右小指１","Pinky_02_R":"右小指２","Pinky_03_R":"右小指３"
}

dic_sifas = {
"Position":"全ての親",
"Hip":"下半身","Spine":"上半身0","Neck":"首","Head":"頭","Spine1":"上半身1","Spine2":"上半身2",

"LeftShoulder":"左肩","LeftArm":"左腕","LeftArmRoll":"左腕","LeftForeArm":"左ひじ","LeftForeArmRoll":"左ひじ","LeftHand":"左手首",
"LeftUpLeg":"左足","LeftLeg":"左ひざ","LeftFoot":"左足首","LeftToeBase":"左つま先",

"LeftHandThumb1":"左親指０","LeftHandThumb2":"左親指１","LeftHandThumb3":"左親指２",
"LeftHandIndex1":"左人指１","LeftHandIndex2":"左人指２","LeftHandIndex3":"左人指３",
"LeftHandMiddle1":"左中指１","LeftHandMiddle2":"左中指２","LeftHandMiddle3":"左中指３",
"LeftHandRing1":"左薬指１","LeftHandRing2":"左薬指２","LeftHandRing3":"左薬指３",
"LeftHandPinky1":"左小指１","LeftHandPinky2":"左小指２","LeftHandPinky3":"左小指３",

"RightShoulder":"右肩","RightArm":"右腕","RightArmRoll":"右腕","RightForeArm":"右ひじ","RightForeArmRoll":"右ひじ","RightHand":"右手首",
"RightUpLeg":"右足","RightLeg":"右ひざ","RightFoot":"右足首","RightToeBase":"右つま先",

"RightHandThumb1":"右親指０","RightHandThumb2":"右親指１","RightHandThumb3":"右親指２",
"RightHandIndex1":"右人指１","RightHandIndex2":"右人指２","RightHandIndex3":"右人指３",
"RightHandMiddle1":"右中指１","RightHandMiddle2":"右中指２","RightHandMiddle3":"右中指３",
"RightHandRing1":"右薬指１","RightHandRing2":"右薬指２","RightHandRing3":"右薬指３",
"RightHandPinky1":"右小指１","RightHandPinky2":"右小指２","RightHandPinky3":"右小指３",
}

dic_starlit = {
#"AO_Attach_L"
#"AO_Attach_R"
"AO_Base":"グルーブ","AO_Neck":"首","AO_Head":"頭",
"AO_Hips":"下半身",
#"AO_Looktarget""AO_Position"
"AO_Spine":"上半身","AO_Spine1":"上半身1","AO_Spine2":"上半身2",

"AO_UpLeg_L":"左足","AO_Leg_L":"左ひざ","AO_Foot_L":"左足首","AO_Toe_L":"左つま先",
"AO_UpLeg_R":"右足","AO_Leg_R":"右ひざ","AO_Foot_R":"右足首","AO_Toe_R":"右つま先",

"AO_Shoulder_L":"左肩","AO_Arm_L":"左腕","AO_ForeArm_L":"左ひじ","AS_Hand_L":"左手首",
"AO_Shoulder_R":"右肩","AO_Arm_R":"右腕","AO_ForeArm_R":"右ひじ","AS_Hand_R":"右手首",

"AS_Thumb1_R":"右親指０","AS_Thumb2_R":"右親指１","AS_Thumb3_R":"右親指２",
"AS_Index1_R":"右人指１","AS_Index2_R":"右人指２","AS_Index3_R":"右人指３",
"AS_Middle1_R":"右中指１","AS_Middle2_R":"右中指２","AS_Middle3_R":"右中指３",
#"AS_Ring_R":""
"AS_Ring1_R":"右薬指１","AS_Ring2_R":"右薬指２","AS_Ring3_R":"右薬指３",
"AS_Pinky1_R":"右小指１","AS_Pinky2_R":"右小指２","AS_Pinky3_R":"右小指３",

"AS_Thumb1_L":"左親指０","AS_Thumb2_L":"左親指１","AS_Thumb3_L":"左親指２",
"AS_Index1_L":"左人指１","AS_Index2_L":"左人指２","AS_Index3_L":"左人指３",
"AS_Middle1_L":"左中指１","AS_Middle2_L":"左中指２","AS_Middle3_L":"左中指３",
#"AS_Ring_L":""
"AS_Ring1_L":"左薬指１","AS_Ring2_L":"左薬指２","AS_Ring3_L":"左薬指３",
"AS_Pinky1_L":"左小指１","AS_Pinky2_L":"左小指２","AS_Pinky3_L":"左小指３",
}

#CGSS部分
if dic_sel == 1 :
    dic=dic_cgss
    target_obj=bpy.context.active_object

#CGSS动作部分
if dic_sel == 2 :
    dic=dic_cgss_mot
    target_obj=bpy.context.active_object

#SIFAS部分
if dic_sel == 3 :
    dic=dic_sifas
    target_obj=bpy.data.objects['Move']

elif dic_sel == 4 :
    dic=dic_starlit
    target_obj=bpy.context.active_object

else :
    print("Wrong input.")
    exit

#对象为空时跳出
if target_obj == "":
    print ("Empty object input!")
    exit

print("Armature selected:",target_obj.name)
print("The current armature has",len(target_obj.data.bones),"Bones")

for single_bone in target_obj.data.bones:
    rename=""
    name_in=single_bone.name

    if name_in not in dic.keys():
        print("bone",name_in,"is not in dictionary")
        continue
    
    else:
        rename=dic[name_in]
        target_obj.data.bones[name_in].name = rename
        print("bone",name_in,"has been renamed to",rename)
        
print("=== Done. ===")
