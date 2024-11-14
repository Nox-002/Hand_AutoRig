'''
This autorig was made on maya 2023 by Charlie COUCOUREUX

If you encounter any problem you can contact me to charlie.coucoureux@gmail.com

Dont hesitate to send me your future rig you'll made with this setup !

Here is the video link to the tutorial : https://vimeo.com/1029667649


When you run the autorig you have to follow this steps to integrate it to your rig 
1- Dont forget to create the "ctrl hand gen" 
2- Your have to parent the locators to the good part of your body in aim to have all the space if you want - And keep the offset for the RT part
3- You have to constaint only the DRV_*nameofthefinger*_1_Lt joint of every fingers to your wrist to make the setup follow your hand


'''




import maya.cmds as cmds
import threading
def OFF():
    selectedObjects = cmds.ls(selection=True)
    if len(selectedObjects) ==1:
        node = selectedObjects[0]   
        if cmds.objExists('OFF_' + node):
            raise ValueError('none')
        else:
            off = cmds.createNode('transform', name='OFF_' + node)
            cmds.matchTransform(off, node)
            cmds.parent(node, off)
            cmds.select(clear=True)
    else:
        raise ValueError('!!!')
def mz_combineShapes(self):
    #store the names of transform nodes
    selObj = cmds.ls(selection = 1)
    #freeze transformations
    cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
    #delete history
    cmds.delete(constructionHistory = 1)
    #store the names of shape nodes
    objShape = cmds.listRelatives(selObj, shapes = 1)
    
    for i in xrange(len(objShape)-1):
        #parent the shape nodes to the last transform node
        cmds.parent(objShape[i],selObj[-1],add = 1, shape = 1)
        #delete the unused transform nodes
        cmds.delete(selObj[i])
        cmds.select(selObj[-1], replace = 1)    
  
  
def index_rig_lt():


    
    def spawn_hand_control_Lt(*args):

        global controler_hand_control

        controler_hand_control = cmds.curve(n='Ctrl_Control_Hand_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\
                point = [(5.8520521406535408e-007, 0, -1.0398099422454834),\
                         (1.2360682487487793, 0, -3.8042259216308594),\
                         (3.2360701560974121, 0, -2.351142406463623),\
                         (0.69169783592224121, 0, -0.53726297616958618),\
                         (3.9999988079071045, 0, 2.2737367544323206e-013),\
                         (3.2360680103302002, 0, 2.3511412143707275),\
                         (0.42749345302581787, 0, 0.27587676048278809),\
                         (1.2360677719116211, 0, 3.8042242527008057),\
                         (-1.2360682487487793, 0, 3.8042266368865967),\
                         (-0.42749285697937012, 0, 0.27587652206420898),\
                         (-3.236067533493042, 0, 2.3511402606964111),\
                         (-4.0000009536743164, 0, 0),\
                         (-0.6916964054107666, 0, -0.53726291656494141),\
                         (-3.2360677719116211, 0, -2.3511404991149902),\
                         (-1.2360686063766479, 0, -3.8042278289794922),\
                         (5.8520521406535408e-007, 0, -1.0398099422454834)]\
              )

        cmds.setAttr(controler_hand_control + '.translateX', 54)
        cmds.setAttr(controler_hand_control + '.translateY', 101)
        cmds.setAttr(controler_hand_control + '.translateZ', -21)
        cmds.setAttr(controler_hand_control + '.rotateZ', -45)
        cmds.addAttr(controler_hand_control, longName='Switch_IKFK', attributeType='double', min=0, max=1, dv=1, k=True )
        cmds.addAttr(controler_hand_control, longName='BendArm', attributeType='bool', dv=True, k=True )
        cmds.addAttr(controler_hand_control, longName='Power_Knuckle', attributeType='double', min=0, max=3, dv=1, k=True )
        cmds.addAttr(controler_hand_control, longName='Power_Tendons', attributeType='double', min=0, max=3, dv=1, k=True )
        cmds.addAttr(controler_hand_control, longName='FK_Finger_Visibility',  attributeType='bool', dv=True, k=True  )


        duplication_ctrl_hand_control = cmds.duplicate(controler_hand_control, rc=True)
        group_miror_hand_control_temp = cmds.group(empty=True , n='Grp_Miror_Hand_temp')
        cmds.parent(duplication_ctrl_hand_control,group_miror_hand_control_temp)
        cmds.setAttr(group_miror_hand_control_temp + '.scaleX', -1)
        cmds.parent(duplication_ctrl_hand_control,w=True)
        cmds.delete(group_miror_hand_control_temp)
        

        cmds.select(controler_hand_control)
        OFF()
        cmds.select(duplication_ctrl_hand_control)
        cmds.rename('Ctrl_Control_Hand_Rt')
        OFF()

        # controler_hand_control = cmds.curve(n='Ctrl_Control_Hand_Lt', degree = 1,\
        #         knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\
        #         point = [(5.8520521406535408e-007, 0, -1.0398099422454834),\
        #                  (1.2360682487487793, 0, -3.8042259216308594),\
        #                  (3.2360701560974121, 0, -2.351142406463623),\
        #                  (0.69169783592224121, 0, -0.53726297616958618),\
        #                  (3.9999988079071045, 0, 2.2737367544323206e-013),\
        #                  (3.2360680103302002, 0, 2.3511412143707275),\
        #                  (0.42749345302581787, 0, 0.27587676048278809),\
        #                  (1.2360677719116211, 0, 3.8042242527008057),\
        #                  (-1.2360682487487793, 0, 3.8042266368865967),\
        #                  (-0.42749285697937012, 0, 0.27587652206420898),\
        #                  (-3.236067533493042, 0, 2.3511402606964111),\
        #                  (-4.0000009536743164, 0, 0),\
        #                  (-0.6916964054107666, 0, -0.53726291656494141),\
        #                  (-3.2360677719116211, 0, -2.3511404991149902),\
        #                  (-1.2360686063766479, 0, -3.8042278289794922),\
        #                  (5.8520521406535408e-007, 0, -1.0398099422454834)]\
        #       )

        # cmds.setAttr(controler_hand_control + '.translateX', 54)
        # cmds.setAttr(controler_hand_control + '.translateY', 101)
        # cmds.setAttr(controler_hand_control + '.translateZ', -21)
        # cmds.setAttr(controler_hand_control + '.rotateZ', -45)
        # cmds.addAttr(controler_hand_control, longName='Power_Knuckle', attributeType='double', min=0, max=3, dv=1, k=True )
        # cmds.addAttr(controler_hand_control, longName='Power_Tendons', attributeType='double', min=0, max=3, dv=1, k=True )

    # def Miror_hand_control_Lt_Rt(*args):

    #     duplication_ctrl_hand_control = cmds.duplicate(controler_hand_control, rc=True)
    #     group_miror_hand_control_temp = cmds.group(empty=True , n='Grp_Miror_Hand_temp')
    #     cmds.parent(duplication_ctrl_hand_control,group_miror_hand_control_temp)
    #     cmds.setAttr(group_miror_hand_control_temp + '.scaleX', -1)
    #     cmds.parent(duplication_ctrl_hand_control,w=True)
    #     cmds.delete(group_miror_hand_control_temp)
        

    #     cmds.select(controler_hand_control)
    #     OFF()
    #     cmds.select(duplication_ctrl_hand_control)
    #     cmds.rename('Ctrl_Control_Hand_Rt')
    #     OFF()
###

    def index_rig_Part_1(*args):
        
        global joint_DRV_Index_1_Lt
        global joint_DRV_Index_2_Lt
        global joint_DRV_Index_3_Lt
        global joint_DRV_Index_4_Lt
        global joint_DRV_Index_T_Lt
        global curve_MP_Index_Lt
        global joint_DRV_Index_3_OFF_Lt
        global joint_DRV_Index_4_OFF_Lt
        
        global joint_Index_Tendon_1_Lt
        global joint_Index_Tendon_2_Lt
        global joint_Index_Tendon_3_Lt
        global joint_Index_Tendon_4_Lt
        global curve_MP_Index_Tendon_Lt
        global joint_Index_Tendon_OFF_1_Lt
        global joint_Index_Tendon_OFF_2_Lt
        global joint_Index_Tendon_OFF_3_Lt
        global joint_Index_Tendon_OFF_4_Lt
        global loc_Index_orientaton_joints_Lt
        global loc_Index_orientaton_joints_Lt_grp

        
        
        


        cmds.select(deselect=True)
        joint_DRV_Index_1_Lt = cmds.joint(n='DRV_Index_1_Lt', p=(55.8, 105.4, -4.5))
        joint_DRV_Index_2_Lt = cmds.joint(n='DRV_Index_2_Lt', p=(61, 101, -3.8))
        joint_DRV_Index_3_Lt = cmds.joint(n='DRV_Index_3_Lt', p=(5, 0, 5))
        joint_DRV_Index_4_Lt = cmds.joint(n='DRV_Index_4_Lt', p=(10, 0, 5))
        joint_DRV_Index_T_Lt = cmds.joint(n='DRV_Index_T_Lt', p=(67, 93, -3.3), rad=0.5)

        cmds.parent(joint_DRV_Index_T_Lt, world=True)
        cmds.parent(joint_DRV_Index_4_Lt, world=True)
        cmds.parent(joint_DRV_Index_3_Lt, world=True)
        cmds.parent(joint_DRV_Index_2_Lt, world=True)
        
       
        
        joint_Index_Tendon_1_Lt = cmds.joint(n='Sk_Index_Tendon_1_Lt', p=(-8, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Index_Tendon_2_Lt = cmds.joint(n='Sk_Index_Tendon_2_Lt', p=(-6, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Index_Tendon_3_Lt = cmds.joint(n='Sk_Index_Tendon_3_Lt', p=(-4, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Index_Tendon_4_Lt = cmds.joint(n='Sk_Index_Tendon_4_Lt', p=(-2, 0, 5), rad=0.2)

        # cmds.parent(joint_Index_Tendon_1_Lt, world=True)
        # cmds.parent(joint_Index_Tendon_2_Lt, world=True)
        # cmds.parent(joint_Index_Tendon_3_Lt, world=True)
        # cmds.parent(joint_Index_Tendon_4_Lt, world=True)
        jnt_finger_Index = [joint_DRV_Index_3_Lt,joint_DRV_Index_4_Lt,joint_Index_Tendon_1_Lt,joint_Index_Tendon_2_Lt,joint_Index_Tendon_3_Lt,joint_Index_Tendon_4_Lt]
        for offset in jnt_finger_Index :
            cmds.select(offset)
            OFF()


        joint_DRV_Index_3_OFF_Lt = cmds.listRelatives(joint_DRV_Index_3_Lt, parent=True, fullPath=True)        
        joint_DRV_Index_4_OFF_Lt = cmds.listRelatives(joint_DRV_Index_4_Lt, parent=True, fullPath=True)

        joint_Index_Tendon_OFF_1_Lt = cmds.listRelatives(joint_Index_Tendon_1_Lt, parent=True, fullPath=True)
        joint_Index_Tendon_OFF_2_Lt = cmds.listRelatives(joint_Index_Tendon_2_Lt, parent=True, fullPath=True)
        joint_Index_Tendon_OFF_3_Lt = cmds.listRelatives(joint_Index_Tendon_3_Lt, parent=True, fullPath=True)
        joint_Index_Tendon_OFF_4_Lt = cmds.listRelatives(joint_Index_Tendon_4_Lt, parent=True, fullPath=True)



        jnt_0_Crv_Position_Index = cmds.xform(joint_DRV_Index_1_Lt, query=True, worldSpace=True, translation=True)
        jnt_1_Crv_Position_Index = cmds.xform(joint_DRV_Index_2_Lt, query=True, worldSpace=True, translation=True)
        jnt_2_Crv_Position_Index = cmds.xform(joint_DRV_Index_T_Lt, query=True, worldSpace=True, translation=True)
        joint_Skin_Crv_Index_1_Lt = [joint_DRV_Index_2_Lt , joint_DRV_Index_T_Lt]
        joint_Skin_Crv_Index_2_Lt = [joint_DRV_Index_1_Lt ,joint_DRV_Index_2_Lt]

        curve_MP_Index_Lt = cmds.curve(d=1, p=[jnt_1_Crv_Position_Index, jnt_2_Crv_Position_Index], n='Crv_MP_Index_Lt_Temp')
        curve_MP_Index_Tendon_Lt = cmds.curve(d=1, p=[jnt_0_Crv_Position_Index, jnt_1_Crv_Position_Index], n='Crv_MP_Index_Tendon_Lt_Temp')

        bind_skin_cluster_Index = cmds.skinCluster(joint_Skin_Crv_Index_1_Lt, curve_MP_Index_Lt, tsb=True)
        bind_skin_cluster_tendon_Index = cmds.skinCluster(joint_Skin_Crv_Index_2_Lt, curve_MP_Index_Tendon_Lt, tsb=True)



        cmds.pathAnimation( joint_DRV_Index_3_OFF_Lt, c=curve_MP_Index_Lt, su=0.3333, follow=True)
        cmds.pathAnimation( joint_DRV_Index_4_OFF_Lt, c=curve_MP_Index_Lt, su=0.6666, follow=True)

        cmds.pathAnimation( joint_Index_Tendon_OFF_1_Lt, c=curve_MP_Index_Tendon_Lt, su=0.2, follow=True)
        cmds.pathAnimation( joint_Index_Tendon_OFF_2_Lt, c=curve_MP_Index_Tendon_Lt, su=0.4, follow=True)
        cmds.pathAnimation( joint_Index_Tendon_OFF_3_Lt, c=curve_MP_Index_Tendon_Lt, su=0.6, follow=True)
        cmds.pathAnimation( joint_Index_Tendon_OFF_4_Lt, c=curve_MP_Index_Tendon_Lt, su=0.8, follow=True)
        

        attributes_to_lock_Index = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Index:
            cmds.setAttr(joint_DRV_Index_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_DRV_Index_4_Lt + "." + attr, lock=True)

        attributes_to_lock_tendon_Index = ["rotateX","rotateY","rotateZ","translateX","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_tendon_Index:
            cmds.setAttr(joint_Index_Tendon_1_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Index_Tendon_2_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Index_Tendon_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Index_Tendon_4_Lt + "." + attr, lock=True)


        
        cmds.select(deselect=True)
        list_grp_placement_jnt = [joint_DRV_Index_1_Lt, joint_DRV_Index_2_Lt, joint_DRV_Index_T_Lt]
        grp_name = "Grp_Deplacement_Groupe_Main_Temp"
        if cmds.objExists(grp_name):
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)
        
        else:
            cmds.group(em=True, n=grp_name)
               
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)

        
        # cmds.setAttr(joint_DRV_Index_1_Lt + ".translatex" + attr, lock=True)

        #loc orientation du doigt
        loc_Index_orientaton_joints_Lt = cmds.spaceLocator(n='LOC_Guide_Orient_Index_Lt_TEMP', p=(0, 0, 0), )
        
        
        cmds.select(loc_Index_orientaton_joints_Lt)
        loc_Index_orientaton_joints_Lt_grp = cmds.group(loc_Index_orientaton_joints_Lt[0], n= 'temp_loc_Index')
        loc_Index_orientaton_joints_Lt_grp = cmds.listRelatives(loc_Index_orientaton_joints_Lt, parent=True, fullPath=True)
        cmds.pathAnimation( loc_Index_orientaton_joints_Lt_grp, c=curve_MP_Index_Lt, su=0.5, follow=True)
        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + '.rotateX', 90)
        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + '.rotateY', 0)
        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + '.rotateZ', 90)

        attributes_to_lock_LOC_Index = ["rotateY","rotateZ","translateX","translateY","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_LOC_Index:
            cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + "." + attr, lock=True)

        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + ".localScaleX" ,0.25)
        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + ".localScaleY" ,2.25)
        cmds.setAttr(loc_Index_orientaton_joints_Lt[0] + ".localScaleZ" ,0.25)


        #display color indication

        jnt_color_green = [joint_DRV_Index_1_Lt,joint_DRV_Index_2_Lt, joint_DRV_Index_T_Lt, loc_Index_orientaton_joints_Lt[0]]
        jnt_color_yellow= [joint_Index_Tendon_1_Lt , joint_Index_Tendon_2_Lt, joint_Index_Tendon_3_Lt, joint_Index_Tendon_4_Lt, joint_DRV_Index_3_Lt, joint_DRV_Index_4_Lt ]

        for objcolorgreen in jnt_color_green : 
            cmds.setAttr(objcolorgreen + '.overrideEnabled', 1)
            cmds.setAttr(objcolorgreen + '.overrideColor', 14)

        for objcoloryelllow in jnt_color_yellow : 
            cmds.setAttr(objcoloryelllow + '.overrideEnabled', 1)
            cmds.setAttr(objcoloryelllow + '.overrideColor', 17)
         
    def index_rig_Part_2(*args):

        global group_ctrls_Index_Lt
        global group_joints_Index_Lt
        global new_Effector_name_Inde
        global group_miror_Index_Loc_Space_IK_temp_Lt
        global locator_Finger_HipSpace_IK_Index_ctrl
        global locator_Finger_HeadSpace_IK_Index_ctrl
        global locator_Finger_HandSpace_IK_Index_ctrl

        # global locator_Finger_Space_PV_Index_ctrl


        controler_hand_control = 'Ctrl_Control_Hand_Lt'

        cmds.delete(curve_MP_Index_Lt, curve_MP_Index_Tendon_Lt)

        attributes_to_lock_Index = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Index:
            cmds.setAttr(joint_DRV_Index_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_DRV_Index_4_Lt + "." + attr, lock=False)

        attributes_to_lock_tendon_Index = ["translateX"]
        for attr in attributes_to_lock_tendon_Index:
            cmds.setAttr(joint_Index_Tendon_1_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Index_Tendon_2_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Index_Tendon_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Index_Tendon_4_Lt + "." + attr, lock=False)




        ################################


        # orient le premier jnt 01 sans affecter les autres
        cmds.parent(joint_DRV_Index_2_Lt, joint_DRV_Index_1_Lt)
        cmds.joint(joint_DRV_Index_1_Lt, edit=True, oj = 'xyz', sao='yup')
        cmds.parent(joint_DRV_Index_2_Lt, world=True)
        cmds.matchTransform(joint_DRV_Index_1_Lt,loc_Index_orientaton_joints_Lt, rx=True, ry=False, rz=False)






        cmds.matchTransform(joint_DRV_Index_2_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Index_3_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Index_4_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Index_T_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        
        
        cmds.parent(joint_DRV_Index_T_Lt, joint_DRV_Index_4_Lt)
        cmds.parent(joint_DRV_Index_4_Lt, joint_DRV_Index_3_Lt)
        cmds.parent(joint_DRV_Index_3_Lt, joint_DRV_Index_2_Lt)
        cmds.parent(joint_DRV_Index_2_Lt, joint_DRV_Index_1_Lt)
        cmds.delete (joint_DRV_Index_3_OFF_Lt,joint_DRV_Index_4_OFF_Lt)





        
        

        

        #cmds.joint(joint_DRV_Index_1_Lt, edit=True, oj = 'xzy', sao='ydown', ch=False)                                   #probleme 
        
        # cmds.joint(joint_DRV_Index_2_Lt, edit=True, oj = 'xzy', sao='ydown')
        # cmds.joint(joint_DRV_Index_3_Lt, edit=True, oj = 'xzy', sao='ydown')              plus utile
        # cmds.joint(joint_DRV_Index_4_Lt, edit=True, oj = 'xzy', sao='ydown')
        # cmds.joint(joint_DRV_Index_T_Lt, edit=True, oj = 'none')
        


        cmds.select(deselect=True)
        joint_Index_1_Lt = cmds.joint(  n='Sk_Index_1_Lt', rad=0.25 )
        cmds.matchTransform(joint_Index_1_Lt,joint_DRV_Index_1_Lt)
        cmds.select(deselect=True)
        joint_Index_2_Lt = cmds.joint( n='Sk_Index_2_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Index_2_Lt,joint_DRV_Index_2_Lt)
        joint_Index_3_Lt = cmds.joint(  n='Sk_Index_3_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Index_3_Lt,joint_DRV_Index_3_Lt)
        joint_Index_4_Lt = cmds.joint(n='Sk_Index_4_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Index_4_Lt,joint_DRV_Index_4_Lt)
        joint_Index_T_Lt = cmds.joint(n='Sk_Index_T_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Index_T_Lt,joint_DRV_Index_T_Lt)



        cmds.parent(joint_Index_T_Lt, joint_Index_4_Lt)
        cmds.parent(joint_Index_4_Lt, joint_Index_3_Lt)
        cmds.parent(joint_Index_3_Lt, joint_Index_2_Lt)
        cmds.parent(joint_Index_2_Lt, joint_Index_1_Lt)

        # cmds.joint(joint_Index_1_Lt, edit=True,oj = 'xzy', sao='ydown', rad=0.25, ch=False)
        # cmds.joint(joint_Index_2_Lt, edit=True,oj = 'xzy', sao='ydown', rad=0.25)
        # cmds.joint(joint_Index_3_Lt, edit=True,oj = 'xzy', sao='ydown', rad=0.25)                  plus utile 
        # cmds.joint(joint_Index_4_Lt, edit=True,oj = 'xzy', sao='ydown', rad=0.25)
        # cmds.joint(joint_Index_T_Lt, edit=True,oj = 'none', rad=0.25)
        # cmds.matchTransform(joint_Index_2_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        # cmds.matchTransform(joint_Index_3_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        # cmds.matchTransform(joint_Index_4_Lt,loc_Index_orientaton_joints_Lt, rot=True)
        # cmds.matchTransform(joint_Index_T_Lt,loc_Index_orientaton_joints_Lt, rot=True)

        #freeze transform jnts avant d'orient
        cmds.select(deselect=True)
        cmds.select(joint_DRV_Index_1_Lt,joint_DRV_Index_2_Lt,joint_DRV_Index_3_Lt,joint_DRV_Index_4_Lt,joint_DRV_Index_T_Lt,joint_Index_1_Lt,joint_Index_2_Lt,joint_Index_3_Lt,joint_Index_4_Lt,joint_Index_T_Lt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        #delete le loc orientation 
        cmds.delete(loc_Index_orientaton_joints_Lt_grp)

        position_joint_DRV_Index_2_Lt = cmds.xform(joint_DRV_Index_2_Lt, query=True, worldSpace=True, translation=True)

        cmds.parent(joint_Index_Tendon_1_Lt, joint_Index_1_Lt)
        cmds.parent(joint_Index_Tendon_2_Lt, joint_Index_1_Lt)
        cmds.parent(joint_Index_Tendon_3_Lt, joint_Index_1_Lt)
        cmds.parent(joint_Index_Tendon_4_Lt, joint_Index_1_Lt)

        cmds.delete(joint_Index_Tendon_OFF_1_Lt,joint_Index_Tendon_OFF_2_Lt,joint_Index_Tendon_OFF_3_Lt,joint_Index_Tendon_OFF_4_Lt)


        ########################



        #creation ctrls
        ctrl_finger_1_Index = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_1_Index_Lt')[0]
        cmds.select(ctrl_finger_1_Index + '.cv[1]', ctrl_finger_1_Index + '.cv[5]')
        cmds.scale(1, 1, 0.194499, relative=True, pivot=(0, 0, 0))
        cmds.select(ctrl_finger_1_Index + '.cv[0]', ctrl_finger_1_Index + '.cv[6]')
        cmds.scale(1, 1, 0.0840956, relative=True, pivot=(0.783612, 0, 0))

        cmds.matchTransform(ctrl_finger_1_Index,joint_Index_1_Lt)
        cmds.select(ctrl_finger_1_Index+'.cv[0:7]')
        cmds.move(0, 2, 0, relative=True, os=True)


        ctrl_finger_2_Index = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_2_Index_Lt')[0]
        cmds.select(ctrl_finger_2_Index + '.cv[1]', ctrl_finger_2_Index + '.cv[5]')
        cmds.scale(1, 1, 0.2, relative=True, pivot=(0, 0, 0))

        cmds.matchTransform(ctrl_finger_2_Index,joint_Index_2_Lt)
        cmds.select(ctrl_finger_2_Index+'.cv[0:7]')
        cmds.move(0, 1.5, 0, relative=True, os=True)


        ctrl_finger_3_Index = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_3_Index_Lt')[0]
        cmds.matchTransform(ctrl_finger_3_Index,joint_Index_3_Lt)
        cmds.select(ctrl_finger_3_Index+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)


        ctrl_finger_4_Index = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_4_Index_Lt')[0]
        cmds.matchTransform(ctrl_finger_4_Index,joint_Index_4_Lt)
        cmds.select(ctrl_finger_4_Index+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)

        ctrl_Ik_Finger_Index = cmds.curve(n='Ctrl_IK_Index_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                point = [(0, 1, 0),\
                         (0, 0.92388000000000003, 0.382683),\
                         (0, 0.70710700000000004, 0.70710700000000004),\
                         (0, 0.382683, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0, -0.382683, 0.92388000000000003),\
                         (0, -0.70710700000000004, 0.70710700000000004),\
                         (0, -0.92388000000000003, 0.382683),\
                         (0, -1, 0),\
                         (0, -0.92388000000000003, -0.382683),\
                         (0, -0.70710700000000004, -0.70710700000000004),\
                         (0, -0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 1, 0),\
                         (0.382683, 0.92388000000000003, 0),\
                         (0.70710700000000004, 0.70710700000000004, 0),\
                         (0.92388000000000003, 0.382683, 0),\
                         (1, 0, 0),\
                         (0.92388000000000003, -0.382683, 0),\
                         (0.70710700000000004, -0.70710700000000004, 0),\
                         (0.382683, -0.92388000000000003, 0),\
                         (0, -1, 0),\
                         (-0.382683, -0.92388000000000003, 0),\
                         (-0.70710700000000004, -0.70710700000000004, 0),\
                         (-0.92388000000000003, -0.382683, 0),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0.382683, 0),\
                         (-0.70710700000000004, 0.70710700000000004, 0),\
                         (-0.382683, 0.92388000000000003, 0),\
                         (0, 1, 0),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (-0.382683, 0, -0.92388000000000003),\
                         (-0.70710700000000004, 0, -0.70710700000000004),\
                         (-0.92388000000000003, 0, -0.382683),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0, 0.382683),\
                         (-0.70710700000000004, 0, 0.70710700000000004),\
                         (-0.382683, 0, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0.382683, 0, 0.92388000000000003),\
                         (0.70710700000000004, 0, 0.70710700000000004),\
                         (0.92388000000000003, 0, 0.382683),\
                         (1, 0, 0),\
                         (0.92388000000000003, 0, -0.382683),\
                         (0.70710700000000004, 0, -0.70710700000000004),\
                         (0.382683, 0, -0.92388000000000003),\
                         (0, 0, -1)]\
              )
        cmds.addAttr(ctrl_Ik_Finger_Index, longName='Space', attributeType='enum', enumName="World:Hand:Head:Hip", k=True )
        cmds.setAttr(ctrl_Ik_Finger_Index + ".Space", 1)
        cmds.matchTransform(ctrl_Ik_Finger_Index,joint_Index_T_Lt)
        cmds.select(ctrl_Ik_Finger_Index+'.cv[0:52]')
        cmds.scale(0.5, 0.5, 0.5, relative=True)
        cmds.move(0, 0, 0, relative=True)
        


        curve_pole_Vector_Index = cmds.curve(n='Crv_PV_Index_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                point = [(-2, 0, 0),\
                         (1, 0, 1),\
                         (1, 0, -1),\
                         (-2, 0, 0),\
                         (1, 1, 0),\
                         (1, 0, 0),\
                         (1, -1, 0),\
                         (-2, 0, 0)]\
              )

        cmds.addAttr(curve_pole_Vector_Index, longName='Guide_Visibility', attributeType='bool', dv=True, k=True )
        cmds.addAttr(curve_pole_Vector_Index, longName='Space', attributeType='enum', enumName="World:Hand:Ik_Finger", k=True )
        cmds.setAttr(curve_pole_Vector_Index + ".Space", 1)
        cmds.matchTransform(curve_pole_Vector_Index,joint_Index_3_Lt)
        cmds.select(curve_pole_Vector_Index)
        cmds.move(0, 3, 0, relative=True, os=True)
        cmds.select(curve_pole_Vector_Index+'.cv[0:7]')
        cmds.rotate(0, 0, 90, relative=True)
        cmds.scale(0.5, 0.5, 0.5, relative=True)

        





        ctrl_finger_Index = [ctrl_finger_1_Index,ctrl_finger_2_Index,ctrl_finger_3_Index,ctrl_finger_4_Index,ctrl_Ik_Finger_Index,curve_pole_Vector_Index]
        for offset in ctrl_finger_Index :
            cmds.select(offset)
            OFF()

        
        ctrl_finger_1_Index_OFF = cmds.listRelatives(ctrl_finger_1_Index, parent=True, fullPath=True)
        ctrl_finger_2_Index_OFF = cmds.listRelatives(ctrl_finger_2_Index, parent=True, fullPath=True)
        ctrl_finger_3_Index_OFF = cmds.listRelatives(ctrl_finger_3_Index, parent=True, fullPath=True)
        ctrl_finger_4_Index_OFF = cmds.listRelatives(ctrl_finger_4_Index, parent=True, fullPath=True)
        
        
        
        cmds.parent(ctrl_finger_4_Index_OFF, ctrl_finger_3_Index)
        cmds.parent(ctrl_finger_3_Index_OFF, ctrl_finger_2_Index)
        cmds.parent(ctrl_finger_2_Index_OFF, ctrl_finger_1_Index)

        cmds.parentConstraint( ctrl_finger_1_Index, joint_Index_1_Lt )
        cmds.parentConstraint( ctrl_finger_2_Index, joint_Index_2_Lt )
        cmds.parentConstraint( ctrl_finger_3_Index, joint_Index_3_Lt )
        cmds.parentConstraint( ctrl_finger_4_Index, joint_Index_4_Lt )
        


        cmds.setAttr(joint_DRV_Index_3_Lt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Index_4_Lt + '.preferredAngleZ', -10.0)

        ik_Handle_Index_Lt = cmds.ikHandle(n='IKRP_Index_Lt',  sj=joint_DRV_Index_2_Lt, ee=joint_DRV_Index_T_Lt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Index_Lt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Index_Lt[0], ctrl_Ik_Finger_Index)
        cmds.poleVectorConstraint( curve_pole_Vector_Index, ik_Handle_Index_Lt[0] )
        


        new_Effector_name_Index = 'EFF_IKRP_Index_Lt'
        List_Input_Ik_Handle_Index = cmds.listConnections('IKRP_Index_Lt',s=True)
        for node in List_Input_Ik_Handle_Index:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Index)
                break
        
        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Index_OFF = cmds.listRelatives(ctrl_finger_1_Index, parent=True, fullPath=True)
        ctrl_finger_2_Index_OFF = cmds.listRelatives(ctrl_finger_2_Index, parent=True, fullPath=True)
        ctrl_finger_3_Index_OFF = cmds.listRelatives(ctrl_finger_3_Index, parent=True, fullPath=True)
        ctrl_finger_4_Index_OFF = cmds.listRelatives(ctrl_finger_4_Index, parent=True, fullPath=True)
        curve_pole_Vector_Index_OFF = cmds.listRelatives(curve_pole_Vector_Index, parent=True, fullPath=True)
        ctrl_Ik_Finger_Index_OFF = cmds.listRelatives(ctrl_Ik_Finger_Index, parent=True, fullPath=True)
        
        decompose_M_DRV_Index_1_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_1_Lt')
        decompose_M_DRV_Index_2_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_2_Lt')
        decompose_M_DRV_Index_3_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_3_Lt')
        decompose_M_DRV_Index_4_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_4_Lt')

        cmds.connectAttr( f'{joint_DRV_Index_1_Lt}.xformMatrix', f'{decompose_M_DRV_Index_1_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_2_Lt}.xformMatrix', f'{decompose_M_DRV_Index_2_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_3_Lt}.xformMatrix', f'{decompose_M_DRV_Index_3_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_4_Lt}.xformMatrix', f'{decompose_M_DRV_Index_4_Lt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Index_1_Lt}.outputTranslate', f'{ctrl_finger_1_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_2_Lt}.outputTranslate', f'{ctrl_finger_2_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_3_Lt}.outputTranslate', f'{ctrl_finger_3_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_4_Lt}.outputTranslate', f'{ctrl_finger_4_Index_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Index_1_Lt}.outputRotate', f'{ctrl_finger_1_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_2_Lt}.outputRotate', f'{ctrl_finger_2_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_3_Lt}.outputRotate', f'{ctrl_finger_3_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_4_Lt}.outputRotate', f'{ctrl_finger_4_Index_OFF[0]}.rotate' )


        cmds.select(deselect=True)
        joint_Index_knuckle = cmds.joint( n='Sk_Index_Knuckle_Lt' , rad=0.75)
        cmds.matchTransform(joint_Index_knuckle,joint_Index_2_Lt)
        cmds.parent(joint_Index_knuckle, joint_Index_2_Lt )
        

        multiply_divide_value_tendon_Index = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Index_Lt')
        multiply_divide_lower_intensity_knuckle_tendon_Index = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Index_Lt')
        multiply_divide_intensity_knuckle_tendon_Index = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Index_Lt')
        condition_positive_tendon_Index = cmds.createNode( 'condition', n='condition_positive_tendon_Index_Lt')

        cmds.setAttr(multiply_divide_value_tendon_Index + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Index + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Index + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Index + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Index + '.operation', 2)

        cmds.connectAttr( f'{joint_Index_2_Lt}.rotateZ', f'{condition_positive_tendon_Index}.firstTerm' )
        cmds.connectAttr( f'{joint_Index_2_Lt}.rotateZ', f'{multiply_divide_value_tendon_Index}.input1X' )
        cmds.connectAttr( f'{joint_Index_2_Lt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Index}.outColorR', f'{multiply_divide_value_tendon_Index}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Index}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Index}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputY', f'{joint_Index_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_1_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_1_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_2_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_2_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_3_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_3_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_4_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_4_Lt}.translateZ' )

        
    
        cmds.connectAttr( f'{controler_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2Y' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2X' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2Z' )

        cmds.select(deselect=True)
        ctrls_Index_to_goup = [ctrl_Ik_Finger_Index_OFF[0], curve_pole_Vector_Index_OFF[0], ctrl_finger_1_Index_OFF[0]]
        group_ctrls_Index_Lt = cmds.group(em=True, name='Grp_Ctrls_Index_Lt')
        cmds.parent(ctrls_Index_to_goup, group_ctrls_Index_Lt)

        
        joint_Index_to_goup = [joint_Index_1_Lt, joint_DRV_Index_1_Lt ]
        group_joints_Index_Lt = cmds.group(em=True, name='Grp_Sk_Index_Lt')
        cmds.parent(joint_Index_to_goup, group_joints_Index_Lt)







        #guide visual pv 
        locator_pv_start_Index_ctrl_Lt = cmds.spaceLocator(n='LOC_Start_Guide_PV_Index_Lt', p=(0, 0, 0), )
        cmds.matchTransform(locator_pv_start_Index_ctrl_Lt, joint_Index_3_Lt)
        cmds.setAttr(locator_pv_start_Index_ctrl_Lt[0] + '.visibility', 0 )
        locator_pv_end_Index_ctrl_Lt = cmds.spaceLocator( n='LOC_End_Guide_PV_Index_Lt', p=(0, 0, 0)  )
        cmds.matchTransform(locator_pv_end_Index_ctrl_Lt, curve_pole_Vector_Index)
        cmds.setAttr(locator_pv_end_Index_ctrl_Lt[0] + '.visibility', 0 )

        locator_pv_start_Index_ctrl_Lt_position = cmds.xform(locator_pv_start_Index_ctrl_Lt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Index_ctrl_Lt_position = cmds.xform(locator_pv_end_Index_ctrl_Lt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Index_ctrl_Lt = cmds.curve(d=1, p=[locator_pv_start_Index_ctrl_Lt_position, locator_pv_end_Index_ctrl_Lt_position], n='Guide_PV_Index_Lt')

        decompose_M_curve_start_Index_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Index_Lt')
        decompose_M_curve_end_Index_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Index_Lt')

        
        #pas besoin
        # listShapes = cmds.listRelatives(curve_pv_Index_ctrl_Lt, allDescendents=True, type='shape')
        # curve_pv_Index_ctrl_Lt_shape = listShapes[0]
        # print(curve_pv_Index_ctrl_Lt_shape)
           
        cmds.connectAttr( f'{locator_pv_start_Index_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_start_Index_Lt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Index_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_end_Index_Lt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Index_Lt}.outputTranslate', f'{curve_pv_Index_ctrl_Lt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Index_Lt}.outputTranslate', f'{curve_pv_Index_ctrl_Lt}.controlPoints[1]' )

        cmds.parent(locator_pv_end_Index_ctrl_Lt, curve_pole_Vector_Index)
        cmds.parent(locator_pv_start_Index_ctrl_Lt, joint_Index_3_Lt)

        cmds.setAttr(curve_pv_Index_ctrl_Lt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Guide_Visibility', f'{curve_pv_Index_ctrl_Lt}.visibility' )


        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Index_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Index_Lt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Index_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Index_Lt', p=(0, 0, 0), )
        print(locator_Finger_FingerSpace_PV_Index_ctrl_Lt)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Index_ctrl_Lt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Index_ctrl_Lt[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Index_ctrl_Lt, curve_pole_Vector_Index)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Index_ctrl_Lt, curve_pole_Vector_Index)

        hold_matrix_Index_PV_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Index_Lt')
        mult_Finger_FingerSpace_PV_Index_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Index_Lt')
        mult_Finger_HandSpace_PV_Index_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Index_Lt')
        condition_Finger_Space_PV_Index_Lt = cmds.createNode( 'condition', n='Cond_Space_Index_PV_Lt')
        condition_Finger_FingerSpace_PV_Index_Lt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Index_Lt')
        condition_Finger_HandSpace_PV_Index_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Index_Lt')

        blend_matrix_PV_Index_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Index_Lt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_PV_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_PV_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Index_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Index_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Index_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Index_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Index_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_PV_Index_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Index_Lt}.matrixSum', f'{blend_matrix_PV_Index_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Index_Lt}.matrixSum', f'{blend_matrix_PV_Index_Lt}.target[0].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_FingerSpace_PV_Index_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_HandSpace_PV_Index_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_Space_PV_Index_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Index_Lt}.outColorR', f'{condition_Finger_Space_PV_Index_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Index_Lt}.outColorR', f'{condition_Finger_Space_PV_Index_Lt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Index_Lt}.outColorR', f'{blend_matrix_PV_Index_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Index_Lt}.outColorG', f'{blend_matrix_PV_Index_Lt}.target[1].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Index_Lt}.outputMatrix', f'{curve_pole_Vector_Index}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Index_ctrl_Lt, ctrl_Ik_Finger_Index) #et on parente direct le locator de l'ik 
        

        
        #Space controller IK a 4 choix

        locator_Finger_HandSpace_IK_Index_ctrl = cmds.spaceLocator(n='LOC_Finger_HandSpace_IK_Index_Lt', p=(0, 0, 0), )
        locator_Finger_HeadSpace_IK_Index_ctrl = cmds.spaceLocator(n='LOC_Finger_HeadSpace_IK_Index_Lt', p=(0, 0, 0), )
        locator_Finger_HipSpace_IK_Index_ctrl = cmds.spaceLocator(n='LOC_Finger_HipSpace_IK_Index_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_HandSpace_IK_Index_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HeadSpace_IK_Index_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HipSpace_IK_Index_ctrl[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_HandSpace_IK_Index_ctrl,ctrl_Ik_Finger_Index)
        cmds.matchTransform(locator_Finger_HeadSpace_IK_Index_ctrl,ctrl_Ik_Finger_Index)
        cmds.matchTransform(locator_Finger_HipSpace_IK_Index_ctrl,ctrl_Ik_Finger_Index)

        hold_matrix_Index_IK_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Index_Lt')
        mult_Finger_HandSpace_IK_Index_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Index_Lt')
        mult_Finger_HeadSpace_IK_Index_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Index_Lt')
        mult_Finger_HipSpace_IK_Index_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Index_Lt')
        condition_Finger_Space_IK_Index_Lt = cmds.createNode( 'condition', n='Cond_Space_Index_Lt')
        condition_Finger_HandSpace_IK_Index_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_Index_Lt')
        condition_Finger_HeadSpace_IK_Index_Lt = cmds.createNode( 'condition', n='Cond_HeadSpace_Index_Lt')
        condition_Finger_HipSpace_IK_Index_Lt = cmds.createNode( 'condition', n='Cond_HipSpace_Index_Lt')

        blend_matrix_IK_Index_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Index_Lt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Lt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_IK_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_IK_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Index_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Index_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Index_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Index_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Index_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_IK_Index_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Index_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HipSpace_IK_Index_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Index_Lt}.matrixSum', f'{blend_matrix_IK_Index_Lt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Index_Lt}.matrixSum', f'{blend_matrix_IK_Index_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Index_Lt}.matrixSum', f'{blend_matrix_IK_Index_Lt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HandSpace_IK_Index_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HeadSpace_IK_Index_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HipSpace_IK_Index_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_Space_IK_Index_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Index_Lt}.outColorR', f'{condition_Finger_Space_IK_Index_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Index_Lt}.outColorR', f'{condition_Finger_Space_IK_Index_Lt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Index_Lt}.outColorR', f'{condition_Finger_Space_IK_Index_Lt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Lt}.outColorR', f'{blend_matrix_IK_Index_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Lt}.outColorG', f'{blend_matrix_IK_Index_Lt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Lt}.outColorB', f'{blend_matrix_IK_Index_Lt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Index_Lt}.outputMatrix', f'{ctrl_Ik_Finger_Index}.offsetParentMatrix' )

        
            #on range les locator space dans les bon endroit

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Lt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Index_ctrl[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Index_ctrl[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Index_ctrl[0], sk_Hand)
        
        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_PV_Index_ctrl_Lt[0], sk_Hand)
            
        else :
            group_miror_Index_Loc_Space_IK_temp_Lt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Index_A_PARENTER_Lt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Index_ctrl[0], locator_Finger_HeadSpace_IK_Index_ctrl[0], locator_Finger_HipSpace_IK_Index_ctrl[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Index_Loc_Space_IK_temp_Lt)
            cmds.select(deselect=True)





        #set skinning
        cmds.select(deselect=True)
        list_set_skin_jnt = [joint_Index_1_Lt, joint_Index_2_Lt, joint_Index_3_Lt, joint_Index_4_Lt, joint_Index_Tendon_1_Lt, joint_Index_Tendon_2_Lt, joint_Index_Tendon_3_Lt, joint_Index_Tendon_4_Lt, joint_Index_knuckle]
        set_name = "MySetJointSkin"
        if cmds.objExists(set_name):
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)
        
        else:
            cmds.sets(n=set_name)
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)




        #rangement dans les groupes


        grp_Controllers = 'Grp_Controllers'
        grp_Skeleton = 'Grp_Skeleton'
        grp_DO_NOT_TOUCH = 'DO_NOT_TOUCH'
        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'



        if not cmds.objExists('Grp_DNT_Hand_Lt'):
            grp_DNT_Hand_Lt = cmds.group(em=True, name='Grp_DNT_Hand_Lt')



        grp_elem_DNT_Index = [curve_pv_Index_ctrl_Lt]

        cmds.parent(grp_elem_DNT_Index, grp_DNT_Hand_Lt )


        if cmds.objExists(grp_Controllers):
            cmds.parent(group_ctrls_Index_Lt, grp_Controllers)
        else:
            grp_Controllers = cmds.group(em=True, name='Grp_Controllers')
            cmds.parent(group_ctrls_Index_Lt, grp_Controllers)


        if cmds.objExists(grp_Skeleton):
            cmds.parent(group_joints_Index_Lt, grp_Skeleton)
        else:
            grp_Skeleton = cmds.group(em=True, name='Grp_Skeleton')
            cmds.parent(group_joints_Index_Lt, grp_Skeleton)


        if cmds.objExists(grp_DO_NOT_TOUCH):
            if cmds.objExists('Grp_DNT_Hand_Lt'):
                parent_of_grp_DNT_Hand_Lt = cmds.listRelatives(grp_DNT_Hand_Lt, parent=True)
                if not parent_of_grp_DNT_Hand_Lt:
                    cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)
        else:
            grp_DO_NOT_TOUCH = cmds.group(em=True, name='DO_NOT_TOUCH')
            cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)



        # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{controler_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Index}.visibility' )     



        #on fait la parentée pour que les mains suivent la structure generale

        DRV_Palm_IK_Lt = "DRV_Palm_IK_Lt"
        if cmds.objExists(DRV_Palm_IK_Lt):
            cmds.parentConstraint(DRV_Palm_IK_Lt, joint_DRV_Index_1_Lt, mo=True)
        ###

        #couleurs des controllers 
        jnt_color_Blue = [ctrl_finger_1_Index, ctrl_finger_2_Index, ctrl_finger_3_Index, ctrl_finger_4_Index, ctrl_Ik_Finger_Index]
        jnt_color_DarkBlue = [ctrl_finger_3_Index, ctrl_finger_4_Index]
        jnt_color_beige= [curve_pole_Vector_Index]
        

        for objcolor_Blue in jnt_color_Blue : 
            cmds.setAttr(objcolor_Blue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Blue + '.overrideColor', 6)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 5)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def index_rig_Part_3_Miror(*args):

        duplication_group_ctrls_sk = cmds.duplicate(group_ctrls_Index_Lt,group_joints_Index_Lt, rc=True)
        

        for Delnode in duplication_group_ctrls_sk: 
            string_del = ['EFF', 'Constraint', 'IKRP_Index_Lt', 'LOC_Finger_FingerSpace_PV_Index_Lt1']
            for substring in string_del:
                if Delnode.find(substring) != -1 and cmds.objExists(Delnode):
                    cmds.delete(Delnode)


             
        
        for rename in duplication_group_ctrls_sk:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        group_ctrls_Index_Rt = 'Grp_Ctrls_Index_Rt'
        group_joints_Index_Rt = 'Grp_Sk_Index_Rt'
        # group_miror_Index_Loc_Space_IK_temp_Rt = 'Grp_LOC_Space_Ik_Finger_Index_A_PARENTER_Rt'
        
    
        cmds.setAttr(group_ctrls_Index_Rt + '.scaleX', -1 )
        cmds.setAttr(group_joints_Index_Rt + '.scaleX', -1 )
        # cmds.setAttr(group_miror_Index_Loc_Space_IK_temp_Rt + '.scaleX', -1 )


        #réassignation des varables pour le miror
        ctrl_finger_1_Index = 'Ctrl_Finger_1_Index_Rt'
        ctrl_finger_2_Index = 'Ctrl_Finger_2_Index_Rt'
        ctrl_finger_3_Index = 'Ctrl_Finger_3_Index_Rt'
        ctrl_finger_4_Index = 'Ctrl_Finger_4_Index_Rt'
        curve_pole_Vector_Index = 'Crv_PV_Index_Rt'
        ctrl_Ik_Finger_Index = 'Ctrl_IK_Index_Rt'

        joint_DRV_Index_1_Rt = 'DRV_Index_1_Rt'
        joint_DRV_Index_2_Rt = 'DRV_Index_2_Rt'
        joint_DRV_Index_3_Rt = 'DRV_Index_3_Rt'
        joint_DRV_Index_4_Rt = 'DRV_Index_4_Rt'
        joint_DRV_Index_T_Rt = 'DRV_Index_T_Rt'
        joint_Index_1_Rt = 'Sk_Index_1_Rt'
        joint_Index_2_Rt = 'Sk_Index_2_Rt'
        joint_Index_3_Rt = 'Sk_Index_3_Rt'
        joint_Index_4_Rt = 'Sk_Index_4_Rt'
        joint_Index_T_Rt = 'Sk_Index_T_Rt'
        joint_Index_Tendon_1_Rt = 'Sk_Index_Tendon_1_Rt'
        joint_Index_Tendon_2_Rt = 'Sk_Index_Tendon_2_Rt'
        joint_Index_Tendon_3_Rt = 'Sk_Index_Tendon_3_Rt'
        joint_Index_Tendon_4_Rt = 'Sk_Index_Tendon_4_Rt'
        joint_Index_knuckle = 'Sk_Index_Knuckle_Rt'

        duplication_ctrl_hand_control = 'Ctrl_Control_Hand_Rt'
        locator_pv_start_Index_ctrl_Rt = 'LOC_Start_Guide_PV_Index_Rt'
        locator_pv_end_Index_ctrl_Rt = 'LOC_End_Guide_PV_Index_Rt'





        '''
        duplication du code au dessus qui suit

        '''

        



        cmds.parentConstraint( ctrl_finger_1_Index, joint_Index_1_Rt )
        cmds.parentConstraint( ctrl_finger_2_Index, joint_Index_2_Rt )
        cmds.parentConstraint( ctrl_finger_3_Index, joint_Index_3_Rt )
        cmds.parentConstraint( ctrl_finger_4_Index, joint_Index_4_Rt )
        


        cmds.setAttr(joint_DRV_Index_3_Rt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Index_4_Rt + '.preferredAngleZ', -10.0)

        ik_Handle_Index_Rt = cmds.ikHandle(n='IKRP_Index_Rt',  sj=joint_DRV_Index_2_Rt, ee=joint_DRV_Index_T_Rt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Index_Rt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Index_Rt[0], ctrl_Ik_Finger_Index)
        cmds.poleVectorConstraint( curve_pole_Vector_Index, ik_Handle_Index_Rt[0] )


        new_Effector_name_Index = 'EFF_IKRP_Index_Rt'
        List_Input_Ik_Handle_Index = cmds.listConnections('IKRP_Index_Rt',s=True)
        for node in List_Input_Ik_Handle_Index:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Index)
                break
        

        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Index_OFF = cmds.listRelatives(ctrl_finger_1_Index, parent=True, fullPath=True)
        ctrl_finger_2_Index_OFF = cmds.listRelatives(ctrl_finger_2_Index, parent=True, fullPath=True)
        ctrl_finger_3_Index_OFF = cmds.listRelatives(ctrl_finger_3_Index, parent=True, fullPath=True)
        ctrl_finger_4_Index_OFF = cmds.listRelatives(ctrl_finger_4_Index, parent=True, fullPath=True)
        curve_pole_Vector_Index_OFF = cmds.listRelatives(curve_pole_Vector_Index, parent=True, fullPath=True)
        ctrl_Ik_Finger_Index_OFF = cmds.listRelatives(ctrl_Ik_Finger_Index, parent=True, fullPath=True)
        
        decompose_M_DRV_Index_1_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_1_Rt')
        decompose_M_DRV_Index_2_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_2_Rt')
        decompose_M_DRV_Index_3_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_3_Rt')
        decompose_M_DRV_Index_4_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Index_4_Rt')

        cmds.connectAttr( f'{joint_DRV_Index_1_Rt}.xformMatrix', f'{decompose_M_DRV_Index_1_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_2_Rt}.xformMatrix', f'{decompose_M_DRV_Index_2_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_3_Rt}.xformMatrix', f'{decompose_M_DRV_Index_3_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Index_4_Rt}.xformMatrix', f'{decompose_M_DRV_Index_4_Rt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Index_1_Rt}.outputTranslate', f'{ctrl_finger_1_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_2_Rt}.outputTranslate', f'{ctrl_finger_2_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_3_Rt}.outputTranslate', f'{ctrl_finger_3_Index_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_4_Rt}.outputTranslate', f'{ctrl_finger_4_Index_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Index_1_Rt}.outputRotate', f'{ctrl_finger_1_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_2_Rt}.outputRotate', f'{ctrl_finger_2_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_3_Rt}.outputRotate', f'{ctrl_finger_3_Index_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Index_4_Rt}.outputRotate', f'{ctrl_finger_4_Index_OFF[0]}.rotate' )


        

        multiply_divide_value_tendon_Index = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Index_Rt')
        multiply_divide_lower_intensity_knuckle_tendon_Index = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Index_Rt')
        multiply_divide_intensity_knuckle_tendon_Index = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Index_Rt')
        condition_positive_tendon_Index = cmds.createNode( 'condition', n='condition_positive_tendon_Index_Rt')

        cmds.setAttr(multiply_divide_value_tendon_Index + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Index + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Index + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Index + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Index + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Index + '.operation', 2)

        cmds.connectAttr( f'{joint_Index_2_Rt}.rotateZ', f'{condition_positive_tendon_Index}.firstTerm' )
        cmds.connectAttr( f'{joint_Index_2_Rt}.rotateZ', f'{multiply_divide_value_tendon_Index}.input1X' )
        cmds.connectAttr( f'{joint_Index_2_Rt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Index}.outColorR', f'{multiply_divide_value_tendon_Index}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Index}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Index}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Index}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Index}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputY', f'{joint_Index_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_1_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_1_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_2_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_2_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_3_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_3_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputX', f'{joint_Index_Tendon_4_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Index}.outputZ', f'{joint_Index_Tendon_4_Rt}.translateZ' )

        
    
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2Y' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2X' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Index}.input2Z' )

        cmds.select(deselect=True)

        

        #miror
        locator_pv_start_Index_ctrl_Rt_position = cmds.xform(locator_pv_start_Index_ctrl_Rt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Index_ctrl_Rt_position = cmds.xform(locator_pv_end_Index_ctrl_Rt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Index_ctrl_Rt = cmds.curve(d=1, p=[locator_pv_start_Index_ctrl_Rt_position, locator_pv_end_Index_ctrl_Rt_position], n='Guide_PV_Index_Rt')

        decompose_M_curve_start_Index_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Index_Rt')
        decompose_M_curve_end_Index_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Index_Rt')


           
        cmds.connectAttr( f'{locator_pv_start_Index_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_start_Index_Rt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Index_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_end_Index_Rt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Index_Rt}.outputTranslate', f'{curve_pv_Index_ctrl_Rt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Index_Rt}.outputTranslate', f'{curve_pv_Index_ctrl_Rt}.controlPoints[1]' )

        

        cmds.setAttr(curve_pv_Index_ctrl_Rt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Guide_Visibility', f'{curve_pv_Index_ctrl_Rt}.visibility' )







        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Index_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Index_Rt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Index_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Index_Rt', p=(0, 0, 0))
        cmds.parent(locator_Finger_FingerSpace_PV_Index_ctrl_Rt, curve_pole_Vector_Index )
        cmds.parent(locator_Finger_HandSpace_PV_Index_ctrl_Rt, curve_pole_Vector_Index )
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Index_ctrl_Rt, curve_pole_Vector_Index)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Index_ctrl_Rt, curve_pole_Vector_Index)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Index_ctrl_Rt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Index_ctrl_Rt[0] + '.visibility', 0)
        

        hold_matrix_Index_PV_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Index_Rt')
        mult_Finger_FingerSpace_PV_Index_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Index_Rt')
        mult_Finger_HandSpace_PV_Index_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Index_Rt')
        condition_Finger_Space_PV_Index_Rt = cmds.createNode( 'condition', n='Cond_Space_Index_PV_Rt')
        condition_Finger_FingerSpace_PV_Index_Rt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Index_Rt')
        condition_Finger_HandSpace_PV_Index_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Index_Rt')

        blend_matrix_PV_Index_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Index_Rt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Index_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Index_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_PV_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Index_PV_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Index_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Index_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Index_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Index_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Index_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Index_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_PV_Index_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Index_Rt}.matrixSum', f'{blend_matrix_PV_Index_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Index_Rt}.matrixSum', f'{blend_matrix_PV_Index_Rt}.target[1].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_FingerSpace_PV_Index_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_HandSpace_PV_Index_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Index}.Space', f'{condition_Finger_Space_PV_Index_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Index_Rt}.outColorR', f'{condition_Finger_Space_PV_Index_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Index_Rt}.outColorR', f'{condition_Finger_Space_PV_Index_Rt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Index_Rt}.outColorR', f'{blend_matrix_PV_Index_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Index_Rt}.outColorG', f'{blend_matrix_PV_Index_Rt}.target[0].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Index_Rt}.outputMatrix', f'{curve_pole_Vector_Index}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Index_ctrl_Rt, ctrl_Ik_Finger_Index) #et on parente direct le locator de l'ik 
        


        # le coté rt ne marche pas avec ça donc il faut venir faire une duplication des anciens locators
            #on vient recuperer les anciens locators
        list_locator_IndexSpace_dup = [locator_Finger_HipSpace_IK_Index_ctrl  , locator_Finger_HeadSpace_IK_Index_ctrl ,   locator_Finger_HandSpace_IK_Index_ctrl ]

            #on cree une nouvelle liste qui va aceuillir nos nouveaux locators
        new_list_locator_IndexSpace_dup = []
        for elem in list_locator_IndexSpace_dup:
            duplication_group_loc_space = cmds.duplicate(elem,  rc=True)
            new_list_locator_IndexSpace_dup.append(duplication_group_loc_space)

            #on cree le grp temporaire qui va scale -1
        group_miror_locators_IndexSpace = cmds.group(empty=True, n='Grp_Temp_miror_Loc_Index_Rt')

            

            #on parente les nouveaux elements de la nouvelle liste au grp  et ensuite on scale le groupe pour miror
        for elem in new_list_locator_IndexSpace_dup :
            cmds.parent(elem, group_miror_locators_IndexSpace)

        cmds.setAttr(group_miror_locators_IndexSpace + ".scaleX", -1)

            #on vient faire une list relative pour identifier les enfants et pas que ça poe de probleme pour le rename 
        group_miror_locators_IndexSpace_children = cmds.listRelatives(group_miror_locators_IndexSpace, c=True)

            #on vient les renommer en rt
        for rename in group_miror_locators_IndexSpace_children:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        locator_Finger_HandSpace_IK_Index_ctrl_Rt = 'LOC_Finger_HandSpace_IK_Index_Rt'
        locator_Finger_HeadSpace_IK_Index_ctrl_Rt = 'LOC_Finger_HeadSpace_IK_Index_Rt'
        locator_Finger_HipSpace_IK_Index_ctrl_Rt = 'LOC_Finger_HipSpace_IK_Index_Rt'


        cmds.select(locator_Finger_HandSpace_IK_Index_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HeadSpace_IK_Index_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HipSpace_IK_Index_ctrl_Rt)                
        OFF()
        

        

        locator_Finger_HandSpace_IK_Index_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HandSpace_IK_Index_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HeadSpace_IK_Index_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HeadSpace_IK_Index_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HipSpace_IK_Index_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HipSpace_IK_Index_ctrl_Rt, parent=True, fullPath=True)
        


        hold_matrix_Index_IK_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Index_Rt')
        mult_Finger_HandSpace_IK_Index_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Index_Rt')
        mult_Finger_HeadSpace_IK_Index_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Index_Rt')
        mult_Finger_HipSpace_IK_Index_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Index_Rt')
        condition_Finger_Space_IK_Index_Rt = cmds.createNode( 'condition', n='Cond_Space_Index_Rt')
        condition_Finger_HandSpace_IK_Index_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_Index_Rt')
        condition_Finger_HeadSpace_IK_Index_Rt = cmds.createNode( 'condition', n='Cond_HeadSpace_Index_Rt')
        condition_Finger_HipSpace_IK_Index_Rt = cmds.createNode( 'condition', n='Cond_HipSpace_Index_Rt')

        blend_matrix_IK_Index_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Index_Rt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Rt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Index_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Index_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Index_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Index_IK_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Index_IK_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Index_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Index_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Index_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Index_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Index_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Index_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_IK_Index_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Index_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Index_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HipSpace_IK_Index_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Index_Rt}.matrixSum', f'{blend_matrix_IK_Index_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Index_Rt}.matrixSum', f'{blend_matrix_IK_Index_Rt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Index_Rt}.matrixSum', f'{blend_matrix_IK_Index_Rt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HandSpace_IK_Index_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HeadSpace_IK_Index_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_HipSpace_IK_Index_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Index}.Space', f'{condition_Finger_Space_IK_Index_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Index_Rt}.outColorR', f'{condition_Finger_Space_IK_Index_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Index_Rt}.outColorR', f'{condition_Finger_Space_IK_Index_Rt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Index_Rt}.outColorR', f'{condition_Finger_Space_IK_Index_Rt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Rt}.outColorR', f'{blend_matrix_IK_Index_Rt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Rt}.outColorG', f'{blend_matrix_IK_Index_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Index_Rt}.outColorB', f'{blend_matrix_IK_Index_Rt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Index_Rt}.outputMatrix', f'{ctrl_Ik_Finger_Index}.offsetParentMatrix' )  


            #on parente les locators

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Rt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Index_ctrl_Rt_OFF[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Index_ctrl_Rt_OFF[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Index_ctrl_Rt_OFF[0], sk_Hand)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_PV_Index_ctrl_Rt[0], sk_Hand)
            
        else :
            group_miror_Index_Loc_Space_IK_temp_Rt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Index_A_PARENTER_Rt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Index_ctrl_Rt_OFF[0], locator_Finger_HeadSpace_IK_Index_ctrl_Rt_OFF[0], locator_Finger_HipSpace_IK_Index_ctrl_Rt_OFF[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Index_Loc_Space_IK_temp_Rt)
            cmds.select(deselect=True)

        #apres ça on supprime le grp scale -1 des locators 
        cmds.delete(group_miror_locators_IndexSpace)


        #parenter les crv guides 

        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'
        cmds.parent(curve_pv_Index_ctrl_Rt, grp_DNT_Hand_Lt)


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Index}.visibility' )   

        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Rt = "DRV_Palm_IK_Rt"
        if cmds.objExists(DRV_Palm_IK_Rt):
            cmds.parentConstraint(DRV_Palm_IK_Rt, joint_DRV_Index_1_Rt, mo=True)  

        
        #couleurs des controllers 
        jnt_color_Red = [ctrl_finger_1_Index, ctrl_finger_2_Index, ctrl_finger_3_Index, ctrl_finger_4_Index, ctrl_Ik_Finger_Index]
        jnt_color_DarkBlue = [ctrl_finger_3_Index, ctrl_finger_4_Index]
        jnt_color_beige= [curve_pole_Vector_Index]
        

        for objcolor_Red in jnt_color_Red : 
            cmds.setAttr(objcolor_Red + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Red + '.overrideColor', 13)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 18)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def index_rig_Suppr(*args): 
        
        index_finger_to_suppr = ['Grp_Ctrls_Index_Lt', 'Grp_Sk_Index_Lt','Guide_PV_Index_Lt', 'Grp_LOC_Space_Ik_Finger_Index_A_PARENTER_Lt', 'Grp_Ctrls_Index_Rt', 'Grp_Sk_Index_Rt','Guide_PV_Index_Rt', 'Grp_LOC_Space_Ik_Finger_Index_A_PARENTER_Rt']
        identify_index_finger_to_suppr = cmds.listRelatives(index_finger_to_suppr, ad=True)
        list_suppr = [index_finger_to_suppr]

        for i in range(100):
            list_suppr.append(identify_index_finger_to_suppr)
            identify_index_finger_to_suppr = cmds.listConnections(identify_index_finger_to_suppr, d=True, s=True)
            
            if not identify_index_finger_to_suppr:
                break

        list_suppr_2 = []
        list_Not_Suppr_Index = ['defaultRenderUtilityList', 'MayaNodeEditorSavedTabsInfo', 'Ctrl_Control_Hand', 'Middle', 'Ring', 'Pinky', 'Thumb','bindPose','ikRPsolver','ikSCsolver','hikSolver', 'ikSplineSolver','ikSystem','MySetJointSkin']

        for elem in list_suppr:
            for node in elem:
                skip_node = False

                for index_name in list_Not_Suppr_Index:
                    if index_name in node:
                        skip_node = True
                        break

                if not skip_node:
                    list_suppr_2.append(node)

        cmds.delete(list_suppr_2)           
###
    
    def middle_rig_Part_1(*args):
        
        global joint_DRV_Middle_1_Lt
        global joint_DRV_Middle_2_Lt
        global joint_DRV_Middle_3_Lt
        global joint_DRV_Middle_4_Lt
        global joint_DRV_Middle_T_Lt
        global curve_MP_Middle_Lt
        global joint_DRV_Middle_3_OFF_Lt
        global joint_DRV_Middle_4_OFF_Lt
        
        global joint_Middle_Tendon_1_Lt
        global joint_Middle_Tendon_2_Lt
        global joint_Middle_Tendon_3_Lt
        global joint_Middle_Tendon_4_Lt
        global curve_MP_Middle_Tendon_Lt
        global joint_Middle_Tendon_OFF_1_Lt
        global joint_Middle_Tendon_OFF_2_Lt
        global joint_Middle_Tendon_OFF_3_Lt
        global joint_Middle_Tendon_OFF_4_Lt
        global loc_Middle_orientaton_joints_Lt
        global loc_Middle_orientaton_joints_Lt_grp
        
        


        cmds.select(deselect=True)
        joint_DRV_Middle_1_Lt = cmds.joint(n='DRV_Middle_1_Lt', p=(55, 105, -6))
        joint_DRV_Middle_2_Lt = cmds.joint(n='DRV_Middle_2_Lt', p=(61, 100, -6.5))
        joint_DRV_Middle_3_Lt = cmds.joint(n='DRV_Middle_3_Lt', p=(5, 0, 5))
        joint_DRV_Middle_4_Lt = cmds.joint(n='DRV_Middle_4_Lt', p=(10, 0, 5))
        joint_DRV_Middle_T_Lt = cmds.joint(n='DRV_Middle_T_Lt', p=(69, 92, -6.5), rad=0.5)

        cmds.parent(joint_DRV_Middle_T_Lt, world=True)
        cmds.parent(joint_DRV_Middle_4_Lt, world=True)
        cmds.parent(joint_DRV_Middle_3_Lt, world=True)
        cmds.parent(joint_DRV_Middle_2_Lt, world=True)
        
       
        
        joint_Middle_Tendon_1_Lt = cmds.joint(n='Sk_Middle_Tendon_1_Lt', p=(-8, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Middle_Tendon_2_Lt = cmds.joint(n='Sk_Middle_Tendon_2_Lt', p=(-6, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Middle_Tendon_3_Lt = cmds.joint(n='Sk_Middle_Tendon_3_Lt', p=(-4, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Middle_Tendon_4_Lt = cmds.joint(n='Sk_Middle_Tendon_4_Lt', p=(-2, 0, 5), rad=0.2)


        jnt_finger_Middle = [joint_DRV_Middle_3_Lt,joint_DRV_Middle_4_Lt,joint_Middle_Tendon_1_Lt,joint_Middle_Tendon_2_Lt,joint_Middle_Tendon_3_Lt,joint_Middle_Tendon_4_Lt]
        for offset in jnt_finger_Middle :
            cmds.select(offset)
            OFF()


        joint_DRV_Middle_3_OFF_Lt = cmds.listRelatives(joint_DRV_Middle_3_Lt, parent=True, fullPath=True)        
        joint_DRV_Middle_4_OFF_Lt = cmds.listRelatives(joint_DRV_Middle_4_Lt, parent=True, fullPath=True)

        joint_Middle_Tendon_OFF_1_Lt = cmds.listRelatives(joint_Middle_Tendon_1_Lt, parent=True, fullPath=True)
        joint_Middle_Tendon_OFF_2_Lt = cmds.listRelatives(joint_Middle_Tendon_2_Lt, parent=True, fullPath=True)
        joint_Middle_Tendon_OFF_3_Lt = cmds.listRelatives(joint_Middle_Tendon_3_Lt, parent=True, fullPath=True)
        joint_Middle_Tendon_OFF_4_Lt = cmds.listRelatives(joint_Middle_Tendon_4_Lt, parent=True, fullPath=True)



        jnt_0_Crv_Position_Middle = cmds.xform(joint_DRV_Middle_1_Lt, query=True, worldSpace=True, translation=True)
        jnt_1_Crv_Position_Middle = cmds.xform(joint_DRV_Middle_2_Lt, query=True, worldSpace=True, translation=True)
        jnt_2_Crv_Position_Middle = cmds.xform(joint_DRV_Middle_T_Lt, query=True, worldSpace=True, translation=True)
        joint_Skin_Crv_Middle_1_Lt = [joint_DRV_Middle_2_Lt , joint_DRV_Middle_T_Lt]
        joint_Skin_Crv_Middle_2_Lt = [joint_DRV_Middle_1_Lt ,joint_DRV_Middle_2_Lt]

        curve_MP_Middle_Lt = cmds.curve(d=1, p=[jnt_1_Crv_Position_Middle, jnt_2_Crv_Position_Middle], n='Crv_MP_Middle_Lt_Temp')
        curve_MP_Middle_Tendon_Lt = cmds.curve(d=1, p=[jnt_0_Crv_Position_Middle, jnt_1_Crv_Position_Middle], n='Crv_MP_Middle_Tendon_Lt_Temp')

        bind_skin_cluster_Middle = cmds.skinCluster(joint_Skin_Crv_Middle_1_Lt, curve_MP_Middle_Lt, tsb=True)
        bind_skin_cluster_tendon_Middle = cmds.skinCluster(joint_Skin_Crv_Middle_2_Lt, curve_MP_Middle_Tendon_Lt, tsb=True)



        cmds.pathAnimation( joint_DRV_Middle_3_OFF_Lt, c=curve_MP_Middle_Lt, su=0.3333, follow=True)
        cmds.pathAnimation( joint_DRV_Middle_4_OFF_Lt, c=curve_MP_Middle_Lt, su=0.6666, follow=True)

        cmds.pathAnimation( joint_Middle_Tendon_OFF_1_Lt, c=curve_MP_Middle_Tendon_Lt, su=0.2, follow=True)
        cmds.pathAnimation( joint_Middle_Tendon_OFF_2_Lt, c=curve_MP_Middle_Tendon_Lt, su=0.4, follow=True)
        cmds.pathAnimation( joint_Middle_Tendon_OFF_3_Lt, c=curve_MP_Middle_Tendon_Lt, su=0.6, follow=True)
        cmds.pathAnimation( joint_Middle_Tendon_OFF_4_Lt, c=curve_MP_Middle_Tendon_Lt, su=0.8, follow=True)
        

        attributes_to_lock_Middle = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Middle:
            cmds.setAttr(joint_DRV_Middle_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_DRV_Middle_4_Lt + "." + attr, lock=True)

        attributes_to_lock_tendon_Middle = ["rotateX","rotateY","rotateZ","translateX","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_tendon_Middle:
            cmds.setAttr(joint_Middle_Tendon_1_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Middle_Tendon_2_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Middle_Tendon_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Middle_Tendon_4_Lt + "." + attr, lock=True)

        

        cmds.select(deselect=True)
        list_grp_placement_jnt = [joint_DRV_Middle_1_Lt, joint_DRV_Middle_2_Lt, joint_DRV_Middle_T_Lt]
        grp_name = "Grp_Deplacement_Groupe_Main_Temp"
        if cmds.objExists(grp_name):
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)
        
        else:
            cmds.group(em=True, n=grp_name)
            
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)




        # cmds.setAttr(joint_DRV_Middle_1_Lt + ".translatex" + attr, lock=True)

        #loc orientation du doigt
        loc_Middle_orientaton_joints_Lt = cmds.spaceLocator(n='LOC_Guide_Orient_Middle_Lt_TEMP', p=(0, 0, 0), )
        
        
        cmds.select(loc_Middle_orientaton_joints_Lt)
        loc_Middle_orientaton_joints_Lt_grp = cmds.group(loc_Middle_orientaton_joints_Lt[0], n= 'temp_loc_Middle')
        loc_Middle_orientaton_joints_Lt_grp = cmds.listRelatives(loc_Middle_orientaton_joints_Lt, parent=True, fullPath=True)
        cmds.pathAnimation( loc_Middle_orientaton_joints_Lt_grp, c=curve_MP_Middle_Lt, su=0.5, follow=True)
        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + '.rotateX', 90)
        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + '.rotateY', 0)
        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + '.rotateZ', 90)

        attributes_to_lock_LOC_Middle = ["rotateY","rotateZ","translateX","translateY","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_LOC_Middle:
            cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + "." + attr, lock=True)

        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + ".localScaleX" ,0.25)
        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + ".localScaleY" ,2.25)
        cmds.setAttr(loc_Middle_orientaton_joints_Lt[0] + ".localScaleZ" ,0.25)


        jnt_color_green = [joint_DRV_Middle_1_Lt,joint_DRV_Middle_2_Lt, joint_DRV_Middle_T_Lt, loc_Middle_orientaton_joints_Lt[0]]
        jnt_color_yellow= [joint_Middle_Tendon_1_Lt , joint_Middle_Tendon_2_Lt, joint_Middle_Tendon_3_Lt, joint_Middle_Tendon_4_Lt, joint_DRV_Middle_3_Lt, joint_DRV_Middle_4_Lt ]

        for objcolorgreen in jnt_color_green : 
            cmds.setAttr(objcolorgreen + '.overrideEnabled', 1)
            cmds.setAttr(objcolorgreen + '.overrideColor', 14)

        for objcoloryelllow in jnt_color_yellow : 
            cmds.setAttr(objcoloryelllow + '.overrideEnabled', 1)
            cmds.setAttr(objcoloryelllow + '.overrideColor', 17)
              
    def middle_rig_Part_2(*args):

        global group_ctrls_Middle_Lt
        global group_joints_Middle_Lt
        global new_Effector_name_Inde
        global group_miror_Middle_Loc_Space_IK_temp_Lt
        global locator_Finger_HipSpace_IK_Middle_ctrl
        global locator_Finger_HeadSpace_IK_Middle_ctrl
        global locator_Finger_HandSpace_IK_Middle_ctrl

        global locator_Finger_Space_PV_Middle_ctrl



        controler_hand_control = 'Ctrl_Control_Hand_Lt'
        
        cmds.delete(curve_MP_Middle_Lt, curve_MP_Middle_Tendon_Lt)

        attributes_to_lock_Middle = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Middle:
            cmds.setAttr(joint_DRV_Middle_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_DRV_Middle_4_Lt + "." + attr, lock=False)

        attributes_to_lock_tendon_Middle = ["translateX"]
        for attr in attributes_to_lock_tendon_Middle:
            cmds.setAttr(joint_Middle_Tendon_1_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Middle_Tendon_2_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Middle_Tendon_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Middle_Tendon_4_Lt + "." + attr, lock=False)





        ################################


        # orient le premier jnt 01 sans affecter les autres
        cmds.parent(joint_DRV_Middle_2_Lt, joint_DRV_Middle_1_Lt)
        cmds.joint(joint_DRV_Middle_1_Lt, edit=True, oj = 'xyz', sao='yup')
        cmds.parent(joint_DRV_Middle_2_Lt, world=True)
        cmds.matchTransform(joint_DRV_Middle_1_Lt,loc_Middle_orientaton_joints_Lt, rx=True, ry=False, rz=False)






        cmds.matchTransform(joint_DRV_Middle_2_Lt,loc_Middle_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Middle_3_Lt,loc_Middle_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Middle_4_Lt,loc_Middle_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Middle_T_Lt,loc_Middle_orientaton_joints_Lt, rot=True)
        
        
        cmds.parent(joint_DRV_Middle_T_Lt, joint_DRV_Middle_4_Lt)
        cmds.parent(joint_DRV_Middle_4_Lt, joint_DRV_Middle_3_Lt)
        cmds.parent(joint_DRV_Middle_3_Lt, joint_DRV_Middle_2_Lt)
        cmds.parent(joint_DRV_Middle_2_Lt, joint_DRV_Middle_1_Lt)
        cmds.delete (joint_DRV_Middle_3_OFF_Lt,joint_DRV_Middle_4_OFF_Lt)



        cmds.select(deselect=True)
        joint_Middle_1_Lt = cmds.joint(  n='Sk_Middle_1_Lt', rad=0.25 )
        cmds.matchTransform(joint_Middle_1_Lt,joint_DRV_Middle_1_Lt)
        cmds.select(deselect=True)
        joint_Middle_2_Lt = cmds.joint( n='Sk_Middle_2_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Middle_2_Lt,joint_DRV_Middle_2_Lt)
        joint_Middle_3_Lt = cmds.joint(  n='Sk_Middle_3_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Middle_3_Lt,joint_DRV_Middle_3_Lt)
        joint_Middle_4_Lt = cmds.joint(n='Sk_Middle_4_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Middle_4_Lt,joint_DRV_Middle_4_Lt)
        joint_Middle_T_Lt = cmds.joint(n='Sk_Middle_T_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Middle_T_Lt,joint_DRV_Middle_T_Lt)



        cmds.parent(joint_Middle_T_Lt, joint_Middle_4_Lt)
        cmds.parent(joint_Middle_4_Lt, joint_Middle_3_Lt)
        cmds.parent(joint_Middle_3_Lt, joint_Middle_2_Lt)
        cmds.parent(joint_Middle_2_Lt, joint_Middle_1_Lt)

        #freeze transform jnts avant d'orient
        cmds.select(deselect=True)
        cmds.select(joint_DRV_Middle_1_Lt,joint_DRV_Middle_2_Lt,joint_DRV_Middle_3_Lt,joint_DRV_Middle_4_Lt,joint_DRV_Middle_T_Lt,joint_Middle_1_Lt,joint_Middle_2_Lt,joint_Middle_3_Lt,joint_Middle_4_Lt,joint_Middle_T_Lt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        #delete le loc orientation 
        cmds.delete(loc_Middle_orientaton_joints_Lt_grp)

        position_joint_DRV_Middle_2_Lt = cmds.xform(joint_DRV_Middle_2_Lt, query=True, worldSpace=True, translation=True)

        cmds.parent(joint_Middle_Tendon_1_Lt, joint_Middle_1_Lt)
        cmds.parent(joint_Middle_Tendon_2_Lt, joint_Middle_1_Lt)
        cmds.parent(joint_Middle_Tendon_3_Lt, joint_Middle_1_Lt)
        cmds.parent(joint_Middle_Tendon_4_Lt, joint_Middle_1_Lt)

        cmds.delete(joint_Middle_Tendon_OFF_1_Lt,joint_Middle_Tendon_OFF_2_Lt,joint_Middle_Tendon_OFF_3_Lt,joint_Middle_Tendon_OFF_4_Lt)


        ########################


        #creation ctrls
        ctrl_finger_1_Middle = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_1_Middle_Lt')[0]
        cmds.select(ctrl_finger_1_Middle + '.cv[1]', ctrl_finger_1_Middle + '.cv[5]')
        cmds.scale(1, 1, 0.194499, relative=True, pivot=(0, 0, 0))
        cmds.select(ctrl_finger_1_Middle + '.cv[0]', ctrl_finger_1_Middle + '.cv[6]')
        cmds.scale(1, 1, 0.0840956, relative=True, pivot=(0.783612, 0, 0))

        cmds.matchTransform(ctrl_finger_1_Middle,joint_Middle_1_Lt)
        cmds.select(ctrl_finger_1_Middle+'.cv[0:7]')
        cmds.move(0, 2, 0, relative=True, os=True)


        ctrl_finger_2_Middle = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_2_Middle_Lt')[0]
        cmds.select(ctrl_finger_2_Middle + '.cv[1]', ctrl_finger_2_Middle + '.cv[5]')
        cmds.scale(1, 1, 0.2, relative=True, pivot=(0, 0, 0))

        cmds.matchTransform(ctrl_finger_2_Middle,joint_Middle_2_Lt)
        cmds.select(ctrl_finger_2_Middle+'.cv[0:7]')
        cmds.move(0, 1.5, 0, relative=True, os=True)


        ctrl_finger_3_Middle = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_3_Middle_Lt')[0]
        cmds.matchTransform(ctrl_finger_3_Middle,joint_Middle_3_Lt)
        cmds.select(ctrl_finger_3_Middle+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)


        ctrl_finger_4_Middle = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_4_Middle_Lt')[0]
        cmds.matchTransform(ctrl_finger_4_Middle,joint_Middle_4_Lt)
        cmds.select(ctrl_finger_4_Middle+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)

        ctrl_Ik_Finger_Middle = cmds.curve(n='Ctrl_IK_Middle_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                point = [(0, 1, 0),\
                         (0, 0.92388000000000003, 0.382683),\
                         (0, 0.70710700000000004, 0.70710700000000004),\
                         (0, 0.382683, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0, -0.382683, 0.92388000000000003),\
                         (0, -0.70710700000000004, 0.70710700000000004),\
                         (0, -0.92388000000000003, 0.382683),\
                         (0, -1, 0),\
                         (0, -0.92388000000000003, -0.382683),\
                         (0, -0.70710700000000004, -0.70710700000000004),\
                         (0, -0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 1, 0),\
                         (0.382683, 0.92388000000000003, 0),\
                         (0.70710700000000004, 0.70710700000000004, 0),\
                         (0.92388000000000003, 0.382683, 0),\
                         (1, 0, 0),\
                         (0.92388000000000003, -0.382683, 0),\
                         (0.70710700000000004, -0.70710700000000004, 0),\
                         (0.382683, -0.92388000000000003, 0),\
                         (0, -1, 0),\
                         (-0.382683, -0.92388000000000003, 0),\
                         (-0.70710700000000004, -0.70710700000000004, 0),\
                         (-0.92388000000000003, -0.382683, 0),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0.382683, 0),\
                         (-0.70710700000000004, 0.70710700000000004, 0),\
                         (-0.382683, 0.92388000000000003, 0),\
                         (0, 1, 0),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (-0.382683, 0, -0.92388000000000003),\
                         (-0.70710700000000004, 0, -0.70710700000000004),\
                         (-0.92388000000000003, 0, -0.382683),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0, 0.382683),\
                         (-0.70710700000000004, 0, 0.70710700000000004),\
                         (-0.382683, 0, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0.382683, 0, 0.92388000000000003),\
                         (0.70710700000000004, 0, 0.70710700000000004),\
                         (0.92388000000000003, 0, 0.382683),\
                         (1, 0, 0),\
                         (0.92388000000000003, 0, -0.382683),\
                         (0.70710700000000004, 0, -0.70710700000000004),\
                         (0.382683, 0, -0.92388000000000003),\
                         (0, 0, -1)]\
              )
        cmds.addAttr(ctrl_Ik_Finger_Middle, longName='Space', attributeType='enum', enumName="World:Hand:Head:Hip", k=True )
        cmds.setAttr(ctrl_Ik_Finger_Middle + ".Space", 1)
        cmds.matchTransform(ctrl_Ik_Finger_Middle,joint_Middle_T_Lt)
        cmds.select(ctrl_Ik_Finger_Middle+'.cv[0:52]')
        cmds.scale(0.5, 0.5, 0.5, relative=True)
        cmds.move(0, 0, 0, relative=True)
        


        curve_pole_Vector_Middle = cmds.curve(n='Crv_PV_Middle_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                point = [(-2, 0, 0),\
                         (1, 0, 1),\
                         (1, 0, -1),\
                         (-2, 0, 0),\
                         (1, 1, 0),\
                         (1, 0, 0),\
                         (1, -1, 0),\
                         (-2, 0, 0)]\
              )

        cmds.addAttr(curve_pole_Vector_Middle, longName='Guide_Visibility', attributeType='bool', dv=True, k=True )
        cmds.addAttr(curve_pole_Vector_Middle, longName='Space', attributeType='enum', enumName="World:Hand:Ik_Finger", k=True )
        cmds.setAttr(curve_pole_Vector_Middle + ".Space", 1)
        cmds.matchTransform(curve_pole_Vector_Middle,joint_Middle_3_Lt)
        cmds.select(curve_pole_Vector_Middle)
        cmds.move(0, 3, 0, relative=True, os=True)
        cmds.select(curve_pole_Vector_Middle+'.cv[0:7]')
        cmds.rotate(0, 0, 90, relative=True)
        cmds.scale(0.5, 0.5, 0.5, relative=True)

        





        ctrl_finger_Middle = [ctrl_finger_1_Middle,ctrl_finger_2_Middle,ctrl_finger_3_Middle,ctrl_finger_4_Middle,ctrl_Ik_Finger_Middle,curve_pole_Vector_Middle]
        for offset in ctrl_finger_Middle :
            cmds.select(offset)
            OFF()

        
        ctrl_finger_1_Middle_OFF = cmds.listRelatives(ctrl_finger_1_Middle, parent=True, fullPath=True)
        ctrl_finger_2_Middle_OFF = cmds.listRelatives(ctrl_finger_2_Middle, parent=True, fullPath=True)
        ctrl_finger_3_Middle_OFF = cmds.listRelatives(ctrl_finger_3_Middle, parent=True, fullPath=True)
        ctrl_finger_4_Middle_OFF = cmds.listRelatives(ctrl_finger_4_Middle, parent=True, fullPath=True)
        
        
        
        cmds.parent(ctrl_finger_4_Middle_OFF, ctrl_finger_3_Middle)
        cmds.parent(ctrl_finger_3_Middle_OFF, ctrl_finger_2_Middle)
        cmds.parent(ctrl_finger_2_Middle_OFF, ctrl_finger_1_Middle)

        cmds.parentConstraint( ctrl_finger_1_Middle, joint_Middle_1_Lt )
        cmds.parentConstraint( ctrl_finger_2_Middle, joint_Middle_2_Lt )
        cmds.parentConstraint( ctrl_finger_3_Middle, joint_Middle_3_Lt )
        cmds.parentConstraint( ctrl_finger_4_Middle, joint_Middle_4_Lt )
        


        cmds.setAttr(joint_DRV_Middle_3_Lt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Middle_4_Lt + '.preferredAngleZ', -10.0)

        ik_Handle_Middle_Lt = cmds.ikHandle(n='IKRP_Middle_Lt',  sj=joint_DRV_Middle_2_Lt, ee=joint_DRV_Middle_T_Lt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Middle_Lt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Middle_Lt[0], ctrl_Ik_Finger_Middle)
        cmds.poleVectorConstraint( curve_pole_Vector_Middle, ik_Handle_Middle_Lt[0] )
        


        new_Effector_name_Middle = 'EFF_IKRP_Middle_Lt'
        List_Input_Ik_Handle_Middle = cmds.listConnections('IKRP_Middle_Lt',s=True)
        for node in List_Input_Ik_Handle_Middle:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Middle)
                break
        
        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Middle_OFF = cmds.listRelatives(ctrl_finger_1_Middle, parent=True, fullPath=True)
        ctrl_finger_2_Middle_OFF = cmds.listRelatives(ctrl_finger_2_Middle, parent=True, fullPath=True)
        ctrl_finger_3_Middle_OFF = cmds.listRelatives(ctrl_finger_3_Middle, parent=True, fullPath=True)
        ctrl_finger_4_Middle_OFF = cmds.listRelatives(ctrl_finger_4_Middle, parent=True, fullPath=True)
        curve_pole_Vector_Middle_OFF = cmds.listRelatives(curve_pole_Vector_Middle, parent=True, fullPath=True)
        ctrl_Ik_Finger_Middle_OFF = cmds.listRelatives(ctrl_Ik_Finger_Middle, parent=True, fullPath=True)
        
        decompose_M_DRV_Middle_1_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_1_Lt')
        decompose_M_DRV_Middle_2_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_2_Lt')
        decompose_M_DRV_Middle_3_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_3_Lt')
        decompose_M_DRV_Middle_4_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_4_Lt')

        cmds.connectAttr( f'{joint_DRV_Middle_1_Lt}.xformMatrix', f'{decompose_M_DRV_Middle_1_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_2_Lt}.xformMatrix', f'{decompose_M_DRV_Middle_2_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_3_Lt}.xformMatrix', f'{decompose_M_DRV_Middle_3_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_4_Lt}.xformMatrix', f'{decompose_M_DRV_Middle_4_Lt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Middle_1_Lt}.outputTranslate', f'{ctrl_finger_1_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_2_Lt}.outputTranslate', f'{ctrl_finger_2_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_3_Lt}.outputTranslate', f'{ctrl_finger_3_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_4_Lt}.outputTranslate', f'{ctrl_finger_4_Middle_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Middle_1_Lt}.outputRotate', f'{ctrl_finger_1_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_2_Lt}.outputRotate', f'{ctrl_finger_2_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_3_Lt}.outputRotate', f'{ctrl_finger_3_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_4_Lt}.outputRotate', f'{ctrl_finger_4_Middle_OFF[0]}.rotate' )

        
        cmds.select(deselect=True)
        joint_Middle_knuckle = cmds.joint(  n='Sk_Middle_Knuckle_Lt' , rad=0.75)
        cmds.matchTransform(joint_Middle_knuckle,joint_Middle_2_Lt)
        cmds.parent(joint_Middle_knuckle, joint_Middle_2_Lt )

        
        

        multiply_divide_value_tendon_Middle = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Middle_Lt')
        multiply_divide_lower_intensity_knuckle_tendon_Middle = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Middle_Lt')
        multiply_divide_intensity_knuckle_tendon_Middle = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Middle_Lt')
        condition_positive_tendon_Middle = cmds.createNode( 'condition', n='condition_positive_tendon_Middle_Lt')

        cmds.setAttr(multiply_divide_value_tendon_Middle + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Middle + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Middle + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Middle + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Middle + '.operation', 2)

        cmds.connectAttr( f'{joint_Middle_2_Lt}.rotateZ', f'{condition_positive_tendon_Middle}.firstTerm' )
        cmds.connectAttr( f'{joint_Middle_2_Lt}.rotateZ', f'{multiply_divide_value_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{joint_Middle_2_Lt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Middle}.outColorR', f'{multiply_divide_value_tendon_Middle}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Middle}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Middle}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputY', f'{joint_Middle_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_1_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_1_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_2_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_2_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_3_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_3_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_4_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_4_Lt}.translateZ' )

        
    
        cmds.connectAttr( f'{controler_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2Y' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2X' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2Z' )

        cmds.select(deselect=True)
        ctrls_Middle_to_goup = [ctrl_Ik_Finger_Middle_OFF[0], curve_pole_Vector_Middle_OFF[0], ctrl_finger_1_Middle_OFF[0]]
        group_ctrls_Middle_Lt = cmds.group(em=True, name='Grp_Ctrls_Middle_Lt')
        cmds.parent(ctrls_Middle_to_goup, group_ctrls_Middle_Lt)

        
        joint_Middle_to_goup = [joint_Middle_1_Lt, joint_DRV_Middle_1_Lt ]
        group_joints_Middle_Lt = cmds.group(em=True, name='Grp_Sk_Middle_Lt')
        cmds.parent(joint_Middle_to_goup, group_joints_Middle_Lt)







        #guide visual pv 
        locator_pv_start_Middle_ctrl_Lt = cmds.spaceLocator(n='LOC_Start_Guide_PV_Middle_Lt', p=(0, 0, 0), )
        cmds.matchTransform(locator_pv_start_Middle_ctrl_Lt, joint_Middle_3_Lt)
        cmds.setAttr(locator_pv_start_Middle_ctrl_Lt[0] + '.visibility', 0 )
        locator_pv_end_Middle_ctrl_Lt = cmds.spaceLocator( n='LOC_End_Guide_PV_Middle_Lt', p=(0, 0, 0)  )
        cmds.matchTransform(locator_pv_end_Middle_ctrl_Lt, curve_pole_Vector_Middle)
        cmds.setAttr(locator_pv_end_Middle_ctrl_Lt[0] + '.visibility', 0 )

        locator_pv_start_Middle_ctrl_Lt_position = cmds.xform(locator_pv_start_Middle_ctrl_Lt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Middle_ctrl_Lt_position = cmds.xform(locator_pv_end_Middle_ctrl_Lt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Middle_ctrl_Lt = cmds.curve(d=1, p=[locator_pv_start_Middle_ctrl_Lt_position, locator_pv_end_Middle_ctrl_Lt_position], n='Guide_PV_Middle_Lt')

        decompose_M_curve_start_Middle_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Middle_Lt')
        decompose_M_curve_end_Middle_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Middle_Lt')

        
        #pas besoin
        # listShapes = cmds.listRelatives(curve_pv_Middle_ctrl_Lt, allDescendents=True, type='shape')
        # curve_pv_Middle_ctrl_Lt_shape = listShapes[0]
        # print(curve_pv_Middle_ctrl_Lt_shape)
           
        cmds.connectAttr( f'{locator_pv_start_Middle_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_start_Middle_Lt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Middle_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_end_Middle_Lt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Middle_Lt}.outputTranslate', f'{curve_pv_Middle_ctrl_Lt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Middle_Lt}.outputTranslate', f'{curve_pv_Middle_ctrl_Lt}.controlPoints[1]' )

        cmds.parent(locator_pv_end_Middle_ctrl_Lt, curve_pole_Vector_Middle)
        cmds.parent(locator_pv_start_Middle_ctrl_Lt, joint_Middle_3_Lt)

        cmds.setAttr(curve_pv_Middle_ctrl_Lt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Guide_Visibility', f'{curve_pv_Middle_ctrl_Lt}.visibility' )

        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Middle_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Middle_Lt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Middle_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Middle_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_FingerSpace_PV_Middle_ctrl_Lt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Middle_ctrl_Lt[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Middle_ctrl_Lt, curve_pole_Vector_Middle)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Middle_ctrl_Lt, curve_pole_Vector_Middle)

        hold_matrix_Middle_PV_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Middle_Lt')
        mult_Finger_FingerSpace_PV_Middle_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Middle_Lt')
        mult_Finger_HandSpace_PV_Middle_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Middle_Lt')
        condition_Finger_Space_PV_Middle_Lt = cmds.createNode( 'condition', n='Cond_Space_Middle_PV_Lt')
        condition_Finger_FingerSpace_PV_Middle_Lt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Middle_Lt')
        condition_Finger_HandSpace_PV_Middle_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Middle_Lt')

        blend_matrix_PV_Middle_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Middle_Lt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_PV_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_PV_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Middle_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Middle_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Middle_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Middle_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Middle_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_PV_Middle_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Middle_Lt}.matrixSum', f'{blend_matrix_PV_Middle_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Middle_Lt}.matrixSum', f'{blend_matrix_PV_Middle_Lt}.target[0].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_FingerSpace_PV_Middle_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_HandSpace_PV_Middle_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_Space_PV_Middle_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Middle_Lt}.outColorR', f'{condition_Finger_Space_PV_Middle_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Middle_Lt}.outColorR', f'{condition_Finger_Space_PV_Middle_Lt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Middle_Lt}.outColorR', f'{blend_matrix_PV_Middle_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Middle_Lt}.outColorG', f'{blend_matrix_PV_Middle_Lt}.target[1].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Middle_Lt}.outputMatrix', f'{curve_pole_Vector_Middle}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Middle_ctrl_Lt, ctrl_Ik_Finger_Middle) #et on parente direct le locator de l'ik 




        #Space controller IK a 4 choix

        locator_Finger_HandSpace_IK_Middle_ctrl = cmds.spaceLocator(n='LOC_Finger_HandSpace_IK_Middle_Lt', p=(0, 0, 0), )
        locator_Finger_HeadSpace_IK_Middle_ctrl = cmds.spaceLocator(n='LOC_Finger_HeadSpace_IK_Middle_Lt', p=(0, 0, 0), )
        locator_Finger_HipSpace_IK_Middle_ctrl = cmds.spaceLocator(n='LOC_Finger_HipSpace_IK_Middle_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_HandSpace_IK_Middle_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HeadSpace_IK_Middle_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HipSpace_IK_Middle_ctrl[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_HandSpace_IK_Middle_ctrl,ctrl_Ik_Finger_Middle)
        cmds.matchTransform(locator_Finger_HeadSpace_IK_Middle_ctrl,ctrl_Ik_Finger_Middle)
        cmds.matchTransform(locator_Finger_HipSpace_IK_Middle_ctrl,ctrl_Ik_Finger_Middle)

        hold_matrix_Middle_IK_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Middle_Lt')
        mult_Finger_HandSpace_IK_Middle_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Middle_Lt')
        mult_Finger_HeadSpace_IK_Middle_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Middle_Lt')
        mult_Finger_HipSpace_IK_Middle_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Middle_Lt')
        condition_Finger_Space_IK_Middle_Lt = cmds.createNode( 'condition', n='Cond_Space_Middle_Lt')
        condition_Finger_HandSpace_IK_Middle_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_Middle_Lt')
        condition_Finger_HeadSpace_IK_Middle_Lt = cmds.createNode( 'condition', n='Cond_HeadSpace_Middle_Lt')
        condition_Finger_HipSpace_IK_Middle_Lt = cmds.createNode( 'condition', n='Cond_HipSpace_Middle_Lt')

        blend_matrix_IK_Middle_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Middle_Lt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Lt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_IK_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_IK_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Middle_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Middle_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Middle_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Middle_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Middle_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_IK_Middle_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Middle_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HipSpace_IK_Middle_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Middle_Lt}.matrixSum', f'{blend_matrix_IK_Middle_Lt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Middle_Lt}.matrixSum', f'{blend_matrix_IK_Middle_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Middle_Lt}.matrixSum', f'{blend_matrix_IK_Middle_Lt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HandSpace_IK_Middle_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HeadSpace_IK_Middle_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HipSpace_IK_Middle_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_Space_IK_Middle_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Middle_Lt}.outColorR', f'{condition_Finger_Space_IK_Middle_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Middle_Lt}.outColorR', f'{condition_Finger_Space_IK_Middle_Lt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Middle_Lt}.outColorR', f'{condition_Finger_Space_IK_Middle_Lt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Lt}.outColorR', f'{blend_matrix_IK_Middle_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Lt}.outColorG', f'{blend_matrix_IK_Middle_Lt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Lt}.outColorB', f'{blend_matrix_IK_Middle_Lt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Middle_Lt}.outputMatrix', f'{ctrl_Ik_Finger_Middle}.offsetParentMatrix' )

            #on range les locator space dans les bon endroit

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Lt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Middle_ctrl[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Middle_ctrl[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Middle_ctrl[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Middle_ctrl_Lt[0], sk_Hand)
            
            
        else :
            group_miror_Middle_Loc_Space_IK_temp_Lt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Middle_A_PARENTER_Lt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Middle_ctrl[0], locator_Finger_HeadSpace_IK_Middle_ctrl[0], locator_Finger_HipSpace_IK_Middle_ctrl[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Middle_Loc_Space_IK_temp_Lt)
            cmds.select(deselect=True)



        #set skin
        cmds.select(deselect=True)
        list_set_skin_jnt = [joint_Middle_1_Lt, joint_Middle_2_Lt, joint_Middle_3_Lt, joint_Middle_4_Lt, joint_Middle_Tendon_1_Lt, joint_Middle_Tendon_2_Lt, joint_Middle_Tendon_3_Lt, joint_Middle_Tendon_4_Lt, joint_Middle_knuckle]
        set_name = "MySetJointSkin"
        if cmds.objExists(set_name):
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)
        
        else:
            cmds.sets(n=set_name)
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)


        #rangement dans les groupes
        grp_Controllers = 'Grp_Controllers'
        grp_Skeleton = 'Grp_Skeleton'
        grp_DO_NOT_TOUCH = 'DO_NOT_TOUCH'
        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'



        if not cmds.objExists('Grp_DNT_Hand_Lt'):
            grp_DNT_Hand_Lt = cmds.group(em=True, name='Grp_DNT_Hand_Lt')



        grp_elem_DNT_Middle = [curve_pv_Middle_ctrl_Lt]

        cmds.parent(grp_elem_DNT_Middle, grp_DNT_Hand_Lt )


        if cmds.objExists(grp_Controllers):
            cmds.parent(group_ctrls_Middle_Lt, grp_Controllers)
        else:
            grp_Controllers = cmds.group(em=True, name='Grp_Controllers')
            cmds.parent(group_ctrls_Middle_Lt, grp_Controllers)


        if cmds.objExists(grp_Skeleton):
            cmds.parent(group_joints_Middle_Lt, grp_Skeleton)
        else:
            grp_Skeleton = cmds.group(em=True, name='Grp_Skeleton')
            cmds.parent(group_joints_Middle_Lt, grp_Skeleton)


        if cmds.objExists(grp_DO_NOT_TOUCH):
            if cmds.objExists('Grp_DNT_Hand_Lt'):
                parent_of_grp_DNT_Hand_Lt = cmds.listRelatives(grp_DNT_Hand_Lt, parent=True)
                if not parent_of_grp_DNT_Hand_Lt:
                    cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)
        else:
            grp_DO_NOT_TOUCH = cmds.group(em=True, name='DO_NOT_TOUCH')
            cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{controler_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Middle}.visibility' )


        #on fait la parentée pour que les mains suivent la structure generale

        DRV_Palm_IK_Lt = "DRV_Palm_IK_Lt"
        if cmds.objExists(DRV_Palm_IK_Lt):
            cmds.parentConstraint(DRV_Palm_IK_Lt, joint_DRV_Middle_1_Lt, mo=True)   

            
        #couleurs des controllers 
        jnt_color_Blue = [ctrl_finger_1_Middle, ctrl_finger_2_Middle, ctrl_finger_3_Middle, ctrl_finger_4_Middle, ctrl_Ik_Finger_Middle]
        jnt_color_DarkBlue = [ctrl_finger_3_Middle, ctrl_finger_4_Middle]
        jnt_color_beige= [curve_pole_Vector_Middle]
        

        for objcolor_Blue in jnt_color_Blue : 
            cmds.setAttr(objcolor_Blue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Blue + '.overrideColor', 6)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 5)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21) 

    def middle_rig_Part_3_Miror(*args):

        duplication_group_ctrls_sk = cmds.duplicate(group_ctrls_Middle_Lt,group_joints_Middle_Lt, rc=True)
        

        for Delnode in duplication_group_ctrls_sk: 
            string_del = ['EFF', 'Constraint', 'IKRP_Middle_Lt', 'LOC_Finger_FingerSpace_PV_Middle_Lt1']
            for substring in string_del:
                if Delnode.find(substring) != -1 and cmds.objExists(Delnode):
                    cmds.delete(Delnode)


             
        
        for rename in duplication_group_ctrls_sk:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        group_ctrls_Middle_Rt = 'Grp_Ctrls_Middle_Rt'
        group_joints_Middle_Rt = 'Grp_Sk_Middle_Rt'

        
    
        cmds.setAttr(group_ctrls_Middle_Rt + '.scaleX', -1 )
        cmds.setAttr(group_joints_Middle_Rt + '.scaleX', -1 )



        #réassignation des varables pour le miror
        ctrl_finger_1_Middle = 'Ctrl_Finger_1_Middle_Rt'
        ctrl_finger_2_Middle = 'Ctrl_Finger_2_Middle_Rt'
        ctrl_finger_3_Middle = 'Ctrl_Finger_3_Middle_Rt'
        ctrl_finger_4_Middle = 'Ctrl_Finger_4_Middle_Rt'
        curve_pole_Vector_Middle = 'Crv_PV_Middle_Rt'
        ctrl_Ik_Finger_Middle = 'Ctrl_IK_Middle_Rt'

        joint_DRV_Middle_1_Rt = 'DRV_Middle_1_Rt'
        joint_DRV_Middle_2_Rt = 'DRV_Middle_2_Rt'
        joint_DRV_Middle_3_Rt = 'DRV_Middle_3_Rt'
        joint_DRV_Middle_4_Rt = 'DRV_Middle_4_Rt'
        joint_DRV_Middle_T_Rt = 'DRV_Middle_T_Rt'
        joint_Middle_1_Rt = 'Sk_Middle_1_Rt'
        joint_Middle_2_Rt = 'Sk_Middle_2_Rt'
        joint_Middle_3_Rt = 'Sk_Middle_3_Rt'
        joint_Middle_4_Rt = 'Sk_Middle_4_Rt'
        joint_Middle_T_Rt = 'Sk_Middle_T_Rt'
        joint_Middle_Tendon_1_Rt = 'Sk_Middle_Tendon_1_Rt'
        joint_Middle_Tendon_2_Rt = 'Sk_Middle_Tendon_2_Rt'
        joint_Middle_Tendon_3_Rt = 'Sk_Middle_Tendon_3_Rt'
        joint_Middle_Tendon_4_Rt = 'Sk_Middle_Tendon_4_Rt'
        joint_Middle_knuckle = 'Sk_Middle_Knuckle_Rt'

        duplication_ctrl_hand_control = 'Ctrl_Control_Hand_Rt'
        locator_pv_start_Middle_ctrl_Rt = 'LOC_Start_Guide_PV_Middle_Rt'
        locator_pv_end_Middle_ctrl_Rt = 'LOC_End_Guide_PV_Middle_Rt'



        '''
        duplication du code au dessus qui suit

        '''

        cmds.parentConstraint( ctrl_finger_1_Middle, joint_Middle_1_Rt )
        cmds.parentConstraint( ctrl_finger_2_Middle, joint_Middle_2_Rt )
        cmds.parentConstraint( ctrl_finger_3_Middle, joint_Middle_3_Rt )
        cmds.parentConstraint( ctrl_finger_4_Middle, joint_Middle_4_Rt )
        


        cmds.setAttr(joint_DRV_Middle_3_Rt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Middle_4_Rt + '.preferredAngleZ', -10.0)

        ik_Handle_Middle_Rt = cmds.ikHandle(n='IKRP_Middle_Rt',  sj=joint_DRV_Middle_2_Rt, ee=joint_DRV_Middle_T_Rt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Middle_Rt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Middle_Rt[0], ctrl_Ik_Finger_Middle)
        cmds.poleVectorConstraint( curve_pole_Vector_Middle, ik_Handle_Middle_Rt[0] )


        new_Effector_name_Middle = 'EFF_IKRP_Middle_Rt'
        List_Input_Ik_Handle_Middle = cmds.listConnections('IKRP_Middle_Rt',s=True)
        for node in List_Input_Ik_Handle_Middle:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Middle)
                break
        

        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Middle_OFF = cmds.listRelatives(ctrl_finger_1_Middle, parent=True, fullPath=True)
        ctrl_finger_2_Middle_OFF = cmds.listRelatives(ctrl_finger_2_Middle, parent=True, fullPath=True)
        ctrl_finger_3_Middle_OFF = cmds.listRelatives(ctrl_finger_3_Middle, parent=True, fullPath=True)
        ctrl_finger_4_Middle_OFF = cmds.listRelatives(ctrl_finger_4_Middle, parent=True, fullPath=True)
        curve_pole_Vector_Middle_OFF = cmds.listRelatives(curve_pole_Vector_Middle, parent=True, fullPath=True)
        ctrl_Ik_Finger_Middle_OFF = cmds.listRelatives(ctrl_Ik_Finger_Middle, parent=True, fullPath=True)
        
        decompose_M_DRV_Middle_1_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_1_Rt')
        decompose_M_DRV_Middle_2_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_2_Rt')
        decompose_M_DRV_Middle_3_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_3_Rt')
        decompose_M_DRV_Middle_4_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Middle_4_Rt')

        cmds.connectAttr( f'{joint_DRV_Middle_1_Rt}.xformMatrix', f'{decompose_M_DRV_Middle_1_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_2_Rt}.xformMatrix', f'{decompose_M_DRV_Middle_2_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_3_Rt}.xformMatrix', f'{decompose_M_DRV_Middle_3_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Middle_4_Rt}.xformMatrix', f'{decompose_M_DRV_Middle_4_Rt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Middle_1_Rt}.outputTranslate', f'{ctrl_finger_1_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_2_Rt}.outputTranslate', f'{ctrl_finger_2_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_3_Rt}.outputTranslate', f'{ctrl_finger_3_Middle_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_4_Rt}.outputTranslate', f'{ctrl_finger_4_Middle_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Middle_1_Rt}.outputRotate', f'{ctrl_finger_1_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_2_Rt}.outputRotate', f'{ctrl_finger_2_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_3_Rt}.outputRotate', f'{ctrl_finger_3_Middle_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Middle_4_Rt}.outputRotate', f'{ctrl_finger_4_Middle_OFF[0]}.rotate' )

        

        multiply_divide_value_tendon_Middle = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Middle_Rt')
        multiply_divide_lower_intensity_knuckle_tendon_Middle = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Middle_Rt')
        multiply_divide_intensity_knuckle_tendon_Middle = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Middle_Rt')
        condition_positive_tendon_Middle = cmds.createNode( 'condition', n='condition_positive_tendon_Middle_Rt')

        cmds.setAttr(multiply_divide_value_tendon_Middle + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Middle + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Middle + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Middle + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Middle + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Middle + '.operation', 2)

        cmds.connectAttr( f'{joint_Middle_2_Rt}.rotateZ', f'{condition_positive_tendon_Middle}.firstTerm' )
        cmds.connectAttr( f'{joint_Middle_2_Rt}.rotateZ', f'{multiply_divide_value_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{joint_Middle_2_Rt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Middle}.outColorR', f'{multiply_divide_value_tendon_Middle}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Middle}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Middle}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Middle}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputY', f'{joint_Middle_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_1_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_1_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_2_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_2_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_3_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_3_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputX', f'{joint_Middle_Tendon_4_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Middle}.outputZ', f'{joint_Middle_Tendon_4_Rt}.translateZ' )

        
    
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2Y' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2X' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Middle}.input2Z' )

        cmds.select(deselect=True)

        

        #miror
        locator_pv_start_Middle_ctrl_Rt_position = cmds.xform(locator_pv_start_Middle_ctrl_Rt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Middle_ctrl_Rt_position = cmds.xform(locator_pv_end_Middle_ctrl_Rt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Middle_ctrl_Rt = cmds.curve(d=1, p=[locator_pv_start_Middle_ctrl_Rt_position, locator_pv_end_Middle_ctrl_Rt_position], n='Guide_PV_Middle_Rt')

        decompose_M_curve_start_Middle_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Middle_Rt')
        decompose_M_curve_end_Middle_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Middle_Rt')

        
        #pas besoin
           
        cmds.connectAttr( f'{locator_pv_start_Middle_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_start_Middle_Rt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Middle_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_end_Middle_Rt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Middle_Rt}.outputTranslate', f'{curve_pv_Middle_ctrl_Rt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Middle_Rt}.outputTranslate', f'{curve_pv_Middle_ctrl_Rt}.controlPoints[1]' )

        

        cmds.setAttr(curve_pv_Middle_ctrl_Rt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Guide_Visibility', f'{curve_pv_Middle_ctrl_Rt}.visibility' )


        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Middle_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Middle_Rt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Middle_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Middle_Rt', p=(0, 0, 0))
        cmds.parent(locator_Finger_FingerSpace_PV_Middle_ctrl_Rt, curve_pole_Vector_Middle )
        cmds.parent(locator_Finger_HandSpace_PV_Middle_ctrl_Rt, curve_pole_Vector_Middle )
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Middle_ctrl_Rt, curve_pole_Vector_Middle)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Middle_ctrl_Rt, curve_pole_Vector_Middle)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Middle_ctrl_Rt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Middle_ctrl_Rt[0] + '.visibility', 0)
        

        hold_matrix_Middle_PV_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Middle_Rt')
        mult_Finger_FingerSpace_PV_Middle_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Middle_Rt')
        mult_Finger_HandSpace_PV_Middle_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Middle_Rt')
        condition_Finger_Space_PV_Middle_Rt = cmds.createNode( 'condition', n='Cond_Space_Middle_PV_Rt')
        condition_Finger_FingerSpace_PV_Middle_Rt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Middle_Rt')
        condition_Finger_HandSpace_PV_Middle_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Middle_Rt')

        blend_matrix_PV_Middle_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Middle_Rt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Middle_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Middle_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_PV_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Middle_PV_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Middle_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Middle_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Middle_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Middle_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Middle_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Middle_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_PV_Middle_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Middle_Rt}.matrixSum', f'{blend_matrix_PV_Middle_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Middle_Rt}.matrixSum', f'{blend_matrix_PV_Middle_Rt}.target[1].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_FingerSpace_PV_Middle_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_HandSpace_PV_Middle_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Middle}.Space', f'{condition_Finger_Space_PV_Middle_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Middle_Rt}.outColorR', f'{condition_Finger_Space_PV_Middle_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Middle_Rt}.outColorR', f'{condition_Finger_Space_PV_Middle_Rt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Middle_Rt}.outColorR', f'{blend_matrix_PV_Middle_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Middle_Rt}.outColorG', f'{blend_matrix_PV_Middle_Rt}.target[0].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Middle_Rt}.outputMatrix', f'{curve_pole_Vector_Middle}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Middle_ctrl_Rt, ctrl_Ik_Finger_Middle) #et on parente direct le locator de l'ik 





                #Space controller IK a 4 choix MIROR    
        

        # le coté rt ne marche pas avec ça donc il faut venir faire une duplication des anciens locators
            #on vient recuperer les anciens locators
        list_locator_MiddleSpace_dup = [locator_Finger_HipSpace_IK_Middle_ctrl  , locator_Finger_HeadSpace_IK_Middle_ctrl ,   locator_Finger_HandSpace_IK_Middle_ctrl ]

            #on cree une nouvelle liste qui va aceuillir nos nouveaux locators
        new_list_locator_MiddleSpace_dup = []
        for elem in list_locator_MiddleSpace_dup:
            duplication_group_loc_space = cmds.duplicate(elem,  rc=True)
            new_list_locator_MiddleSpace_dup.append(duplication_group_loc_space)

            #on cree le grp temporaire qui va scale -1
        group_miror_locators_MiddleSpace = cmds.group(empty=True, n='Grp_Temp_miror_Loc_Middle_Rt')

            

            #on parente les nouveaux elements de la nouvelle liste au grp  et ensuite on scale le groupe pour miror
        for elem in new_list_locator_MiddleSpace_dup :
            cmds.parent(elem, group_miror_locators_MiddleSpace)

        cmds.setAttr(group_miror_locators_MiddleSpace + ".scaleX", -1)

            #on vient faire une list relative pour identifier les enfants et pas que ça poe de probleme pour le rename 
        group_miror_locators_MiddleSpace_children = cmds.listRelatives(group_miror_locators_MiddleSpace, c=True)

            #on vient les renommer en rt
        for rename in group_miror_locators_MiddleSpace_children:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        locator_Finger_HandSpace_IK_Middle_ctrl_Rt = 'LOC_Finger_HandSpace_IK_Middle_Rt'
        locator_Finger_HeadSpace_IK_Middle_ctrl_Rt = 'LOC_Finger_HeadSpace_IK_Middle_Rt'
        locator_Finger_HipSpace_IK_Middle_ctrl_Rt = 'LOC_Finger_HipSpace_IK_Middle_Rt'

        
        cmds.select(locator_Finger_HandSpace_IK_Middle_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HeadSpace_IK_Middle_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HipSpace_IK_Middle_ctrl_Rt)                
        OFF()
        

        

        locator_Finger_HandSpace_IK_Middle_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HandSpace_IK_Middle_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HeadSpace_IK_Middle_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HeadSpace_IK_Middle_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HipSpace_IK_Middle_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HipSpace_IK_Middle_ctrl_Rt, parent=True, fullPath=True)
        


        hold_matrix_Middle_IK_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Middle_Rt')
        mult_Finger_HandSpace_IK_Middle_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Middle_Rt')
        mult_Finger_HeadSpace_IK_Middle_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Middle_Rt')
        mult_Finger_HipSpace_IK_Middle_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Middle_Rt')
        condition_Finger_Space_IK_Middle_Rt = cmds.createNode( 'condition', n='Cond_Space_Middle_Rt')
        condition_Finger_HandSpace_IK_Middle_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_Middle_Rt')
        condition_Finger_HeadSpace_IK_Middle_Rt = cmds.createNode( 'condition', n='Cond_HeadSpace_Middle_Rt')
        condition_Finger_HipSpace_IK_Middle_Rt = cmds.createNode( 'condition', n='Cond_HipSpace_Middle_Rt')

        blend_matrix_IK_Middle_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Middle_Rt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Rt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Middle_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Middle_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Middle_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Middle_IK_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Middle_IK_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Middle_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Middle_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Middle_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Middle_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Middle_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Middle_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_IK_Middle_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Middle_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Middle_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HipSpace_IK_Middle_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Middle_Rt}.matrixSum', f'{blend_matrix_IK_Middle_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Middle_Rt}.matrixSum', f'{blend_matrix_IK_Middle_Rt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Middle_Rt}.matrixSum', f'{blend_matrix_IK_Middle_Rt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HandSpace_IK_Middle_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HeadSpace_IK_Middle_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_HipSpace_IK_Middle_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Middle}.Space', f'{condition_Finger_Space_IK_Middle_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Middle_Rt}.outColorR', f'{condition_Finger_Space_IK_Middle_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Middle_Rt}.outColorR', f'{condition_Finger_Space_IK_Middle_Rt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Middle_Rt}.outColorR', f'{condition_Finger_Space_IK_Middle_Rt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Rt}.outColorR', f'{blend_matrix_IK_Middle_Rt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Rt}.outColorG', f'{blend_matrix_IK_Middle_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Middle_Rt}.outColorB', f'{blend_matrix_IK_Middle_Rt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Middle_Rt}.outputMatrix', f'{ctrl_Ik_Finger_Middle}.offsetParentMatrix' )  


            #on parente les locators

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Rt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Middle_ctrl_Rt_OFF[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Middle_ctrl_Rt_OFF[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Middle_ctrl_Rt_OFF[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Middle_ctrl_Rt[0], sk_Hand)
            
            
        else :
            group_miror_Middle_Loc_Space_IK_temp_Rt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Middle_A_PARENTER_Rt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Middle_ctrl_Rt_OFF[0], locator_Finger_HeadSpace_IK_Middle_ctrl_Rt_OFF[0], locator_Finger_HipSpace_IK_Middle_ctrl_Rt_OFF[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Middle_Loc_Space_IK_temp_Rt)
            cmds.select(deselect=True)

        #apres ça on supprime le grp scale -1 des locators 
        cmds.delete(group_miror_locators_MiddleSpace)


        #parenter les crv guides 

        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'
        cmds.parent(curve_pv_Middle_ctrl_Rt, grp_DNT_Hand_Lt)


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Middle}.visibility' )    

        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Rt = "DRV_Palm_IK_Rt"
        if cmds.objExists(DRV_Palm_IK_Rt):
            cmds.parentConstraint(DRV_Palm_IK_Rt, joint_DRV_Middle_1_Rt, mo=True)   

        
        #couleurs des controllers 
        jnt_color_Red = [ctrl_finger_1_Middle, ctrl_finger_2_Middle, ctrl_finger_3_Middle, ctrl_finger_4_Middle, ctrl_Ik_Finger_Middle]
        jnt_color_DarkBlue = [ctrl_finger_3_Middle, ctrl_finger_4_Middle]
        jnt_color_beige= [curve_pole_Vector_Middle]
        

        for objcolor_Red in jnt_color_Red : 
            cmds.setAttr(objcolor_Red + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Red + '.overrideColor', 13)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 18)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def middle_rig_Suppr(*args): 
        
        middle_finger_to_suppr = ['Grp_Ctrls_Middle_Lt', 'Grp_Sk_Middle_Lt','Guide_PV_Middle_Lt', 'Grp_LOC_Space_Ik_Finger_Middle_A_PARENTER_Lt', 'Grp_Ctrls_Middle_Rt', 'Grp_Sk_Middle_Rt','Guide_PV_Middle_Rt', 'Grp_LOC_Space_Ik_Finger_Middle_A_PARENTER_Rt']
        identify_middle_finger_to_suppr = cmds.listRelatives(middle_finger_to_suppr, ad=True)
        list_suppr = [middle_finger_to_suppr]

        for i in range(100):
            list_suppr.append(identify_middle_finger_to_suppr)
            identify_middle_finger_to_suppr = cmds.listConnections(identify_middle_finger_to_suppr, d=True, s=True)
            
            if not identify_middle_finger_to_suppr:
                break

        list_suppr_2 = []
        list_Not_Suppr_middle = ['defaultRenderUtilityList', 'MayaNodeEditorSavedTabsInfo', 'Ctrl_Control_Hand', 'Index', 'Ring', 'Pinky', 'Thumb','bindPose','ikRPsolver','ikSCsolver','hikSolver', 'ikSplineSolver','ikSystem','MySetJointSkin']

        for elem in list_suppr:
            for node in elem:
                skip_node = False

                for middle_name in list_Not_Suppr_middle:
                    if middle_name in node:
                        skip_node = True
                        break

                if not skip_node:
                    list_suppr_2.append(node)

        cmds.delete(list_suppr_2)  
###   
    
    def ring_rig_Part_1(*args):
        
        global joint_DRV_Ring_1_Lt
        global joint_DRV_Ring_2_Lt
        global joint_DRV_Ring_3_Lt
        global joint_DRV_Ring_4_Lt
        global joint_DRV_Ring_T_Lt
        global curve_MP_Ring_Lt
        global joint_DRV_Ring_3_OFF_Lt
        global joint_DRV_Ring_4_OFF_Lt
        
        global joint_Ring_Tendon_1_Lt
        global joint_Ring_Tendon_2_Lt
        global joint_Ring_Tendon_3_Lt
        global joint_Ring_Tendon_4_Lt
        global curve_MP_Ring_Tendon_Lt
        global joint_Ring_Tendon_OFF_1_Lt
        global joint_Ring_Tendon_OFF_2_Lt
        global joint_Ring_Tendon_OFF_3_Lt
        global joint_Ring_Tendon_OFF_4_Lt
        global loc_Ring_orientaton_joints_Lt
        global loc_Ring_orientaton_joints_Lt_grp
        
        

        cmds.select(deselect=True)
        joint_DRV_Ring_1_Lt = cmds.joint(n='DRV_Ring_1_Lt', p=(55, 105, -7.5))
        joint_DRV_Ring_2_Lt = cmds.joint(n='DRV_Ring_2_Lt', p=(60, 100, -8.5))
        joint_DRV_Ring_3_Lt = cmds.joint(n='DRV_Ring_3_Lt', p=(5, 0, 5))
        joint_DRV_Ring_4_Lt = cmds.joint(n='DRV_Ring_4_Lt', p=(10, 0, 5))
        joint_DRV_Ring_T_Lt = cmds.joint(n='DRV_Ring_T_Lt', p=(67, 92.5, -10), rad=0.5)

        cmds.parent(joint_DRV_Ring_T_Lt, world=True)
        cmds.parent(joint_DRV_Ring_4_Lt, world=True)
        cmds.parent(joint_DRV_Ring_3_Lt, world=True)
        cmds.parent(joint_DRV_Ring_2_Lt, world=True)
        
       
        
        joint_Ring_Tendon_1_Lt = cmds.joint(n='Sk_Ring_Tendon_1_Lt', p=(-8, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Ring_Tendon_2_Lt = cmds.joint(n='Sk_Ring_Tendon_2_Lt', p=(-6, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Ring_Tendon_3_Lt = cmds.joint(n='Sk_Ring_Tendon_3_Lt', p=(-4, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Ring_Tendon_4_Lt = cmds.joint(n='Sk_Ring_Tendon_4_Lt', p=(-2, 0, 5), rad=0.2)


        jnt_finger_Ring = [joint_DRV_Ring_3_Lt,joint_DRV_Ring_4_Lt,joint_Ring_Tendon_1_Lt,joint_Ring_Tendon_2_Lt,joint_Ring_Tendon_3_Lt,joint_Ring_Tendon_4_Lt]
        for offset in jnt_finger_Ring :
            cmds.select(offset)
            OFF()


        joint_DRV_Ring_3_OFF_Lt = cmds.listRelatives(joint_DRV_Ring_3_Lt, parent=True, fullPath=True)        
        joint_DRV_Ring_4_OFF_Lt = cmds.listRelatives(joint_DRV_Ring_4_Lt, parent=True, fullPath=True)

        joint_Ring_Tendon_OFF_1_Lt = cmds.listRelatives(joint_Ring_Tendon_1_Lt, parent=True, fullPath=True)
        joint_Ring_Tendon_OFF_2_Lt = cmds.listRelatives(joint_Ring_Tendon_2_Lt, parent=True, fullPath=True)
        joint_Ring_Tendon_OFF_3_Lt = cmds.listRelatives(joint_Ring_Tendon_3_Lt, parent=True, fullPath=True)
        joint_Ring_Tendon_OFF_4_Lt = cmds.listRelatives(joint_Ring_Tendon_4_Lt, parent=True, fullPath=True)



        jnt_0_Crv_Position_Ring = cmds.xform(joint_DRV_Ring_1_Lt, query=True, worldSpace=True, translation=True)
        jnt_1_Crv_Position_Ring = cmds.xform(joint_DRV_Ring_2_Lt, query=True, worldSpace=True, translation=True)
        jnt_2_Crv_Position_Ring = cmds.xform(joint_DRV_Ring_T_Lt, query=True, worldSpace=True, translation=True)
        joint_Skin_Crv_Ring_1_Lt = [joint_DRV_Ring_2_Lt , joint_DRV_Ring_T_Lt]
        joint_Skin_Crv_Ring_2_Lt = [joint_DRV_Ring_1_Lt ,joint_DRV_Ring_2_Lt]

        curve_MP_Ring_Lt = cmds.curve(d=1, p=[jnt_1_Crv_Position_Ring, jnt_2_Crv_Position_Ring], n='Crv_MP_Ring_Lt_Temp')
        curve_MP_Ring_Tendon_Lt = cmds.curve(d=1, p=[jnt_0_Crv_Position_Ring, jnt_1_Crv_Position_Ring], n='Crv_MP_Ring_Tendon_Lt_Temp')

        bind_skin_cluster_Ring = cmds.skinCluster(joint_Skin_Crv_Ring_1_Lt, curve_MP_Ring_Lt, tsb=True)
        bind_skin_cluster_tendon_Ring = cmds.skinCluster(joint_Skin_Crv_Ring_2_Lt, curve_MP_Ring_Tendon_Lt, tsb=True)



        cmds.pathAnimation( joint_DRV_Ring_3_OFF_Lt, c=curve_MP_Ring_Lt, su=0.3333, follow=True)
        cmds.pathAnimation( joint_DRV_Ring_4_OFF_Lt, c=curve_MP_Ring_Lt, su=0.6666, follow=True)

        cmds.pathAnimation( joint_Ring_Tendon_OFF_1_Lt, c=curve_MP_Ring_Tendon_Lt, su=0.2, follow=True)
        cmds.pathAnimation( joint_Ring_Tendon_OFF_2_Lt, c=curve_MP_Ring_Tendon_Lt, su=0.4, follow=True)
        cmds.pathAnimation( joint_Ring_Tendon_OFF_3_Lt, c=curve_MP_Ring_Tendon_Lt, su=0.6, follow=True)
        cmds.pathAnimation( joint_Ring_Tendon_OFF_4_Lt, c=curve_MP_Ring_Tendon_Lt, su=0.8, follow=True)
        

        attributes_to_lock_Ring = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Ring:
            cmds.setAttr(joint_DRV_Ring_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_DRV_Ring_4_Lt + "." + attr, lock=True)

        attributes_to_lock_tendon_Ring = ["rotateX","rotateY","rotateZ","translateX","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_tendon_Ring:
            cmds.setAttr(joint_Ring_Tendon_1_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Ring_Tendon_2_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Ring_Tendon_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Ring_Tendon_4_Lt + "." + attr, lock=True)

        

        cmds.select(deselect=True)
        list_grp_placement_jnt = [joint_DRV_Ring_1_Lt, joint_DRV_Ring_2_Lt, joint_DRV_Ring_T_Lt]
        grp_name = "Grp_Deplacement_Groupe_Main_Temp"
        if cmds.objExists(grp_name):
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)
        
        else:
            cmds.group(em=True, n=grp_name)
             
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)


        # cmds.setAttr(joint_DRV_Ring_1_Lt + ".translatex" + attr, lock=True)

        #loc orientation du doigt
        loc_Ring_orientaton_joints_Lt = cmds.spaceLocator(n='LOC_Guide_Orient_Ring_Lt_TEMP', p=(0, 0, 0), )
        
        
        cmds.select(loc_Ring_orientaton_joints_Lt)
        loc_Ring_orientaton_joints_Lt_grp = cmds.group(loc_Ring_orientaton_joints_Lt[0], n= 'temp_loc_Ring')
        loc_Ring_orientaton_joints_Lt_grp = cmds.listRelatives(loc_Ring_orientaton_joints_Lt, parent=True, fullPath=True)
        cmds.pathAnimation( loc_Ring_orientaton_joints_Lt_grp, c=curve_MP_Ring_Lt, su=0.5, follow=True)
        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + '.rotateX', 90)
        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + '.rotateY', 0)
        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + '.rotateZ', 90)

        attributes_to_lock_LOC_Ring = ["rotateY","rotateZ","translateX","translateY","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_LOC_Ring:
            cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + "." + attr, lock=True)

        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + ".localScaleX" ,0.25)
        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + ".localScaleY" ,2.25)
        cmds.setAttr(loc_Ring_orientaton_joints_Lt[0] + ".localScaleZ" ,0.25)



        #color
        jnt_color_green = [joint_DRV_Ring_1_Lt,joint_DRV_Ring_2_Lt, joint_DRV_Ring_T_Lt, loc_Ring_orientaton_joints_Lt[0]]
        jnt_color_yellow= [joint_Ring_Tendon_1_Lt , joint_Ring_Tendon_2_Lt, joint_Ring_Tendon_3_Lt, joint_Ring_Tendon_4_Lt, joint_DRV_Ring_3_Lt, joint_DRV_Ring_4_Lt ]

        for objcolorgreen in jnt_color_green : 
            cmds.setAttr(objcolorgreen + '.overrideEnabled', 1)
            cmds.setAttr(objcolorgreen + '.overrideColor', 14)

        for objcoloryelllow in jnt_color_yellow : 
            cmds.setAttr(objcoloryelllow + '.overrideEnabled', 1)
            cmds.setAttr(objcoloryelllow + '.overrideColor', 17)
             
    def ring_rig_Part_2(*args):

        global group_ctrls_Ring_Lt
        global group_joints_Ring_Lt
        global new_Effector_name_Inde
        global group_miror_Ring_Loc_Space_IK_temp_Lt
        global locator_Finger_HipSpace_IK_Ring_ctrl
        global locator_Finger_HeadSpace_IK_Ring_ctrl
        global locator_Finger_HandSpace_IK_Ring_ctrl

        global locator_Finger_Space_PV_Ring_ctrl


        controler_hand_control = 'Ctrl_Control_Hand_Lt'

        cmds.delete(curve_MP_Ring_Lt, curve_MP_Ring_Tendon_Lt)

        attributes_to_lock_Ring = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Ring:
            cmds.setAttr(joint_DRV_Ring_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_DRV_Ring_4_Lt + "." + attr, lock=False)

        attributes_to_lock_tendon_Ring = ["translateX"]
        for attr in attributes_to_lock_tendon_Ring:
            cmds.setAttr(joint_Ring_Tendon_1_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Ring_Tendon_2_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Ring_Tendon_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Ring_Tendon_4_Lt + "." + attr, lock=False)



        ################################


        # orient le premier jnt 01 sans affecter les autres
        cmds.parent(joint_DRV_Ring_2_Lt, joint_DRV_Ring_1_Lt)
        cmds.joint(joint_DRV_Ring_1_Lt, edit=True, oj = 'xyz', sao='yup')
        cmds.parent(joint_DRV_Ring_2_Lt, world=True)
        cmds.matchTransform(joint_DRV_Ring_1_Lt,loc_Ring_orientaton_joints_Lt, rx=True, ry=False, rz=False)



        cmds.matchTransform(joint_DRV_Ring_2_Lt,loc_Ring_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Ring_3_Lt,loc_Ring_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Ring_4_Lt,loc_Ring_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Ring_T_Lt,loc_Ring_orientaton_joints_Lt, rot=True)
        
        
        cmds.parent(joint_DRV_Ring_T_Lt, joint_DRV_Ring_4_Lt)
        cmds.parent(joint_DRV_Ring_4_Lt, joint_DRV_Ring_3_Lt)
        cmds.parent(joint_DRV_Ring_3_Lt, joint_DRV_Ring_2_Lt)
        cmds.parent(joint_DRV_Ring_2_Lt, joint_DRV_Ring_1_Lt)
        cmds.delete (joint_DRV_Ring_3_OFF_Lt,joint_DRV_Ring_4_OFF_Lt)


        cmds.select(deselect=True)
        joint_Ring_1_Lt = cmds.joint(  n='Sk_Ring_1_Lt', rad=0.25 )
        cmds.matchTransform(joint_Ring_1_Lt,joint_DRV_Ring_1_Lt)
        cmds.select(deselect=True)
        joint_Ring_2_Lt = cmds.joint( n='Sk_Ring_2_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Ring_2_Lt,joint_DRV_Ring_2_Lt)
        joint_Ring_3_Lt = cmds.joint(  n='Sk_Ring_3_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Ring_3_Lt,joint_DRV_Ring_3_Lt)
        joint_Ring_4_Lt = cmds.joint(n='Sk_Ring_4_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Ring_4_Lt,joint_DRV_Ring_4_Lt)
        joint_Ring_T_Lt = cmds.joint(n='Sk_Ring_T_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Ring_T_Lt,joint_DRV_Ring_T_Lt)



        cmds.parent(joint_Ring_T_Lt, joint_Ring_4_Lt)
        cmds.parent(joint_Ring_4_Lt, joint_Ring_3_Lt)
        cmds.parent(joint_Ring_3_Lt, joint_Ring_2_Lt)
        cmds.parent(joint_Ring_2_Lt, joint_Ring_1_Lt)



        #freeze transform jnts avant d'orient
        cmds.select(deselect=True)
        cmds.select(joint_DRV_Ring_1_Lt,joint_DRV_Ring_2_Lt,joint_DRV_Ring_3_Lt,joint_DRV_Ring_4_Lt,joint_DRV_Ring_T_Lt,joint_Ring_1_Lt,joint_Ring_2_Lt,joint_Ring_3_Lt,joint_Ring_4_Lt,joint_Ring_T_Lt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        #delete le loc orientation 
        cmds.delete(loc_Ring_orientaton_joints_Lt_grp)

        position_joint_DRV_Ring_2_Lt = cmds.xform(joint_DRV_Ring_2_Lt, query=True, worldSpace=True, translation=True)

        cmds.parent(joint_Ring_Tendon_1_Lt, joint_Ring_1_Lt)
        cmds.parent(joint_Ring_Tendon_2_Lt, joint_Ring_1_Lt)
        cmds.parent(joint_Ring_Tendon_3_Lt, joint_Ring_1_Lt)
        cmds.parent(joint_Ring_Tendon_4_Lt, joint_Ring_1_Lt)

        cmds.delete(joint_Ring_Tendon_OFF_1_Lt,joint_Ring_Tendon_OFF_2_Lt,joint_Ring_Tendon_OFF_3_Lt,joint_Ring_Tendon_OFF_4_Lt)




        ########################


        #creation ctrls
        ctrl_finger_1_Ring = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_1_Ring_Lt')[0]
        cmds.select(ctrl_finger_1_Ring + '.cv[1]', ctrl_finger_1_Ring + '.cv[5]')
        cmds.scale(1, 1, 0.194499, relative=True, pivot=(0, 0, 0))
        cmds.select(ctrl_finger_1_Ring + '.cv[0]', ctrl_finger_1_Ring + '.cv[6]')
        cmds.scale(1, 1, 0.0840956, relative=True, pivot=(0.783612, 0, 0))

        cmds.matchTransform(ctrl_finger_1_Ring,joint_Ring_1_Lt)
        cmds.select(ctrl_finger_1_Ring+'.cv[0:7]')
        cmds.move(0, 2, 0, relative=True, os=True)


        ctrl_finger_2_Ring = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_2_Ring_Lt')[0]
        cmds.select(ctrl_finger_2_Ring + '.cv[1]', ctrl_finger_2_Ring + '.cv[5]')
        cmds.scale(1, 1, 0.2, relative=True, pivot=(0, 0, 0))

        cmds.matchTransform(ctrl_finger_2_Ring,joint_Ring_2_Lt)
        cmds.select(ctrl_finger_2_Ring+'.cv[0:7]')
        cmds.move(0, 1.5, 0, relative=True, os=True)


        ctrl_finger_3_Ring = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_3_Ring_Lt')[0]
        cmds.matchTransform(ctrl_finger_3_Ring,joint_Ring_3_Lt)
        cmds.select(ctrl_finger_3_Ring+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)


        ctrl_finger_4_Ring = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_4_Ring_Lt')[0]
        cmds.matchTransform(ctrl_finger_4_Ring,joint_Ring_4_Lt)
        cmds.select(ctrl_finger_4_Ring+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)

        ctrl_Ik_Finger_Ring = cmds.curve(n='Ctrl_IK_Ring_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                point = [(0, 1, 0),\
                         (0, 0.92388000000000003, 0.382683),\
                         (0, 0.70710700000000004, 0.70710700000000004),\
                         (0, 0.382683, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0, -0.382683, 0.92388000000000003),\
                         (0, -0.70710700000000004, 0.70710700000000004),\
                         (0, -0.92388000000000003, 0.382683),\
                         (0, -1, 0),\
                         (0, -0.92388000000000003, -0.382683),\
                         (0, -0.70710700000000004, -0.70710700000000004),\
                         (0, -0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 1, 0),\
                         (0.382683, 0.92388000000000003, 0),\
                         (0.70710700000000004, 0.70710700000000004, 0),\
                         (0.92388000000000003, 0.382683, 0),\
                         (1, 0, 0),\
                         (0.92388000000000003, -0.382683, 0),\
                         (0.70710700000000004, -0.70710700000000004, 0),\
                         (0.382683, -0.92388000000000003, 0),\
                         (0, -1, 0),\
                         (-0.382683, -0.92388000000000003, 0),\
                         (-0.70710700000000004, -0.70710700000000004, 0),\
                         (-0.92388000000000003, -0.382683, 0),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0.382683, 0),\
                         (-0.70710700000000004, 0.70710700000000004, 0),\
                         (-0.382683, 0.92388000000000003, 0),\
                         (0, 1, 0),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (-0.382683, 0, -0.92388000000000003),\
                         (-0.70710700000000004, 0, -0.70710700000000004),\
                         (-0.92388000000000003, 0, -0.382683),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0, 0.382683),\
                         (-0.70710700000000004, 0, 0.70710700000000004),\
                         (-0.382683, 0, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0.382683, 0, 0.92388000000000003),\
                         (0.70710700000000004, 0, 0.70710700000000004),\
                         (0.92388000000000003, 0, 0.382683),\
                         (1, 0, 0),\
                         (0.92388000000000003, 0, -0.382683),\
                         (0.70710700000000004, 0, -0.70710700000000004),\
                         (0.382683, 0, -0.92388000000000003),\
                         (0, 0, -1)]\
              )
        cmds.addAttr(ctrl_Ik_Finger_Ring, longName='Space', attributeType='enum', enumName="World:Hand:Head:Hip", k=True )
        cmds.setAttr(ctrl_Ik_Finger_Ring + ".Space", 1)
        cmds.matchTransform(ctrl_Ik_Finger_Ring,joint_Ring_T_Lt)
        cmds.select(ctrl_Ik_Finger_Ring+'.cv[0:52]')
        cmds.scale(0.5, 0.5, 0.5, relative=True)
        cmds.move(0, 0, 0, relative=True)
        


        curve_pole_Vector_Ring = cmds.curve(n='Crv_PV_Ring_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                point = [(-2, 0, 0),\
                         (1, 0, 1),\
                         (1, 0, -1),\
                         (-2, 0, 0),\
                         (1, 1, 0),\
                         (1, 0, 0),\
                         (1, -1, 0),\
                         (-2, 0, 0)]\
              )

        cmds.addAttr(curve_pole_Vector_Ring, longName='Guide_Visibility', attributeType='bool', dv=True, k=True )
        cmds.addAttr(curve_pole_Vector_Ring, longName='Space', attributeType='enum', enumName="World:Hand:Ik_Finger", k=True )
        cmds.setAttr(curve_pole_Vector_Ring + ".Space", 1)
        cmds.matchTransform(curve_pole_Vector_Ring,joint_Ring_3_Lt)
        cmds.select(curve_pole_Vector_Ring)
        cmds.move(0, 3, 0, relative=True, os=True)
        cmds.select(curve_pole_Vector_Ring+'.cv[0:7]')
        cmds.rotate(0, 0, 90, relative=True)
        cmds.scale(0.5, 0.5, 0.5, relative=True)

        





        ctrl_finger_Ring = [ctrl_finger_1_Ring,ctrl_finger_2_Ring,ctrl_finger_3_Ring,ctrl_finger_4_Ring,ctrl_Ik_Finger_Ring,curve_pole_Vector_Ring]
        for offset in ctrl_finger_Ring :
            cmds.select(offset)
            OFF()

        
        ctrl_finger_1_Ring_OFF = cmds.listRelatives(ctrl_finger_1_Ring, parent=True, fullPath=True)
        ctrl_finger_2_Ring_OFF = cmds.listRelatives(ctrl_finger_2_Ring, parent=True, fullPath=True)
        ctrl_finger_3_Ring_OFF = cmds.listRelatives(ctrl_finger_3_Ring, parent=True, fullPath=True)
        ctrl_finger_4_Ring_OFF = cmds.listRelatives(ctrl_finger_4_Ring, parent=True, fullPath=True)
        
        
        
        cmds.parent(ctrl_finger_4_Ring_OFF, ctrl_finger_3_Ring)
        cmds.parent(ctrl_finger_3_Ring_OFF, ctrl_finger_2_Ring)
        cmds.parent(ctrl_finger_2_Ring_OFF, ctrl_finger_1_Ring)

        cmds.parentConstraint( ctrl_finger_1_Ring, joint_Ring_1_Lt )
        cmds.parentConstraint( ctrl_finger_2_Ring, joint_Ring_2_Lt )
        cmds.parentConstraint( ctrl_finger_3_Ring, joint_Ring_3_Lt )
        cmds.parentConstraint( ctrl_finger_4_Ring, joint_Ring_4_Lt )
        


        cmds.setAttr(joint_DRV_Ring_3_Lt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Ring_4_Lt + '.preferredAngleZ', -10.0)

        ik_Handle_Ring_Lt = cmds.ikHandle(n='IKRP_Ring_Lt',  sj=joint_DRV_Ring_2_Lt, ee=joint_DRV_Ring_T_Lt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Ring_Lt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Ring_Lt[0], ctrl_Ik_Finger_Ring)
        cmds.poleVectorConstraint( curve_pole_Vector_Ring, ik_Handle_Ring_Lt[0] )
        


        new_Effector_name_Ring = 'EFF_IKRP_Ring_Lt'
        List_Input_Ik_Handle_Ring = cmds.listConnections('IKRP_Ring_Lt',s=True)
        for node in List_Input_Ik_Handle_Ring:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Ring)
                break
        
        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Ring_OFF = cmds.listRelatives(ctrl_finger_1_Ring, parent=True, fullPath=True)
        ctrl_finger_2_Ring_OFF = cmds.listRelatives(ctrl_finger_2_Ring, parent=True, fullPath=True)
        ctrl_finger_3_Ring_OFF = cmds.listRelatives(ctrl_finger_3_Ring, parent=True, fullPath=True)
        ctrl_finger_4_Ring_OFF = cmds.listRelatives(ctrl_finger_4_Ring, parent=True, fullPath=True)
        curve_pole_Vector_Ring_OFF = cmds.listRelatives(curve_pole_Vector_Ring, parent=True, fullPath=True)
        ctrl_Ik_Finger_Ring_OFF = cmds.listRelatives(ctrl_Ik_Finger_Ring, parent=True, fullPath=True)
        
        decompose_M_DRV_Ring_1_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_1_Lt')
        decompose_M_DRV_Ring_2_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_2_Lt')
        decompose_M_DRV_Ring_3_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_3_Lt')
        decompose_M_DRV_Ring_4_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_4_Lt')

        cmds.connectAttr( f'{joint_DRV_Ring_1_Lt}.xformMatrix', f'{decompose_M_DRV_Ring_1_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_2_Lt}.xformMatrix', f'{decompose_M_DRV_Ring_2_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_3_Lt}.xformMatrix', f'{decompose_M_DRV_Ring_3_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_4_Lt}.xformMatrix', f'{decompose_M_DRV_Ring_4_Lt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Ring_1_Lt}.outputTranslate', f'{ctrl_finger_1_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_2_Lt}.outputTranslate', f'{ctrl_finger_2_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_3_Lt}.outputTranslate', f'{ctrl_finger_3_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_4_Lt}.outputTranslate', f'{ctrl_finger_4_Ring_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Ring_1_Lt}.outputRotate', f'{ctrl_finger_1_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_2_Lt}.outputRotate', f'{ctrl_finger_2_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_3_Lt}.outputRotate', f'{ctrl_finger_3_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_4_Lt}.outputRotate', f'{ctrl_finger_4_Ring_OFF[0]}.rotate' )


        cmds.select(deselect=True)
        joint_Ring_knuckle = cmds.joint( n='Sk_Ring_Knuckle_Lt' , rad=0.75)
        cmds.matchTransform(joint_Ring_knuckle,joint_Ring_2_Lt)
        cmds.parent(joint_Ring_knuckle, joint_Ring_2_Lt )
        

        

        multiply_divide_value_tendon_Ring = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Ring_Lt')
        multiply_divide_lower_intensity_knuckle_tendon_Ring = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Ring_Lt')
        multiply_divide_intensity_knuckle_tendon_Ring = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Ring_Lt')
        condition_positive_tendon_Ring = cmds.createNode( 'condition', n='condition_positive_tendon_Ring_Lt')

        cmds.setAttr(multiply_divide_value_tendon_Ring + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Ring + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Ring + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Ring + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Ring + '.operation', 2)

        cmds.connectAttr( f'{joint_Ring_2_Lt}.rotateZ', f'{condition_positive_tendon_Ring}.firstTerm' )
        cmds.connectAttr( f'{joint_Ring_2_Lt}.rotateZ', f'{multiply_divide_value_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{joint_Ring_2_Lt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Ring}.outColorR', f'{multiply_divide_value_tendon_Ring}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Ring}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Ring}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputY', f'{joint_Ring_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_1_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_1_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_2_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_2_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_3_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_3_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_4_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_4_Lt}.translateZ' )

        
    
        cmds.connectAttr( f'{controler_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2Y' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2X' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2Z' )

        cmds.select(deselect=True)
        ctrls_Ring_to_goup = [ctrl_Ik_Finger_Ring_OFF[0], curve_pole_Vector_Ring_OFF[0], ctrl_finger_1_Ring_OFF[0]]
        group_ctrls_Ring_Lt = cmds.group(em=True, name='Grp_Ctrls_Ring_Lt')
        cmds.parent(ctrls_Ring_to_goup, group_ctrls_Ring_Lt)

        
        joint_Ring_to_goup = [joint_Ring_1_Lt, joint_DRV_Ring_1_Lt ]
        group_joints_Ring_Lt = cmds.group(em=True, name='Grp_Sk_Ring_Lt')
        cmds.parent(joint_Ring_to_goup, group_joints_Ring_Lt)







        #guide visual pv 
        locator_pv_start_Ring_ctrl_Lt = cmds.spaceLocator(n='LOC_Start_Guide_PV_Ring_Lt', p=(0, 0, 0), )
        cmds.matchTransform(locator_pv_start_Ring_ctrl_Lt, joint_Ring_3_Lt)
        cmds.setAttr(locator_pv_start_Ring_ctrl_Lt[0] + '.visibility', 0 )
        locator_pv_end_Ring_ctrl_Lt = cmds.spaceLocator( n='LOC_End_Guide_PV_Ring_Lt', p=(0, 0, 0)  )
        cmds.matchTransform(locator_pv_end_Ring_ctrl_Lt, curve_pole_Vector_Ring)
        cmds.setAttr(locator_pv_end_Ring_ctrl_Lt[0] + '.visibility', 0 )

        locator_pv_start_Ring_ctrl_Lt_position = cmds.xform(locator_pv_start_Ring_ctrl_Lt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Ring_ctrl_Lt_position = cmds.xform(locator_pv_end_Ring_ctrl_Lt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Ring_ctrl_Lt = cmds.curve(d=1, p=[locator_pv_start_Ring_ctrl_Lt_position, locator_pv_end_Ring_ctrl_Lt_position], n='Guide_PV_Ring_Lt')

        decompose_M_curve_start_Ring_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Ring_Lt')
        decompose_M_curve_end_Ring_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Ring_Lt')


           
        cmds.connectAttr( f'{locator_pv_start_Ring_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_start_Ring_Lt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Ring_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_end_Ring_Lt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Ring_Lt}.outputTranslate', f'{curve_pv_Ring_ctrl_Lt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Ring_Lt}.outputTranslate', f'{curve_pv_Ring_ctrl_Lt}.controlPoints[1]' )

        cmds.parent(locator_pv_end_Ring_ctrl_Lt, curve_pole_Vector_Ring)
        cmds.parent(locator_pv_start_Ring_ctrl_Lt, joint_Ring_3_Lt)

        cmds.setAttr(curve_pv_Ring_ctrl_Lt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Guide_Visibility', f'{curve_pv_Ring_ctrl_Lt}.visibility' )
        

        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Ring_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Ring_Lt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Ring_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Ring_Lt', p=(0, 0, 0), )
        print(locator_Finger_FingerSpace_PV_Ring_ctrl_Lt)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Ring_ctrl_Lt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Ring_ctrl_Lt[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Ring_ctrl_Lt, curve_pole_Vector_Ring)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Ring_ctrl_Lt, curve_pole_Vector_Ring)

        hold_matrix_Ring_PV_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Ring_Lt')
        mult_Finger_FingerSpace_PV_Ring_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Ring_Lt')
        mult_Finger_HandSpace_PV_Ring_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Ring_Lt')
        condition_Finger_Space_PV_Ring_Lt = cmds.createNode( 'condition', n='Cond_Space_Ring_PV_Lt')
        condition_Finger_FingerSpace_PV_Ring_Lt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Ring_Lt')
        condition_Finger_HandSpace_PV_Ring_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Ring_Lt')

        blend_matrix_PV_Ring_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Ring_Lt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_PV_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_PV_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Ring_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Ring_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Ring_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Ring_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Ring_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_PV_Ring_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Ring_Lt}.matrixSum', f'{blend_matrix_PV_Ring_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Ring_Lt}.matrixSum', f'{blend_matrix_PV_Ring_Lt}.target[0].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_FingerSpace_PV_Ring_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_HandSpace_PV_Ring_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_Space_PV_Ring_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Ring_Lt}.outColorR', f'{condition_Finger_Space_PV_Ring_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Ring_Lt}.outColorR', f'{condition_Finger_Space_PV_Ring_Lt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Ring_Lt}.outColorR', f'{blend_matrix_PV_Ring_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Ring_Lt}.outColorG', f'{blend_matrix_PV_Ring_Lt}.target[1].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Ring_Lt}.outputMatrix', f'{curve_pole_Vector_Ring}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Ring_ctrl_Lt, ctrl_Ik_Finger_Ring) #et on parente direct le locator de l'ik 


        #Space controller IK a 4 choix

        locator_Finger_HandSpace_IK_Ring_ctrl = cmds.spaceLocator(n='LOC_Finger_HandSpace_IK_Ring_Lt', p=(0, 0, 0), )
        locator_Finger_HeadSpace_IK_Ring_ctrl = cmds.spaceLocator(n='LOC_Finger_HeadSpace_IK_Ring_Lt', p=(0, 0, 0), )
        locator_Finger_HipSpace_IK_Ring_ctrl = cmds.spaceLocator(n='LOC_Finger_HipSpace_IK_Ring_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_HandSpace_IK_Ring_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HeadSpace_IK_Ring_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HipSpace_IK_Ring_ctrl[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_HandSpace_IK_Ring_ctrl,ctrl_Ik_Finger_Ring)
        cmds.matchTransform(locator_Finger_HeadSpace_IK_Ring_ctrl,ctrl_Ik_Finger_Ring)
        cmds.matchTransform(locator_Finger_HipSpace_IK_Ring_ctrl,ctrl_Ik_Finger_Ring)

        hold_matrix_Ring_IK_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Ring_Lt')
        mult_Finger_HandSpace_IK_Ring_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Ring_Lt')
        mult_Finger_HeadSpace_IK_Ring_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Ring_Lt')
        mult_Finger_HipSpace_IK_Ring_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Ring_Lt')
        condition_Finger_Space_IK_Ring_Lt = cmds.createNode( 'condition', n='Cond_Space_Ring_Lt')
        condition_Finger_HandSpace_IK_Ring_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_Ring_Lt')
        condition_Finger_HeadSpace_IK_Ring_Lt = cmds.createNode( 'condition', n='Cond_HeadSpace_Ring_Lt')
        condition_Finger_HipSpace_IK_Ring_Lt = cmds.createNode( 'condition', n='Cond_HipSpace_Ring_Lt')

        blend_matrix_IK_Ring_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Ring_Lt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Lt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_IK_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_IK_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Ring_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Ring_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Ring_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Ring_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Ring_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_IK_Ring_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Ring_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HipSpace_IK_Ring_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Ring_Lt}.matrixSum', f'{blend_matrix_IK_Ring_Lt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Ring_Lt}.matrixSum', f'{blend_matrix_IK_Ring_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Ring_Lt}.matrixSum', f'{blend_matrix_IK_Ring_Lt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HandSpace_IK_Ring_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HeadSpace_IK_Ring_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HipSpace_IK_Ring_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_Space_IK_Ring_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Ring_Lt}.outColorR', f'{condition_Finger_Space_IK_Ring_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Ring_Lt}.outColorR', f'{condition_Finger_Space_IK_Ring_Lt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Ring_Lt}.outColorR', f'{condition_Finger_Space_IK_Ring_Lt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Lt}.outColorR', f'{blend_matrix_IK_Ring_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Lt}.outColorG', f'{blend_matrix_IK_Ring_Lt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Lt}.outColorB', f'{blend_matrix_IK_Ring_Lt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Ring_Lt}.outputMatrix', f'{ctrl_Ik_Finger_Ring}.offsetParentMatrix' )


            #on range les locator space dans les bon endroit

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Lt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Ring_ctrl[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Ring_ctrl[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Ring_ctrl[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Ring_ctrl_Lt[0], sk_Hand)
            
            
        else :
            group_miror_Ring_Loc_Space_IK_temp_Lt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Ring_A_PARENTER_Lt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Ring_ctrl[0], locator_Finger_HeadSpace_IK_Ring_ctrl[0], locator_Finger_HipSpace_IK_Ring_ctrl[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Ring_Loc_Space_IK_temp_Lt)



        cmds.select(deselect=True)
        list_set_skin_jnt = [joint_Ring_1_Lt, joint_Ring_2_Lt, joint_Ring_3_Lt, joint_Ring_4_Lt, joint_Ring_Tendon_1_Lt, joint_Ring_Tendon_2_Lt, joint_Ring_Tendon_3_Lt, joint_Ring_Tendon_4_Lt, joint_Ring_knuckle]
        set_name = "MySetJointSkin"
        if cmds.objExists(set_name):
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)
        
        else:
            cmds.sets(n=set_name)
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)




        #rangement dans les groupes


        grp_Controllers = 'Grp_Controllers'
        grp_Skeleton = 'Grp_Skeleton'
        grp_DO_NOT_TOUCH = 'DO_NOT_TOUCH'
        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'


        if not cmds.objExists('Grp_DNT_Hand_Lt'):
            grp_DNT_Hand_Lt = cmds.group(em=True, name='Grp_DNT_Hand_Lt')


        grp_elem_DNT_Ring = [curve_pv_Ring_ctrl_Lt]

        cmds.parent(grp_elem_DNT_Ring, grp_DNT_Hand_Lt )


        if cmds.objExists(grp_Controllers):
            cmds.parent(group_ctrls_Ring_Lt, grp_Controllers)
        else:
            grp_Controllers = cmds.group(em=True, name='Grp_Controllers')
            cmds.parent(group_ctrls_Ring_Lt, grp_Controllers)


        if cmds.objExists(grp_Skeleton):
            cmds.parent(group_joints_Ring_Lt, grp_Skeleton)
        else:
            grp_Skeleton = cmds.group(em=True, name='Grp_Skeleton')
            cmds.parent(group_joints_Ring_Lt, grp_Skeleton)


        if cmds.objExists(grp_DO_NOT_TOUCH):
            if cmds.objExists('Grp_DNT_Hand_Lt'):
                parent_of_grp_DNT_Hand_Lt = cmds.listRelatives(grp_DNT_Hand_Lt, parent=True)
                if not parent_of_grp_DNT_Hand_Lt:
                    cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)
        else:
            grp_DO_NOT_TOUCH = cmds.group(em=True, name='DO_NOT_TOUCH')
            cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)


        ###


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{controler_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Ring}.visibility' )     

        #on fait la parentée pour que les mains suivent la structure generale

        DRV_Palm_IK_Lt = "DRV_Palm_IK_Lt"
        if cmds.objExists(DRV_Palm_IK_Lt):
            cmds.parentConstraint(DRV_Palm_IK_Lt, joint_DRV_Ring_1_Lt, mo=True)

        #couleurs des controllers 
        jnt_color_Blue = [ctrl_finger_1_Ring, ctrl_finger_2_Ring, ctrl_finger_3_Ring, ctrl_finger_4_Ring, ctrl_Ik_Finger_Ring]
        jnt_color_DarkBlue = [ctrl_finger_3_Ring, ctrl_finger_4_Ring]
        jnt_color_beige= [curve_pole_Vector_Ring]
        

        for objcolor_Blue in jnt_color_Blue : 
            cmds.setAttr(objcolor_Blue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Blue + '.overrideColor', 6)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 5)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21) 

    def ring_rig_Part_3_Miror(*args):

        duplication_group_ctrls_sk = cmds.duplicate(group_ctrls_Ring_Lt,group_joints_Ring_Lt, rc=True)
        

        for Delnode in duplication_group_ctrls_sk: 
            string_del = ['EFF', 'Constraint', 'IKRP_Ring_Lt', 'LOC_Finger_FingerSpace_PV_Ring_Lt1']
            for substring in string_del:
                if Delnode.find(substring) != -1 and cmds.objExists(Delnode):
                    cmds.delete(Delnode)


             
        
        for rename in duplication_group_ctrls_sk:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        group_ctrls_Ring_Rt = 'Grp_Ctrls_Ring_Rt'
        group_joints_Ring_Rt = 'Grp_Sk_Ring_Rt'
        # group_miror_Ring_Loc_Space_IK_temp_Rt = 'Grp_LOC_Space_Ik_Finger_Ring_A_PARENTER_Rt'
        
    
        cmds.setAttr(group_ctrls_Ring_Rt + '.scaleX', -1 )
        cmds.setAttr(group_joints_Ring_Rt + '.scaleX', -1 )
        # cmds.setAttr(group_miror_Ring_Loc_Space_IK_temp_Rt + '.scaleX', -1 )


        #réassignation des varables pour le miror
        ctrl_finger_1_Ring = 'Ctrl_Finger_1_Ring_Rt'
        ctrl_finger_2_Ring = 'Ctrl_Finger_2_Ring_Rt'
        ctrl_finger_3_Ring = 'Ctrl_Finger_3_Ring_Rt'
        ctrl_finger_4_Ring = 'Ctrl_Finger_4_Ring_Rt'
        curve_pole_Vector_Ring = 'Crv_PV_Ring_Rt'
        ctrl_Ik_Finger_Ring = 'Ctrl_IK_Ring_Rt'

        joint_DRV_Ring_1_Rt = 'DRV_Ring_1_Rt'
        joint_DRV_Ring_2_Rt = 'DRV_Ring_2_Rt'
        joint_DRV_Ring_3_Rt = 'DRV_Ring_3_Rt'
        joint_DRV_Ring_4_Rt = 'DRV_Ring_4_Rt'
        joint_DRV_Ring_T_Rt = 'DRV_Ring_T_Rt'
        joint_Ring_1_Rt = 'Sk_Ring_1_Rt'
        joint_Ring_2_Rt = 'Sk_Ring_2_Rt'
        joint_Ring_3_Rt = 'Sk_Ring_3_Rt'
        joint_Ring_4_Rt = 'Sk_Ring_4_Rt'
        joint_Ring_T_Rt = 'Sk_Ring_T_Rt'
        joint_Ring_Tendon_1_Rt = 'Sk_Ring_Tendon_1_Rt'
        joint_Ring_Tendon_2_Rt = 'Sk_Ring_Tendon_2_Rt'
        joint_Ring_Tendon_3_Rt = 'Sk_Ring_Tendon_3_Rt'
        joint_Ring_Tendon_4_Rt = 'Sk_Ring_Tendon_4_Rt'
        joint_Ring_knuckle = 'Sk_Ring_Knuckle_Rt'

        duplication_ctrl_hand_control = 'Ctrl_Control_Hand_Rt'
        locator_pv_start_Ring_ctrl_Rt = 'LOC_Start_Guide_PV_Ring_Rt'
        locator_pv_end_Ring_ctrl_Rt = 'LOC_End_Guide_PV_Ring_Rt'
   


        '''
        duplication du code au dessus qui suit

        '''

        



        cmds.parentConstraint( ctrl_finger_1_Ring, joint_Ring_1_Rt )
        cmds.parentConstraint( ctrl_finger_2_Ring, joint_Ring_2_Rt )
        cmds.parentConstraint( ctrl_finger_3_Ring, joint_Ring_3_Rt )
        cmds.parentConstraint( ctrl_finger_4_Ring, joint_Ring_4_Rt )
        


        cmds.setAttr(joint_DRV_Ring_3_Rt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Ring_4_Rt + '.preferredAngleZ', -10.0)

        ik_Handle_Ring_Rt = cmds.ikHandle(n='IKRP_Ring_Rt',  sj=joint_DRV_Ring_2_Rt, ee=joint_DRV_Ring_T_Rt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Ring_Rt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Ring_Rt[0], ctrl_Ik_Finger_Ring)
        cmds.poleVectorConstraint( curve_pole_Vector_Ring, ik_Handle_Ring_Rt[0] )


        new_Effector_name_Ring = 'EFF_IKRP_Ring_Rt'
        List_Input_Ik_Handle_Ring = cmds.listConnections('IKRP_Ring_Rt',s=True)
        for node in List_Input_Ik_Handle_Ring:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Ring)
                break
        

        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Ring_OFF = cmds.listRelatives(ctrl_finger_1_Ring, parent=True, fullPath=True)
        ctrl_finger_2_Ring_OFF = cmds.listRelatives(ctrl_finger_2_Ring, parent=True, fullPath=True)
        ctrl_finger_3_Ring_OFF = cmds.listRelatives(ctrl_finger_3_Ring, parent=True, fullPath=True)
        ctrl_finger_4_Ring_OFF = cmds.listRelatives(ctrl_finger_4_Ring, parent=True, fullPath=True)
        curve_pole_Vector_Ring_OFF = cmds.listRelatives(curve_pole_Vector_Ring, parent=True, fullPath=True)
        ctrl_Ik_Finger_Ring_OFF = cmds.listRelatives(ctrl_Ik_Finger_Ring, parent=True, fullPath=True)
        
        decompose_M_DRV_Ring_1_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_1_Rt')
        decompose_M_DRV_Ring_2_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_2_Rt')
        decompose_M_DRV_Ring_3_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_3_Rt')
        decompose_M_DRV_Ring_4_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Ring_4_Rt')

        cmds.connectAttr( f'{joint_DRV_Ring_1_Rt}.xformMatrix', f'{decompose_M_DRV_Ring_1_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_2_Rt}.xformMatrix', f'{decompose_M_DRV_Ring_2_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_3_Rt}.xformMatrix', f'{decompose_M_DRV_Ring_3_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Ring_4_Rt}.xformMatrix', f'{decompose_M_DRV_Ring_4_Rt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Ring_1_Rt}.outputTranslate', f'{ctrl_finger_1_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_2_Rt}.outputTranslate', f'{ctrl_finger_2_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_3_Rt}.outputTranslate', f'{ctrl_finger_3_Ring_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_4_Rt}.outputTranslate', f'{ctrl_finger_4_Ring_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Ring_1_Rt}.outputRotate', f'{ctrl_finger_1_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_2_Rt}.outputRotate', f'{ctrl_finger_2_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_3_Rt}.outputRotate', f'{ctrl_finger_3_Ring_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Ring_4_Rt}.outputRotate', f'{ctrl_finger_4_Ring_OFF[0]}.rotate' )

        #plus besoin deja crée
        # joint_Ring_knuckle = cmds.joint( p=(position_joint_DRV_Ring_2_Rt), n='Sk_Ring_Knuckle_Rt' , rad=0.75)
        # cmds.parent(joint_Ring_knuckle, joint_Ring_2_Rt )
        

        multiply_divide_value_tendon_Ring = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Ring_Rt')
        multiply_divide_lower_intensity_knuckle_tendon_Ring = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Ring_Rt')
        multiply_divide_intensity_knuckle_tendon_Ring = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Ring_Rt')
        condition_positive_tendon_Ring = cmds.createNode( 'condition', n='condition_positive_tendon_Ring_Rt')

        cmds.setAttr(multiply_divide_value_tendon_Ring + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Ring + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Ring + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Ring + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Ring + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Ring + '.operation', 2)

        cmds.connectAttr( f'{joint_Ring_2_Rt}.rotateZ', f'{condition_positive_tendon_Ring}.firstTerm' )
        cmds.connectAttr( f'{joint_Ring_2_Rt}.rotateZ', f'{multiply_divide_value_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{joint_Ring_2_Rt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Ring}.outColorR', f'{multiply_divide_value_tendon_Ring}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Ring}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Ring}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Ring}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputY', f'{joint_Ring_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_1_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_1_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_2_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_2_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_3_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_3_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputX', f'{joint_Ring_Tendon_4_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Ring}.outputZ', f'{joint_Ring_Tendon_4_Rt}.translateZ' )

        
    
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2Y' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2X' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Ring}.input2Z' )

        cmds.select(deselect=True)

        

        #miror
        locator_pv_start_Ring_ctrl_Rt_position = cmds.xform(locator_pv_start_Ring_ctrl_Rt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Ring_ctrl_Rt_position = cmds.xform(locator_pv_end_Ring_ctrl_Rt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Ring_ctrl_Rt = cmds.curve(d=1, p=[locator_pv_start_Ring_ctrl_Rt_position, locator_pv_end_Ring_ctrl_Rt_position], n='Guide_PV_Ring_Rt')

        decompose_M_curve_start_Ring_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Ring_Rt')
        decompose_M_curve_end_Ring_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Ring_Rt')

        
        #pas besoin
        # listShapes = cmds.listRelatives(curve_pv_Ring_ctrl_Rt, allDescendents=True, type='shape')
        # curve_pv_Ring_ctrl_Rt_shape = listShapes[0]
        # print(curve_pv_Ring_ctrl_Rt_shape)
           
        cmds.connectAttr( f'{locator_pv_start_Ring_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_start_Ring_Rt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Ring_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_end_Ring_Rt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Ring_Rt}.outputTranslate', f'{curve_pv_Ring_ctrl_Rt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Ring_Rt}.outputTranslate', f'{curve_pv_Ring_ctrl_Rt}.controlPoints[1]' )

        

        cmds.setAttr(curve_pv_Ring_ctrl_Rt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Guide_Visibility', f'{curve_pv_Ring_ctrl_Rt}.visibility' )



        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Ring_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Ring_Rt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Ring_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Ring_Rt', p=(0, 0, 0))
        cmds.parent(locator_Finger_FingerSpace_PV_Ring_ctrl_Rt, curve_pole_Vector_Ring )
        cmds.parent(locator_Finger_HandSpace_PV_Ring_ctrl_Rt, curve_pole_Vector_Ring )
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Ring_ctrl_Rt, curve_pole_Vector_Ring)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Ring_ctrl_Rt, curve_pole_Vector_Ring)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Ring_ctrl_Rt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Ring_ctrl_Rt[0] + '.visibility', 0)
        

        hold_matrix_Ring_PV_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Ring_Rt')
        mult_Finger_FingerSpace_PV_Ring_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Ring_Rt')
        mult_Finger_HandSpace_PV_Ring_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Ring_Rt')
        condition_Finger_Space_PV_Ring_Rt = cmds.createNode( 'condition', n='Cond_Space_Ring_PV_Rt')
        condition_Finger_FingerSpace_PV_Ring_Rt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Ring_Rt')
        condition_Finger_HandSpace_PV_Ring_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Ring_Rt')

        blend_matrix_PV_Ring_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Ring_Rt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Ring_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Ring_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_PV_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Ring_PV_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Ring_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Ring_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Ring_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Ring_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Ring_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Ring_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_PV_Ring_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Ring_Rt}.matrixSum', f'{blend_matrix_PV_Ring_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Ring_Rt}.matrixSum', f'{blend_matrix_PV_Ring_Rt}.target[1].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_FingerSpace_PV_Ring_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_HandSpace_PV_Ring_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Ring}.Space', f'{condition_Finger_Space_PV_Ring_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Ring_Rt}.outColorR', f'{condition_Finger_Space_PV_Ring_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Ring_Rt}.outColorR', f'{condition_Finger_Space_PV_Ring_Rt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Ring_Rt}.outColorR', f'{blend_matrix_PV_Ring_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Ring_Rt}.outColorG', f'{blend_matrix_PV_Ring_Rt}.target[0].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Ring_Rt}.outputMatrix', f'{curve_pole_Vector_Ring}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Ring_ctrl_Rt, ctrl_Ik_Finger_Ring) #et on parente direct le locator de l'ik 





                #Space controller IK a 4 choix MIROR    
        

        # le coté rt ne marche pas avec ça donc il faut venir faire une duplication des anciens locators
            #on vient recuperer les anciens locators
        list_locator_RingSpace_dup = [locator_Finger_HipSpace_IK_Ring_ctrl  , locator_Finger_HeadSpace_IK_Ring_ctrl ,   locator_Finger_HandSpace_IK_Ring_ctrl ]

            #on cree une nouvelle liste qui va aceuillir nos nouveaux locators
        new_list_locator_RingSpace_dup = []
        for elem in list_locator_RingSpace_dup:
            duplication_group_loc_space = cmds.duplicate(elem,  rc=True)
            new_list_locator_RingSpace_dup.append(duplication_group_loc_space)

            #on cree le grp temporaire qui va scale -1
        group_miror_locators_RingSpace = cmds.group(empty=True, n='Grp_Temp_miror_Loc_Ring_Rt')

            

            #on parente les nouveaux elements de la nouvelle liste au grp  et ensuite on scale le groupe pour miror
        for elem in new_list_locator_RingSpace_dup :
            cmds.parent(elem, group_miror_locators_RingSpace)

        cmds.setAttr(group_miror_locators_RingSpace + ".scaleX", -1)

            #on vient faire une list relative pour identifier les enfants et pas que ça poe de probleme pour le rename 
        group_miror_locators_RingSpace_children = cmds.listRelatives(group_miror_locators_RingSpace, c=True)

            #on vient les renommer en rt
        for rename in group_miror_locators_RingSpace_children:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        locator_Finger_HandSpace_IK_Ring_ctrl_Rt = 'LOC_Finger_HandSpace_IK_Ring_Rt'
        locator_Finger_HeadSpace_IK_Ring_ctrl_Rt = 'LOC_Finger_HeadSpace_IK_Ring_Rt'
        locator_Finger_HipSpace_IK_Ring_ctrl_Rt = 'LOC_Finger_HipSpace_IK_Ring_Rt'

        
        cmds.select(locator_Finger_HandSpace_IK_Ring_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HeadSpace_IK_Ring_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HipSpace_IK_Ring_ctrl_Rt)                #chepa pk la loop marche pas et fait une erreur dans le namespace des off et arrete le script
        OFF()
        

        

        locator_Finger_HandSpace_IK_Ring_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HandSpace_IK_Ring_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HeadSpace_IK_Ring_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HeadSpace_IK_Ring_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HipSpace_IK_Ring_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HipSpace_IK_Ring_ctrl_Rt, parent=True, fullPath=True)
        


        hold_matrix_Ring_IK_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Ring_Rt')
        mult_Finger_HandSpace_IK_Ring_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Ring_Rt')
        mult_Finger_HeadSpace_IK_Ring_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Ring_Rt')
        mult_Finger_HipSpace_IK_Ring_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Ring_Rt')
        condition_Finger_Space_IK_Ring_Rt = cmds.createNode( 'condition', n='Cond_Space_Ring_Rt')
        condition_Finger_HandSpace_IK_Ring_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_Ring_Rt')
        condition_Finger_HeadSpace_IK_Ring_Rt = cmds.createNode( 'condition', n='Cond_HeadSpace_Ring_Rt')
        condition_Finger_HipSpace_IK_Ring_Rt = cmds.createNode( 'condition', n='Cond_HipSpace_Ring_Rt')

        blend_matrix_IK_Ring_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Ring_Rt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Rt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Ring_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Ring_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Ring_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Ring_IK_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Ring_IK_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Ring_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Ring_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Ring_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Ring_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Ring_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Ring_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_IK_Ring_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Ring_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Ring_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HipSpace_IK_Ring_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Ring_Rt}.matrixSum', f'{blend_matrix_IK_Ring_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Ring_Rt}.matrixSum', f'{blend_matrix_IK_Ring_Rt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Ring_Rt}.matrixSum', f'{blend_matrix_IK_Ring_Rt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HandSpace_IK_Ring_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HeadSpace_IK_Ring_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_HipSpace_IK_Ring_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Ring}.Space', f'{condition_Finger_Space_IK_Ring_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Ring_Rt}.outColorR', f'{condition_Finger_Space_IK_Ring_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Ring_Rt}.outColorR', f'{condition_Finger_Space_IK_Ring_Rt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Ring_Rt}.outColorR', f'{condition_Finger_Space_IK_Ring_Rt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Rt}.outColorR', f'{blend_matrix_IK_Ring_Rt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Rt}.outColorG', f'{blend_matrix_IK_Ring_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Ring_Rt}.outColorB', f'{blend_matrix_IK_Ring_Rt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Ring_Rt}.outputMatrix', f'{ctrl_Ik_Finger_Ring}.offsetParentMatrix' )  


            #on parente les locators

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Rt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Ring_ctrl_Rt_OFF[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Ring_ctrl_Rt_OFF[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Ring_ctrl_Rt_OFF[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Ring_ctrl_Rt[0], sk_Hand)
            
            
        else :
            group_miror_Ring_Loc_Space_IK_temp_Rt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Ring_A_PARENTER_Rt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Ring_ctrl_Rt_OFF[0], locator_Finger_HeadSpace_IK_Ring_ctrl_Rt_OFF[0], locator_Finger_HipSpace_IK_Ring_ctrl_Rt_OFF[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Ring_Loc_Space_IK_temp_Rt)
            cmds.select(deselect=True)   

        #apres ça on supprime le grp scale -1 des locators 
        cmds.delete(group_miror_locators_RingSpace)


        #parenter les crv guides 

        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'
        cmds.parent(curve_pv_Ring_ctrl_Rt, grp_DNT_Hand_Lt)


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Ring}.visibility' ) 


        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Rt = "DRV_Palm_IK_Rt"
        if cmds.objExists(DRV_Palm_IK_Rt):
            cmds.parentConstraint(DRV_Palm_IK_Rt, joint_DRV_Ring_1_Rt, mo=True)      


        
        #couleurs des controllers 
        jnt_color_Red = [ctrl_finger_1_Ring, ctrl_finger_2_Ring, ctrl_finger_3_Ring, ctrl_finger_4_Ring, ctrl_Ik_Finger_Ring]
        jnt_color_DarkBlue = [ctrl_finger_3_Ring, ctrl_finger_4_Ring]
        jnt_color_beige= [curve_pole_Vector_Ring]
        

        for objcolor_Red in jnt_color_Red : 
            cmds.setAttr(objcolor_Red + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Red + '.overrideColor', 13)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 18)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def ring_rig_Suppr(*args): 
        
        ring_finger_to_suppr = ['Grp_Ctrls_Ring_Lt', 'Grp_Sk_Ring_Lt','Guide_PV_Ring_Lt', 'Grp_LOC_Space_Ik_Finger_Ring_A_PARENTER_Lt', 'Grp_Ctrls_Ring_Rt', 'Grp_Sk_Ring_Rt','Guide_PV_Ring_Rt', 'Grp_LOC_Space_Ik_Finger_Ring_A_PARENTER_Rt']
        identify_ring_finger_to_suppr = cmds.listRelatives(ring_finger_to_suppr, ad=True)
        list_suppr = [ring_finger_to_suppr]

        for i in range(100):
            list_suppr.append(identify_ring_finger_to_suppr)
            identify_ring_finger_to_suppr = cmds.listConnections(identify_ring_finger_to_suppr, d=True, s=True)
            
            if not identify_ring_finger_to_suppr:
                break

        list_suppr_2 = []
        list_Not_Suppr_ring = ['defaultRenderUtilityList', 'MayaNodeEditorSavedTabsInfo', 'Ctrl_Control_Hand', 'Index', 'Middle', 'Pinky', 'Thumb','bindPose','ikRPsolver','ikSCsolver','hikSolver', 'ikSplineSolver','ikSystem','MySetJointSkin']

        for elem in list_suppr:
            for node in elem:
                skip_node = False

                for ring_name in list_Not_Suppr_ring:
                    if ring_name in node:
                        skip_node = True
                        break

                if not skip_node:
                    list_suppr_2.append(node)

        cmds.delete(list_suppr_2) 
###
    
    def pinky_rig_Part_1(*args):
        
        global joint_DRV_Pinky_1_Lt
        global joint_DRV_Pinky_2_Lt
        global joint_DRV_Pinky_3_Lt
        global joint_DRV_Pinky_4_Lt
        global joint_DRV_Pinky_T_Lt
        global curve_MP_Pinky_Lt
        global joint_DRV_Pinky_3_OFF_Lt
        global joint_DRV_Pinky_4_OFF_Lt
        
        global joint_Pinky_Tendon_1_Lt
        global joint_Pinky_Tendon_2_Lt
        global joint_Pinky_Tendon_3_Lt
        global joint_Pinky_Tendon_4_Lt
        global curve_MP_Pinky_Tendon_Lt
        global joint_Pinky_Tendon_OFF_1_Lt
        global joint_Pinky_Tendon_OFF_2_Lt
        global joint_Pinky_Tendon_OFF_3_Lt
        global joint_Pinky_Tendon_OFF_4_Lt
        global loc_Pinky_orientaton_joints_Lt
        global loc_Pinky_orientaton_joints_Lt_grp
        
        


        cmds.select(deselect=True)
        joint_DRV_Pinky_1_Lt = cmds.joint(n='DRV_Pinky_1_Lt', p=(55,104, -9))
        joint_DRV_Pinky_2_Lt = cmds.joint(n='DRV_Pinky_2_Lt', p=(58.5, 99, -10.5))
        joint_DRV_Pinky_3_Lt = cmds.joint(n='DRV_Pinky_3_Lt', p=(5, 0, 5))
        joint_DRV_Pinky_4_Lt = cmds.joint(n='DRV_Pinky_4_Lt', p=(10, 0, 5))
        joint_DRV_Pinky_T_Lt = cmds.joint(n='DRV_Pinky_T_Lt', p=(62.5, 93, -11.5), rad=0.5)

        cmds.parent(joint_DRV_Pinky_T_Lt, world=True)
        cmds.parent(joint_DRV_Pinky_4_Lt, world=True)
        cmds.parent(joint_DRV_Pinky_3_Lt, world=True)
        cmds.parent(joint_DRV_Pinky_2_Lt, world=True)
        
       
        
        joint_Pinky_Tendon_1_Lt = cmds.joint(n='Sk_Pinky_Tendon_1_Lt', p=(-8, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Pinky_Tendon_2_Lt = cmds.joint(n='Sk_Pinky_Tendon_2_Lt', p=(-6, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Pinky_Tendon_3_Lt = cmds.joint(n='Sk_Pinky_Tendon_3_Lt', p=(-4, 0, 5), rad=0.2)
        cmds.select(deselect=True)
        joint_Pinky_Tendon_4_Lt = cmds.joint(n='Sk_Pinky_Tendon_4_Lt', p=(-2, 0, 5), rad=0.2)


        jnt_finger_Pinky = [joint_DRV_Pinky_3_Lt,joint_DRV_Pinky_4_Lt,joint_Pinky_Tendon_1_Lt,joint_Pinky_Tendon_2_Lt,joint_Pinky_Tendon_3_Lt,joint_Pinky_Tendon_4_Lt]
        for offset in jnt_finger_Pinky :
            cmds.select(offset)
            OFF()


        joint_DRV_Pinky_3_OFF_Lt = cmds.listRelatives(joint_DRV_Pinky_3_Lt, parent=True, fullPath=True)        
        joint_DRV_Pinky_4_OFF_Lt = cmds.listRelatives(joint_DRV_Pinky_4_Lt, parent=True, fullPath=True)

        joint_Pinky_Tendon_OFF_1_Lt = cmds.listRelatives(joint_Pinky_Tendon_1_Lt, parent=True, fullPath=True)
        joint_Pinky_Tendon_OFF_2_Lt = cmds.listRelatives(joint_Pinky_Tendon_2_Lt, parent=True, fullPath=True)
        joint_Pinky_Tendon_OFF_3_Lt = cmds.listRelatives(joint_Pinky_Tendon_3_Lt, parent=True, fullPath=True)
        joint_Pinky_Tendon_OFF_4_Lt = cmds.listRelatives(joint_Pinky_Tendon_4_Lt, parent=True, fullPath=True)



        jnt_0_Crv_Position_Pinky = cmds.xform(joint_DRV_Pinky_1_Lt, query=True, worldSpace=True, translation=True)
        jnt_1_Crv_Position_Pinky = cmds.xform(joint_DRV_Pinky_2_Lt, query=True, worldSpace=True, translation=True)
        jnt_2_Crv_Position_Pinky = cmds.xform(joint_DRV_Pinky_T_Lt, query=True, worldSpace=True, translation=True)
        joint_Skin_Crv_Pinky_1_Lt = [joint_DRV_Pinky_2_Lt , joint_DRV_Pinky_T_Lt]
        joint_Skin_Crv_Pinky_2_Lt = [joint_DRV_Pinky_1_Lt ,joint_DRV_Pinky_2_Lt]

        curve_MP_Pinky_Lt = cmds.curve(d=1, p=[jnt_1_Crv_Position_Pinky, jnt_2_Crv_Position_Pinky], n='Crv_MP_Pinky_Lt_Temp')
        curve_MP_Pinky_Tendon_Lt = cmds.curve(d=1, p=[jnt_0_Crv_Position_Pinky, jnt_1_Crv_Position_Pinky], n='Crv_MP_Pinky_Tendon_Lt_Temp')

        bind_skin_cluster_Pinky = cmds.skinCluster(joint_Skin_Crv_Pinky_1_Lt, curve_MP_Pinky_Lt, tsb=True)
        bind_skin_cluster_tendon_Pinky = cmds.skinCluster(joint_Skin_Crv_Pinky_2_Lt, curve_MP_Pinky_Tendon_Lt, tsb=True)



        cmds.pathAnimation( joint_DRV_Pinky_3_OFF_Lt, c=curve_MP_Pinky_Lt, su=0.3333, follow=True)
        cmds.pathAnimation( joint_DRV_Pinky_4_OFF_Lt, c=curve_MP_Pinky_Lt, su=0.6666, follow=True)

        cmds.pathAnimation( joint_Pinky_Tendon_OFF_1_Lt, c=curve_MP_Pinky_Tendon_Lt, su=0.2, follow=True)
        cmds.pathAnimation( joint_Pinky_Tendon_OFF_2_Lt, c=curve_MP_Pinky_Tendon_Lt, su=0.4, follow=True)
        cmds.pathAnimation( joint_Pinky_Tendon_OFF_3_Lt, c=curve_MP_Pinky_Tendon_Lt, su=0.6, follow=True)
        cmds.pathAnimation( joint_Pinky_Tendon_OFF_4_Lt, c=curve_MP_Pinky_Tendon_Lt, su=0.8, follow=True)
        

        attributes_to_lock_Pinky = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Pinky:
            cmds.setAttr(joint_DRV_Pinky_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_DRV_Pinky_4_Lt + "." + attr, lock=True)

        attributes_to_lock_tendon_Pinky = ["rotateX","rotateY","rotateZ","translateX","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_tendon_Pinky:
            cmds.setAttr(joint_Pinky_Tendon_1_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Pinky_Tendon_2_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Pinky_Tendon_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_Pinky_Tendon_4_Lt + "." + attr, lock=True)

        

        cmds.select(deselect=True)
        list_grp_placement_jnt = [joint_DRV_Pinky_1_Lt, joint_DRV_Pinky_2_Lt, joint_DRV_Pinky_T_Lt]
        grp_name = "Grp_Deplacement_Groupe_Main_Temp"
        if cmds.objExists(grp_name):
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)
        
        else:
            cmds.group(em=True, n=grp_name)
             
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)


        # cmds.setAttr(joint_DRV_Pinky_1_Lt + ".translatex" + attr, lock=True)

        #loc orientation du doigt
        loc_Pinky_orientaton_joints_Lt = cmds.spaceLocator(n='LOC_Guide_Orient_Pinky_Lt_TEMP', p=(0, 0, 0), )
        
        
        cmds.select(loc_Pinky_orientaton_joints_Lt)
        loc_Pinky_orientaton_joints_Lt_grp = cmds.group(loc_Pinky_orientaton_joints_Lt[0], n= 'temp_loc_Pinky')
        loc_Pinky_orientaton_joints_Lt_grp = cmds.listRelatives(loc_Pinky_orientaton_joints_Lt, parent=True, fullPath=True)
        cmds.pathAnimation( loc_Pinky_orientaton_joints_Lt_grp, c=curve_MP_Pinky_Lt, su=0.5, follow=True)
        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + '.rotateX', 90)
        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + '.rotateY', 0)
        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + '.rotateZ', 90)

        attributes_to_lock_LOC_Pinky = ["rotateY","rotateZ","translateX","translateY","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_LOC_Pinky:
            cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + "." + attr, lock=True)

        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + ".localScaleX" ,0.25)
        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + ".localScaleY" ,2.25)
        cmds.setAttr(loc_Pinky_orientaton_joints_Lt[0] + ".localScaleZ" ,0.25)  




        #color
        jnt_color_green = [joint_DRV_Pinky_1_Lt,joint_DRV_Pinky_2_Lt, joint_DRV_Pinky_T_Lt, loc_Pinky_orientaton_joints_Lt[0]]
        jnt_color_yellow= [joint_Pinky_Tendon_1_Lt , joint_Pinky_Tendon_2_Lt, joint_Pinky_Tendon_3_Lt, joint_Pinky_Tendon_4_Lt, joint_DRV_Pinky_3_Lt, joint_DRV_Pinky_4_Lt ]

        for objcolorgreen in jnt_color_green : 
            cmds.setAttr(objcolorgreen + '.overrideEnabled', 1)
            cmds.setAttr(objcolorgreen + '.overrideColor', 14)

        for objcoloryelllow in jnt_color_yellow : 
            cmds.setAttr(objcoloryelllow + '.overrideEnabled', 1)
            cmds.setAttr(objcoloryelllow + '.overrideColor', 17)    
             
    def pinky_rig_Part_2(*args):

        global group_ctrls_Pinky_Lt
        global group_joints_Pinky_Lt
        global new_Effector_name_Inde
        global group_miror_Pinky_Loc_Space_IK_temp_Lt
        global locator_Finger_HipSpace_IK_Pinky_ctrl
        global locator_Finger_HeadSpace_IK_Pinky_ctrl
        global locator_Finger_HandSpace_IK_Pinky_ctrl

        global locator_Finger_Space_PV_Pinky_ctrl


        controler_hand_control = 'Ctrl_Control_Hand_Lt'

        cmds.delete(curve_MP_Pinky_Lt, curve_MP_Pinky_Tendon_Lt)

        attributes_to_lock_Pinky = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Pinky:
            cmds.setAttr(joint_DRV_Pinky_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_DRV_Pinky_4_Lt + "." + attr, lock=False)

        attributes_to_lock_tendon_Pinky = ["translateX"]
        for attr in attributes_to_lock_tendon_Pinky:
            cmds.setAttr(joint_Pinky_Tendon_1_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Pinky_Tendon_2_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Pinky_Tendon_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_Pinky_Tendon_4_Lt + "." + attr, lock=False)


        ################################


        # orient le premier jnt 01 sans affecter les autres
        cmds.parent(joint_DRV_Pinky_2_Lt, joint_DRV_Pinky_1_Lt)
        cmds.joint(joint_DRV_Pinky_1_Lt, edit=True, oj = 'xyz', sao='yup')
        cmds.parent(joint_DRV_Pinky_2_Lt, world=True)
        cmds.matchTransform(joint_DRV_Pinky_1_Lt,loc_Pinky_orientaton_joints_Lt, rx=True, ry=False, rz=False)






        cmds.matchTransform(joint_DRV_Pinky_2_Lt,loc_Pinky_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Pinky_3_Lt,loc_Pinky_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Pinky_4_Lt,loc_Pinky_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Pinky_T_Lt,loc_Pinky_orientaton_joints_Lt, rot=True)
        
        
        cmds.parent(joint_DRV_Pinky_T_Lt, joint_DRV_Pinky_4_Lt)
        cmds.parent(joint_DRV_Pinky_4_Lt, joint_DRV_Pinky_3_Lt)
        cmds.parent(joint_DRV_Pinky_3_Lt, joint_DRV_Pinky_2_Lt)
        cmds.parent(joint_DRV_Pinky_2_Lt, joint_DRV_Pinky_1_Lt)
        cmds.delete (joint_DRV_Pinky_3_OFF_Lt,joint_DRV_Pinky_4_OFF_Lt)




        cmds.select(deselect=True)
        joint_Pinky_1_Lt = cmds.joint(  n='Sk_Pinky_1_Lt', rad=0.25 )
        cmds.matchTransform(joint_Pinky_1_Lt,joint_DRV_Pinky_1_Lt)
        cmds.select(deselect=True)
        joint_Pinky_2_Lt = cmds.joint( n='Sk_Pinky_2_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Pinky_2_Lt,joint_DRV_Pinky_2_Lt)
        joint_Pinky_3_Lt = cmds.joint(  n='Sk_Pinky_3_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Pinky_3_Lt,joint_DRV_Pinky_3_Lt)
        joint_Pinky_4_Lt = cmds.joint(n='Sk_Pinky_4_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Pinky_4_Lt,joint_DRV_Pinky_4_Lt)
        joint_Pinky_T_Lt = cmds.joint(n='Sk_Pinky_T_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Pinky_T_Lt,joint_DRV_Pinky_T_Lt)



        cmds.parent(joint_Pinky_T_Lt, joint_Pinky_4_Lt)
        cmds.parent(joint_Pinky_4_Lt, joint_Pinky_3_Lt)
        cmds.parent(joint_Pinky_3_Lt, joint_Pinky_2_Lt)
        cmds.parent(joint_Pinky_2_Lt, joint_Pinky_1_Lt)

        #freeze transform jnts avant d'orient
        cmds.select(deselect=True)
        cmds.select(joint_DRV_Pinky_1_Lt,joint_DRV_Pinky_2_Lt,joint_DRV_Pinky_3_Lt,joint_DRV_Pinky_4_Lt,joint_DRV_Pinky_T_Lt,joint_Pinky_1_Lt,joint_Pinky_2_Lt,joint_Pinky_3_Lt,joint_Pinky_4_Lt,joint_Pinky_T_Lt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        #delete le loc orientation 
        cmds.delete(loc_Pinky_orientaton_joints_Lt_grp)

        position_joint_DRV_Pinky_2_Lt = cmds.xform(joint_DRV_Pinky_2_Lt, query=True, worldSpace=True, translation=True)

        cmds.parent(joint_Pinky_Tendon_1_Lt, joint_Pinky_1_Lt)
        cmds.parent(joint_Pinky_Tendon_2_Lt, joint_Pinky_1_Lt)
        cmds.parent(joint_Pinky_Tendon_3_Lt, joint_Pinky_1_Lt)
        cmds.parent(joint_Pinky_Tendon_4_Lt, joint_Pinky_1_Lt)

        cmds.delete(joint_Pinky_Tendon_OFF_1_Lt,joint_Pinky_Tendon_OFF_2_Lt,joint_Pinky_Tendon_OFF_3_Lt,joint_Pinky_Tendon_OFF_4_Lt)



        #creation ctrls
        ctrl_finger_1_Pinky = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_1_Pinky_Lt')[0]
        cmds.select(ctrl_finger_1_Pinky + '.cv[1]', ctrl_finger_1_Pinky + '.cv[5]')
        cmds.scale(1, 1, 0.194499, relative=True, pivot=(0, 0, 0))
        cmds.select(ctrl_finger_1_Pinky + '.cv[0]', ctrl_finger_1_Pinky + '.cv[6]')
        cmds.scale(1, 1, 0.0840956, relative=True, pivot=(0.783612, 0, 0))

        cmds.matchTransform(ctrl_finger_1_Pinky,joint_Pinky_1_Lt)
        cmds.select(ctrl_finger_1_Pinky+'.cv[0:7]')
        cmds.move(0, 2, 0, relative=True, os=True)


        ctrl_finger_2_Pinky = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_2_Pinky_Lt')[0]
        cmds.select(ctrl_finger_2_Pinky + '.cv[1]', ctrl_finger_2_Pinky + '.cv[5]')
        cmds.scale(1, 1, 0.2, relative=True, pivot=(0, 0, 0))

        cmds.matchTransform(ctrl_finger_2_Pinky,joint_Pinky_2_Lt)
        cmds.select(ctrl_finger_2_Pinky+'.cv[0:7]')
        cmds.move(0, 1.5, 0, relative=True, os=True)


        ctrl_finger_3_Pinky = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_3_Pinky_Lt')[0]
        cmds.matchTransform(ctrl_finger_3_Pinky,joint_Pinky_3_Lt)
        cmds.select(ctrl_finger_3_Pinky+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)


        ctrl_finger_4_Pinky = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_4_Pinky_Lt')[0]
        cmds.matchTransform(ctrl_finger_4_Pinky,joint_Pinky_4_Lt)
        cmds.select(ctrl_finger_4_Pinky+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)

        ctrl_Ik_Finger_Pinky = cmds.curve(n='Ctrl_IK_Pinky_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                point = [(0, 1, 0),\
                         (0, 0.92388000000000003, 0.382683),\
                         (0, 0.70710700000000004, 0.70710700000000004),\
                         (0, 0.382683, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0, -0.382683, 0.92388000000000003),\
                         (0, -0.70710700000000004, 0.70710700000000004),\
                         (0, -0.92388000000000003, 0.382683),\
                         (0, -1, 0),\
                         (0, -0.92388000000000003, -0.382683),\
                         (0, -0.70710700000000004, -0.70710700000000004),\
                         (0, -0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 1, 0),\
                         (0.382683, 0.92388000000000003, 0),\
                         (0.70710700000000004, 0.70710700000000004, 0),\
                         (0.92388000000000003, 0.382683, 0),\
                         (1, 0, 0),\
                         (0.92388000000000003, -0.382683, 0),\
                         (0.70710700000000004, -0.70710700000000004, 0),\
                         (0.382683, -0.92388000000000003, 0),\
                         (0, -1, 0),\
                         (-0.382683, -0.92388000000000003, 0),\
                         (-0.70710700000000004, -0.70710700000000004, 0),\
                         (-0.92388000000000003, -0.382683, 0),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0.382683, 0),\
                         (-0.70710700000000004, 0.70710700000000004, 0),\
                         (-0.382683, 0.92388000000000003, 0),\
                         (0, 1, 0),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (-0.382683, 0, -0.92388000000000003),\
                         (-0.70710700000000004, 0, -0.70710700000000004),\
                         (-0.92388000000000003, 0, -0.382683),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0, 0.382683),\
                         (-0.70710700000000004, 0, 0.70710700000000004),\
                         (-0.382683, 0, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0.382683, 0, 0.92388000000000003),\
                         (0.70710700000000004, 0, 0.70710700000000004),\
                         (0.92388000000000003, 0, 0.382683),\
                         (1, 0, 0),\
                         (0.92388000000000003, 0, -0.382683),\
                         (0.70710700000000004, 0, -0.70710700000000004),\
                         (0.382683, 0, -0.92388000000000003),\
                         (0, 0, -1)]\
              )
        cmds.addAttr(ctrl_Ik_Finger_Pinky, longName='Space', attributeType='enum', enumName="World:Hand:Head:Hip", k=True )
        cmds.setAttr(ctrl_Ik_Finger_Pinky + ".Space", 1)
        cmds.matchTransform(ctrl_Ik_Finger_Pinky,joint_Pinky_T_Lt)
        cmds.select(ctrl_Ik_Finger_Pinky+'.cv[0:52]')
        cmds.scale(0.5, 0.5, 0.5, relative=True)
        cmds.move(0, 0, 0, relative=True)
        


        curve_pole_Vector_Pinky = cmds.curve(n='Crv_PV_Pinky_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                point = [(-2, 0, 0),\
                         (1, 0, 1),\
                         (1, 0, -1),\
                         (-2, 0, 0),\
                         (1, 1, 0),\
                         (1, 0, 0),\
                         (1, -1, 0),\
                         (-2, 0, 0)]\
              )

        cmds.addAttr(curve_pole_Vector_Pinky, longName='Guide_Visibility', attributeType='bool', dv=True, k=True )
        cmds.addAttr(curve_pole_Vector_Pinky, longName='Space', attributeType='enum', enumName="World:Hand:Ik_Finger", k=True )
        cmds.setAttr(curve_pole_Vector_Pinky + ".Space", 1)
        cmds.matchTransform(curve_pole_Vector_Pinky,joint_Pinky_3_Lt)
        cmds.select(curve_pole_Vector_Pinky)
        cmds.move(0, 3, 0, relative=True, os=True)
        cmds.select(curve_pole_Vector_Pinky+'.cv[0:7]')
        cmds.rotate(0, 0, 90, relative=True)
        cmds.scale(0.5, 0.5, 0.5, relative=True)

        





        ctrl_finger_Pinky = [ctrl_finger_1_Pinky,ctrl_finger_2_Pinky,ctrl_finger_3_Pinky,ctrl_finger_4_Pinky,ctrl_Ik_Finger_Pinky,curve_pole_Vector_Pinky]
        for offset in ctrl_finger_Pinky :
            cmds.select(offset)
            OFF()

        
        ctrl_finger_1_Pinky_OFF = cmds.listRelatives(ctrl_finger_1_Pinky, parent=True, fullPath=True)
        ctrl_finger_2_Pinky_OFF = cmds.listRelatives(ctrl_finger_2_Pinky, parent=True, fullPath=True)
        ctrl_finger_3_Pinky_OFF = cmds.listRelatives(ctrl_finger_3_Pinky, parent=True, fullPath=True)
        ctrl_finger_4_Pinky_OFF = cmds.listRelatives(ctrl_finger_4_Pinky, parent=True, fullPath=True)
        
        
        
        cmds.parent(ctrl_finger_4_Pinky_OFF, ctrl_finger_3_Pinky)
        cmds.parent(ctrl_finger_3_Pinky_OFF, ctrl_finger_2_Pinky)
        cmds.parent(ctrl_finger_2_Pinky_OFF, ctrl_finger_1_Pinky)

        cmds.parentConstraint( ctrl_finger_1_Pinky, joint_Pinky_1_Lt )
        cmds.parentConstraint( ctrl_finger_2_Pinky, joint_Pinky_2_Lt )
        cmds.parentConstraint( ctrl_finger_3_Pinky, joint_Pinky_3_Lt )
        cmds.parentConstraint( ctrl_finger_4_Pinky, joint_Pinky_4_Lt )
        


        cmds.setAttr(joint_DRV_Pinky_3_Lt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Pinky_4_Lt + '.preferredAngleZ', -10.0)

        ik_Handle_Pinky_Lt = cmds.ikHandle(n='IKRP_Pinky_Lt',  sj=joint_DRV_Pinky_2_Lt, ee=joint_DRV_Pinky_T_Lt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Pinky_Lt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Pinky_Lt[0], ctrl_Ik_Finger_Pinky)
        cmds.poleVectorConstraint( curve_pole_Vector_Pinky, ik_Handle_Pinky_Lt[0] )
        


        new_Effector_name_Pinky = 'EFF_IKRP_Pinky_Lt'
        List_Input_Ik_Handle_Pinky = cmds.listConnections('IKRP_Pinky_Lt',s=True)
        for node in List_Input_Ik_Handle_Pinky:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Pinky)
                break
        
        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Pinky_OFF = cmds.listRelatives(ctrl_finger_1_Pinky, parent=True, fullPath=True)
        ctrl_finger_2_Pinky_OFF = cmds.listRelatives(ctrl_finger_2_Pinky, parent=True, fullPath=True)
        ctrl_finger_3_Pinky_OFF = cmds.listRelatives(ctrl_finger_3_Pinky, parent=True, fullPath=True)
        ctrl_finger_4_Pinky_OFF = cmds.listRelatives(ctrl_finger_4_Pinky, parent=True, fullPath=True)
        curve_pole_Vector_Pinky_OFF = cmds.listRelatives(curve_pole_Vector_Pinky, parent=True, fullPath=True)
        ctrl_Ik_Finger_Pinky_OFF = cmds.listRelatives(ctrl_Ik_Finger_Pinky, parent=True, fullPath=True)
        
        decompose_M_DRV_Pinky_1_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_1_Lt')
        decompose_M_DRV_Pinky_2_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_2_Lt')
        decompose_M_DRV_Pinky_3_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_3_Lt')
        decompose_M_DRV_Pinky_4_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_4_Lt')

        cmds.connectAttr( f'{joint_DRV_Pinky_1_Lt}.xformMatrix', f'{decompose_M_DRV_Pinky_1_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_2_Lt}.xformMatrix', f'{decompose_M_DRV_Pinky_2_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_3_Lt}.xformMatrix', f'{decompose_M_DRV_Pinky_3_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_4_Lt}.xformMatrix', f'{decompose_M_DRV_Pinky_4_Lt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Pinky_1_Lt}.outputTranslate', f'{ctrl_finger_1_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_2_Lt}.outputTranslate', f'{ctrl_finger_2_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_3_Lt}.outputTranslate', f'{ctrl_finger_3_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_4_Lt}.outputTranslate', f'{ctrl_finger_4_Pinky_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Pinky_1_Lt}.outputRotate', f'{ctrl_finger_1_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_2_Lt}.outputRotate', f'{ctrl_finger_2_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_3_Lt}.outputRotate', f'{ctrl_finger_3_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_4_Lt}.outputRotate', f'{ctrl_finger_4_Pinky_OFF[0]}.rotate' )



        cmds.select(deselect=True)
        joint_Pinky_knuckle = cmds.joint(  n='Sk_Pinky_Knuckle_Lt' , rad=0.75)
        cmds.matchTransform(joint_Pinky_knuckle,joint_Pinky_2_Lt)
        cmds.parent(joint_Pinky_knuckle, joint_Pinky_2_Lt )


        

        multiply_divide_value_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Pinky_Lt')
        multiply_divide_lower_intensity_knuckle_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Pinky_Lt')
        multiply_divide_intensity_knuckle_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Pinky_Lt')
        condition_positive_tendon_Pinky = cmds.createNode( 'condition', n='condition_positive_tendon_Pinky_Lt')

        cmds.setAttr(multiply_divide_value_tendon_Pinky + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Pinky + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Pinky + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Pinky + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Pinky + '.operation', 2)

        cmds.connectAttr( f'{joint_Pinky_2_Lt}.rotateZ', f'{condition_positive_tendon_Pinky}.firstTerm' )
        cmds.connectAttr( f'{joint_Pinky_2_Lt}.rotateZ', f'{multiply_divide_value_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{joint_Pinky_2_Lt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Pinky}.outColorR', f'{multiply_divide_value_tendon_Pinky}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Pinky}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Pinky}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputY', f'{joint_Pinky_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_1_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_1_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_2_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_2_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_3_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_3_Lt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_4_Lt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_4_Lt}.translateZ' )

        
    
        cmds.connectAttr( f'{controler_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2Y' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2X' )
        cmds.connectAttr( f'{controler_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2Z' )

        cmds.select(deselect=True)
        ctrls_Pinky_to_goup = [ctrl_Ik_Finger_Pinky_OFF[0], curve_pole_Vector_Pinky_OFF[0], ctrl_finger_1_Pinky_OFF[0]]
        group_ctrls_Pinky_Lt = cmds.group(em=True, name='Grp_Ctrls_Pinky_Lt')
        cmds.parent(ctrls_Pinky_to_goup, group_ctrls_Pinky_Lt)

        
        joint_Pinky_to_goup = [joint_Pinky_1_Lt, joint_DRV_Pinky_1_Lt ]
        group_joints_Pinky_Lt = cmds.group(em=True, name='Grp_Sk_Pinky_Lt')
        cmds.parent(joint_Pinky_to_goup, group_joints_Pinky_Lt)



        #guide visual pv 
        locator_pv_start_Pinky_ctrl_Lt = cmds.spaceLocator(n='LOC_Start_Guide_PV_Pinky_Lt', p=(0, 0, 0), )
        cmds.matchTransform(locator_pv_start_Pinky_ctrl_Lt, joint_Pinky_3_Lt)
        cmds.setAttr(locator_pv_start_Pinky_ctrl_Lt[0] + '.visibility', 0 )
        locator_pv_end_Pinky_ctrl_Lt = cmds.spaceLocator( n='LOC_End_Guide_PV_Pinky_Lt', p=(0, 0, 0)  )
        cmds.matchTransform(locator_pv_end_Pinky_ctrl_Lt, curve_pole_Vector_Pinky)
        cmds.setAttr(locator_pv_end_Pinky_ctrl_Lt[0] + '.visibility', 0 )

        locator_pv_start_Pinky_ctrl_Lt_position = cmds.xform(locator_pv_start_Pinky_ctrl_Lt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Pinky_ctrl_Lt_position = cmds.xform(locator_pv_end_Pinky_ctrl_Lt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Pinky_ctrl_Lt = cmds.curve(d=1, p=[locator_pv_start_Pinky_ctrl_Lt_position, locator_pv_end_Pinky_ctrl_Lt_position], n='Guide_PV_Pinky_Lt')

        decompose_M_curve_start_Pinky_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Pinky_Lt')
        decompose_M_curve_end_Pinky_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Pinky_Lt')


           
        cmds.connectAttr( f'{locator_pv_start_Pinky_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_start_Pinky_Lt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Pinky_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_end_Pinky_Lt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Pinky_Lt}.outputTranslate', f'{curve_pv_Pinky_ctrl_Lt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Pinky_Lt}.outputTranslate', f'{curve_pv_Pinky_ctrl_Lt}.controlPoints[1]' )

        cmds.parent(locator_pv_end_Pinky_ctrl_Lt, curve_pole_Vector_Pinky)
        cmds.parent(locator_pv_start_Pinky_ctrl_Lt, joint_Pinky_3_Lt)

        cmds.setAttr(curve_pv_Pinky_ctrl_Lt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Guide_Visibility', f'{curve_pv_Pinky_ctrl_Lt}.visibility' )
        



        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Pinky_Lt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Pinky_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Pinky_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Pinky_ctrl_Lt[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt, curve_pole_Vector_Pinky)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Pinky_ctrl_Lt, curve_pole_Vector_Pinky)

        hold_matrix_Pinky_PV_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Pinky_Lt')
        mult_Finger_FingerSpace_PV_Pinky_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Pinky_Lt')
        mult_Finger_HandSpace_PV_Pinky_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Pinky_Lt')
        condition_Finger_Space_PV_Pinky_Lt = cmds.createNode( 'condition', n='Cond_Space_Pinky_PV_Lt')
        condition_Finger_FingerSpace_PV_Pinky_Lt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Pinky_Lt')
        condition_Finger_HandSpace_PV_Pinky_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Pinky_Lt')

        blend_matrix_PV_Pinky_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Pinky_Lt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_PV_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_PV_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Pinky_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Pinky_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Pinky_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Pinky_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_PV_Pinky_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Pinky_Lt}.matrixSum', f'{blend_matrix_PV_Pinky_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Pinky_Lt}.matrixSum', f'{blend_matrix_PV_Pinky_Lt}.target[0].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_FingerSpace_PV_Pinky_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_HandSpace_PV_Pinky_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_Space_PV_Pinky_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Pinky_Lt}.outColorR', f'{condition_Finger_Space_PV_Pinky_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Pinky_Lt}.outColorR', f'{condition_Finger_Space_PV_Pinky_Lt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Pinky_Lt}.outColorR', f'{blend_matrix_PV_Pinky_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Pinky_Lt}.outColorG', f'{blend_matrix_PV_Pinky_Lt}.target[1].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Pinky_Lt}.outputMatrix', f'{curve_pole_Vector_Pinky}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Pinky_ctrl_Lt, ctrl_Ik_Finger_Pinky) #et on parente direct le locator de l'ik 





        #Space controller IK a 4 choix

        locator_Finger_HandSpace_IK_Pinky_ctrl = cmds.spaceLocator(n='LOC_Finger_HandSpace_IK_Pinky_Lt', p=(0, 0, 0), )
        locator_Finger_HeadSpace_IK_Pinky_ctrl = cmds.spaceLocator(n='LOC_Finger_HeadSpace_IK_Pinky_Lt', p=(0, 0, 0), )
        locator_Finger_HipSpace_IK_Pinky_ctrl = cmds.spaceLocator(n='LOC_Finger_HipSpace_IK_Pinky_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_HandSpace_IK_Pinky_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HeadSpace_IK_Pinky_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HipSpace_IK_Pinky_ctrl[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_HandSpace_IK_Pinky_ctrl,ctrl_Ik_Finger_Pinky)
        cmds.matchTransform(locator_Finger_HeadSpace_IK_Pinky_ctrl,ctrl_Ik_Finger_Pinky)
        cmds.matchTransform(locator_Finger_HipSpace_IK_Pinky_ctrl,ctrl_Ik_Finger_Pinky)

        hold_matrix_Pinky_IK_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Pinky_Lt')
        mult_Finger_HandSpace_IK_Pinky_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Pinky_Lt')
        mult_Finger_HeadSpace_IK_Pinky_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Pinky_Lt')
        mult_Finger_HipSpace_IK_Pinky_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Pinky_Lt')
        condition_Finger_Space_IK_Pinky_Lt = cmds.createNode( 'condition', n='Cond_Space_Pinky_Lt')
        condition_Finger_HandSpace_IK_Pinky_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_Pinky_Lt')
        condition_Finger_HeadSpace_IK_Pinky_Lt = cmds.createNode( 'condition', n='Cond_HeadSpace_Pinky_Lt')
        condition_Finger_HipSpace_IK_Pinky_Lt = cmds.createNode( 'condition', n='Cond_HipSpace_Pinky_Lt')

        blend_matrix_IK_Pinky_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Pinky_Lt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Lt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_IK_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_IK_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Pinky_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Pinky_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Pinky_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Pinky_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Pinky_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_IK_Pinky_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Pinky_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HipSpace_IK_Pinky_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Pinky_Lt}.matrixSum', f'{blend_matrix_IK_Pinky_Lt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Pinky_Lt}.matrixSum', f'{blend_matrix_IK_Pinky_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Pinky_Lt}.matrixSum', f'{blend_matrix_IK_Pinky_Lt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HandSpace_IK_Pinky_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HeadSpace_IK_Pinky_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HipSpace_IK_Pinky_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_Space_IK_Pinky_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Pinky_Lt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Pinky_Lt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Lt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Pinky_Lt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Lt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Lt}.outColorR', f'{blend_matrix_IK_Pinky_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Lt}.outColorG', f'{blend_matrix_IK_Pinky_Lt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Lt}.outColorB', f'{blend_matrix_IK_Pinky_Lt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Pinky_Lt}.outputMatrix', f'{ctrl_Ik_Finger_Pinky}.offsetParentMatrix' )


            #on range les locator space dans les bon endroit

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Lt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Pinky_ctrl[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Pinky_ctrl[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Pinky_ctrl[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Pinky_ctrl_Lt[0], sk_Hand)
            
            
        else :
            group_miror_Pinky_Loc_Space_IK_temp_Lt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Pinky_A_PARENTER_Lt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Pinky_ctrl[0], locator_Finger_HeadSpace_IK_Pinky_ctrl[0], locator_Finger_HipSpace_IK_Pinky_ctrl[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Pinky_Loc_Space_IK_temp_Lt)



        cmds.select(deselect=True)
        list_set_skin_jnt = [joint_Pinky_1_Lt, joint_Pinky_2_Lt, joint_Pinky_3_Lt, joint_Pinky_4_Lt, joint_Pinky_Tendon_1_Lt, joint_Pinky_Tendon_2_Lt, joint_Pinky_Tendon_3_Lt, joint_Pinky_Tendon_4_Lt, joint_Pinky_knuckle]
        set_name = "MySetJointSkin"
        if cmds.objExists(set_name):
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)
        
        else:
            cmds.sets(n=set_name)
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)



        #rangement dans les groupes


        grp_Controllers = 'Grp_Controllers'
        grp_Skeleton = 'Grp_Skeleton'
        grp_DO_NOT_TOUCH = 'DO_NOT_TOUCH'
        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'


        if not cmds.objExists('Grp_DNT_Hand_Lt'):
            grp_DNT_Hand_Lt = cmds.group(em=True, name='Grp_DNT_Hand_Lt')



        grp_elem_DNT_Pinky = [curve_pv_Pinky_ctrl_Lt]


        cmds.parent(grp_elem_DNT_Pinky, grp_DNT_Hand_Lt )


        if cmds.objExists(grp_Controllers):
            cmds.parent(group_ctrls_Pinky_Lt, grp_Controllers)
        else:
            grp_Controllers = cmds.group(em=True, name='Grp_Controllers')
            cmds.parent(group_ctrls_Pinky_Lt, grp_Controllers)


        if cmds.objExists(grp_Skeleton):
            cmds.parent(group_joints_Pinky_Lt, grp_Skeleton)
        else:
            grp_Skeleton = cmds.group(em=True, name='Grp_Skeleton')
            cmds.parent(group_joints_Pinky_Lt, grp_Skeleton)


        if cmds.objExists(grp_DO_NOT_TOUCH):
            if cmds.objExists('Grp_DNT_Hand_Lt'):
                parent_of_grp_DNT_Hand_Lt = cmds.listRelatives(grp_DNT_Hand_Lt, parent=True)
                if not parent_of_grp_DNT_Hand_Lt:
                    cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)
        else:
            grp_DO_NOT_TOUCH = cmds.group(em=True, name='DO_NOT_TOUCH')
            cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)




         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{controler_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Pinky}.visibility' ) 


        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Lt = "DRV_Palm_IK_Lt"
        if cmds.objExists(DRV_Palm_IK_Lt):
            cmds.parentConstraint(DRV_Palm_IK_Lt, joint_DRV_Pinky_1_Lt, mo=True)    


        #couleurs des controllers 
        jnt_color_Blue = [ctrl_finger_1_Pinky, ctrl_finger_2_Pinky, ctrl_finger_3_Pinky, ctrl_finger_4_Pinky, ctrl_Ik_Finger_Pinky]
        jnt_color_DarkBlue = [ctrl_finger_3_Pinky, ctrl_finger_4_Pinky]
        jnt_color_beige= [curve_pole_Vector_Pinky]
        

        for objcolor_Blue in jnt_color_Blue : 
            cmds.setAttr(objcolor_Blue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Blue + '.overrideColor', 6)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 5)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)


        ###
     
    def pinky_rig_Part_3_Miror(*args):

        duplication_group_ctrls_sk = cmds.duplicate(group_ctrls_Pinky_Lt,group_joints_Pinky_Lt, rc=True)
        

        for Delnode in duplication_group_ctrls_sk: 
            stPinky_del = ['EFF', 'Constraint', 'IKRP_Pinky_Lt', 'LOC_Finger_FingerSpace_PV_Pinky_Lt1']
            for substPinky in stPinky_del:
                if Delnode.find(substPinky) != -1 and cmds.objExists(Delnode):
                    cmds.delete(Delnode)


             
        
        for rename in duplication_group_ctrls_sk:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        group_ctrls_Pinky_Rt = 'Grp_Ctrls_Pinky_Rt'
        group_joints_Pinky_Rt = 'Grp_Sk_Pinky_Rt'
        # group_miror_Pinky_Loc_Space_IK_temp_Rt = 'Grp_LOC_Space_Ik_Finger_Pinky_A_PARENTER_Rt'
        
    
        cmds.setAttr(group_ctrls_Pinky_Rt + '.scaleX', -1 )
        cmds.setAttr(group_joints_Pinky_Rt + '.scaleX', -1 )
        # cmds.setAttr(group_miror_Pinky_Loc_Space_IK_temp_Rt + '.scaleX', -1 )


        #réassignation des varables pour le miror
        ctrl_finger_1_Pinky = 'Ctrl_Finger_1_Pinky_Rt'
        ctrl_finger_2_Pinky = 'Ctrl_Finger_2_Pinky_Rt'
        ctrl_finger_3_Pinky = 'Ctrl_Finger_3_Pinky_Rt'
        ctrl_finger_4_Pinky = 'Ctrl_Finger_4_Pinky_Rt'
        curve_pole_Vector_Pinky = 'Crv_PV_Pinky_Rt'
        ctrl_Ik_Finger_Pinky = 'Ctrl_IK_Pinky_Rt'

        joint_DRV_Pinky_1_Rt = 'DRV_Pinky_1_Rt'
        joint_DRV_Pinky_2_Rt = 'DRV_Pinky_2_Rt'
        joint_DRV_Pinky_3_Rt = 'DRV_Pinky_3_Rt'
        joint_DRV_Pinky_4_Rt = 'DRV_Pinky_4_Rt'
        joint_DRV_Pinky_T_Rt = 'DRV_Pinky_T_Rt'
        joint_Pinky_1_Rt = 'Sk_Pinky_1_Rt'
        joint_Pinky_2_Rt = 'Sk_Pinky_2_Rt'
        joint_Pinky_3_Rt = 'Sk_Pinky_3_Rt'
        joint_Pinky_4_Rt = 'Sk_Pinky_4_Rt'
        joint_Pinky_T_Rt = 'Sk_Pinky_T_Rt'
        joint_Pinky_Tendon_1_Rt = 'Sk_Pinky_Tendon_1_Rt'
        joint_Pinky_Tendon_2_Rt = 'Sk_Pinky_Tendon_2_Rt'
        joint_Pinky_Tendon_3_Rt = 'Sk_Pinky_Tendon_3_Rt'
        joint_Pinky_Tendon_4_Rt = 'Sk_Pinky_Tendon_4_Rt'
        joint_Pinky_knuckle = 'Sk_Pinky_Knuckle_Rt'

        duplication_ctrl_hand_control = 'Ctrl_Control_Hand_Rt'
        locator_pv_start_Pinky_ctrl_Rt = 'LOC_Start_Guide_PV_Pinky_Rt'
        locator_pv_end_Pinky_ctrl_Rt = 'LOC_End_Guide_PV_Pinky_Rt'


        '''
        duplication du code au dessus qui suit

        '''


        cmds.parentConstraint( ctrl_finger_1_Pinky, joint_Pinky_1_Rt )
        cmds.parentConstraint( ctrl_finger_2_Pinky, joint_Pinky_2_Rt )
        cmds.parentConstraint( ctrl_finger_3_Pinky, joint_Pinky_3_Rt )
        cmds.parentConstraint( ctrl_finger_4_Pinky, joint_Pinky_4_Rt )
        


        cmds.setAttr(joint_DRV_Pinky_3_Rt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Pinky_4_Rt + '.preferredAngleZ', -10.0)

        ik_Handle_Pinky_Rt = cmds.ikHandle(n='IKRP_Pinky_Rt',  sj=joint_DRV_Pinky_2_Rt, ee=joint_DRV_Pinky_T_Rt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Pinky_Rt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Pinky_Rt[0], ctrl_Ik_Finger_Pinky)
        cmds.poleVectorConstraint( curve_pole_Vector_Pinky, ik_Handle_Pinky_Rt[0] )


        new_Effector_name_Pinky = 'EFF_IKRP_Pinky_Rt'
        List_Input_Ik_Handle_Pinky = cmds.listConnections('IKRP_Pinky_Rt',s=True)
        for node in List_Input_Ik_Handle_Pinky:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Pinky)
                break
        

        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Pinky_OFF = cmds.listRelatives(ctrl_finger_1_Pinky, parent=True, fullPath=True)
        ctrl_finger_2_Pinky_OFF = cmds.listRelatives(ctrl_finger_2_Pinky, parent=True, fullPath=True)
        ctrl_finger_3_Pinky_OFF = cmds.listRelatives(ctrl_finger_3_Pinky, parent=True, fullPath=True)
        ctrl_finger_4_Pinky_OFF = cmds.listRelatives(ctrl_finger_4_Pinky, parent=True, fullPath=True)
        curve_pole_Vector_Pinky_OFF = cmds.listRelatives(curve_pole_Vector_Pinky, parent=True, fullPath=True)
        ctrl_Ik_Finger_Pinky_OFF = cmds.listRelatives(ctrl_Ik_Finger_Pinky, parent=True, fullPath=True)
        
        decompose_M_DRV_Pinky_1_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_1_Rt')
        decompose_M_DRV_Pinky_2_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_2_Rt')
        decompose_M_DRV_Pinky_3_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_3_Rt')
        decompose_M_DRV_Pinky_4_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Pinky_4_Rt')

        cmds.connectAttr( f'{joint_DRV_Pinky_1_Rt}.xformMatrix', f'{decompose_M_DRV_Pinky_1_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_2_Rt}.xformMatrix', f'{decompose_M_DRV_Pinky_2_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_3_Rt}.xformMatrix', f'{decompose_M_DRV_Pinky_3_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Pinky_4_Rt}.xformMatrix', f'{decompose_M_DRV_Pinky_4_Rt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Pinky_1_Rt}.outputTranslate', f'{ctrl_finger_1_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_2_Rt}.outputTranslate', f'{ctrl_finger_2_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_3_Rt}.outputTranslate', f'{ctrl_finger_3_Pinky_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_4_Rt}.outputTranslate', f'{ctrl_finger_4_Pinky_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Pinky_1_Rt}.outputRotate', f'{ctrl_finger_1_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_2_Rt}.outputRotate', f'{ctrl_finger_2_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_3_Rt}.outputRotate', f'{ctrl_finger_3_Pinky_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Pinky_4_Rt}.outputRotate', f'{ctrl_finger_4_Pinky_OFF[0]}.rotate' )



        multiply_divide_value_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Pinky_Rt')
        multiply_divide_lower_intensity_knuckle_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Pinky_Rt')
        multiply_divide_intensity_knuckle_tendon_Pinky = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Pinky_Rt')
        condition_positive_tendon_Pinky = cmds.createNode( 'condition', n='condition_positive_tendon_Pinky_Rt')

        cmds.setAttr(multiply_divide_value_tendon_Pinky + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Pinky + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Pinky + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Pinky + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Pinky + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Pinky + '.operation', 2)

        cmds.connectAttr( f'{joint_Pinky_2_Rt}.rotateZ', f'{condition_positive_tendon_Pinky}.firstTerm' )
        cmds.connectAttr( f'{joint_Pinky_2_Rt}.rotateZ', f'{multiply_divide_value_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{joint_Pinky_2_Rt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Pinky}.outColorR', f'{multiply_divide_value_tendon_Pinky}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Pinky}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Pinky}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Pinky}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputY', f'{joint_Pinky_knuckle}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_1_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_1_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_2_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_2_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_3_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_3_Rt}.translateZ' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputX', f'{joint_Pinky_Tendon_4_Rt}.translateY' )
        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Pinky}.outputZ', f'{joint_Pinky_Tendon_4_Rt}.translateZ' )

        
    
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2Y' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2X' )
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Tendons', f'{multiply_divide_intensity_knuckle_tendon_Pinky}.input2Z' )

        cmds.select(deselect=True)

        

        #miror
        locator_pv_start_Pinky_ctrl_Rt_position = cmds.xform(locator_pv_start_Pinky_ctrl_Rt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Pinky_ctrl_Rt_position = cmds.xform(locator_pv_end_Pinky_ctrl_Rt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Pinky_ctrl_Rt = cmds.curve(d=1, p=[locator_pv_start_Pinky_ctrl_Rt_position, locator_pv_end_Pinky_ctrl_Rt_position], n='Guide_PV_Pinky_Rt')

        decompose_M_curve_start_Pinky_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Pinky_Rt')
        decompose_M_curve_end_Pinky_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Pinky_Rt')

        
   
        cmds.connectAttr( f'{locator_pv_start_Pinky_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_start_Pinky_Rt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Pinky_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_end_Pinky_Rt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Pinky_Rt}.outputTranslate', f'{curve_pv_Pinky_ctrl_Rt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Pinky_Rt}.outputTranslate', f'{curve_pv_Pinky_ctrl_Rt}.controlPoints[1]' )

        

        cmds.setAttr(curve_pv_Pinky_ctrl_Rt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Guide_Visibility', f'{curve_pv_Pinky_ctrl_Rt}.visibility' )



        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Pinky_Rt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Pinky_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Pinky_Rt', p=(0, 0, 0))
        cmds.parent(locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt, curve_pole_Vector_Pinky )
        cmds.parent(locator_Finger_HandSpace_PV_Pinky_ctrl_Rt, curve_pole_Vector_Pinky )
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt, curve_pole_Vector_Pinky)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Pinky_ctrl_Rt, curve_pole_Vector_Pinky)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Pinky_ctrl_Rt[0] + '.visibility', 0)
        

        hold_matrix_Pinky_PV_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Pinky_Rt')
        mult_Finger_FingerSpace_PV_Pinky_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Pinky_Rt')
        mult_Finger_HandSpace_PV_Pinky_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Pinky_Rt')
        condition_Finger_Space_PV_Pinky_Rt = cmds.createNode( 'condition', n='Cond_Space_Pinky_PV_Rt')
        condition_Finger_FingerSpace_PV_Pinky_Rt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Pinky_Rt')
        condition_Finger_HandSpace_PV_Pinky_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Pinky_Rt')

        blend_matrix_PV_Pinky_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Pinky_Rt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Pinky_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Pinky_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_PV_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_PV_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Pinky_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Pinky_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Pinky_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Pinky_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_PV_Pinky_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Pinky_Rt}.matrixSum', f'{blend_matrix_PV_Pinky_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Pinky_Rt}.matrixSum', f'{blend_matrix_PV_Pinky_Rt}.target[1].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_FingerSpace_PV_Pinky_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_HandSpace_PV_Pinky_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Pinky}.Space', f'{condition_Finger_Space_PV_Pinky_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Pinky_Rt}.outColorR', f'{condition_Finger_Space_PV_Pinky_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Pinky_Rt}.outColorR', f'{condition_Finger_Space_PV_Pinky_Rt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Pinky_Rt}.outColorR', f'{blend_matrix_PV_Pinky_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Pinky_Rt}.outColorG', f'{blend_matrix_PV_Pinky_Rt}.target[0].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Pinky_Rt}.outputMatrix', f'{curve_pole_Vector_Pinky}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Pinky_ctrl_Rt, ctrl_Ik_Finger_Pinky) #et on parente direct le locator de l'ik 




                #Space controller IK a 4 choix MIROR    
        

        # le coté rt ne marche pas avec ça donc il faut venir faire une duplication des anciens locators
            #on vient recuperer les anciens locators
        list_locator_PinkySpace_dup = [locator_Finger_HipSpace_IK_Pinky_ctrl  , locator_Finger_HeadSpace_IK_Pinky_ctrl ,   locator_Finger_HandSpace_IK_Pinky_ctrl ]

            #on cree une nouvelle liste qui va aceuillir nos nouveaux locators
        new_list_locator_PinkySpace_dup = []
        for elem in list_locator_PinkySpace_dup:
            duplication_group_loc_space = cmds.duplicate(elem,  rc=True)
            new_list_locator_PinkySpace_dup.append(duplication_group_loc_space)

            #on cree le grp temporaire qui va scale -1
        group_miror_locators_PinkySpace = cmds.group(empty=True, n='Grp_Temp_miror_Loc_Pinky_Rt')

            

            #on parente les nouveaux elements de la nouvelle liste au grp  et ensuite on scale le groupe pour miror
        for elem in new_list_locator_PinkySpace_dup :
            cmds.parent(elem, group_miror_locators_PinkySpace)

        cmds.setAttr(group_miror_locators_PinkySpace + ".scaleX", -1)

            #on vient faire une list relative pour identifier les enfants et pas que ça poe de probleme pour le rename 
        group_miror_locators_PinkySpace_children = cmds.listRelatives(group_miror_locators_PinkySpace, c=True)

            #on vient les renommer en rt
        for rename in group_miror_locators_PinkySpace_children:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        locator_Finger_HandSpace_IK_Pinky_ctrl_Rt = 'LOC_Finger_HandSpace_IK_Pinky_Rt'
        locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt = 'LOC_Finger_HeadSpace_IK_Pinky_Rt'
        locator_Finger_HipSpace_IK_Pinky_ctrl_Rt = 'LOC_Finger_HipSpace_IK_Pinky_Rt'

        
        cmds.select(locator_Finger_HandSpace_IK_Pinky_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HipSpace_IK_Pinky_ctrl_Rt)                
        OFF()
        

        

        locator_Finger_HandSpace_IK_Pinky_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HandSpace_IK_Pinky_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HipSpace_IK_Pinky_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HipSpace_IK_Pinky_ctrl_Rt, parent=True, fullPath=True)
        

        

        
 
        

        hold_matrix_Pinky_IK_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Pinky_Rt')
        mult_Finger_HandSpace_IK_Pinky_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Pinky_Rt')
        mult_Finger_HeadSpace_IK_Pinky_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Pinky_Rt')
        mult_Finger_HipSpace_IK_Pinky_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Pinky_Rt')
        condition_Finger_Space_IK_Pinky_Rt = cmds.createNode( 'condition', n='Cond_Space_Pinky_Rt')
        condition_Finger_HandSpace_IK_Pinky_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_Pinky_Rt')
        condition_Finger_HeadSpace_IK_Pinky_Rt = cmds.createNode( 'condition', n='Cond_HeadSpace_Pinky_Rt')
        condition_Finger_HipSpace_IK_Pinky_Rt = cmds.createNode( 'condition', n='Cond_HipSpace_Pinky_Rt')

        blend_matrix_IK_Pinky_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Pinky_Rt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Rt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Pinky_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Pinky_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Pinky_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_IK_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Pinky_IK_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Pinky_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Pinky_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Pinky_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Pinky_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Pinky_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_IK_Pinky_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Pinky_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Pinky_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HipSpace_IK_Pinky_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Pinky_Rt}.matrixSum', f'{blend_matrix_IK_Pinky_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Pinky_Rt}.matrixSum', f'{blend_matrix_IK_Pinky_Rt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Pinky_Rt}.matrixSum', f'{blend_matrix_IK_Pinky_Rt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HandSpace_IK_Pinky_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HeadSpace_IK_Pinky_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_HipSpace_IK_Pinky_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Pinky}.Space', f'{condition_Finger_Space_IK_Pinky_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Pinky_Rt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Pinky_Rt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Rt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Pinky_Rt}.outColorR', f'{condition_Finger_Space_IK_Pinky_Rt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Rt}.outColorR', f'{blend_matrix_IK_Pinky_Rt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Rt}.outColorG', f'{blend_matrix_IK_Pinky_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Pinky_Rt}.outColorB', f'{blend_matrix_IK_Pinky_Rt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Pinky_Rt}.outputMatrix', f'{ctrl_Ik_Finger_Pinky}.offsetParentMatrix' )  


            #on parente les locators

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Rt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Pinky_ctrl_Rt_OFF[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt_OFF[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Pinky_ctrl_Rt_OFF[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Pinky_ctrl_Rt[0], sk_Hand)
            
            
        else :
            group_miror_Pinky_Loc_Space_IK_temp_Rt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Pinky_A_PARENTER_Rt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Pinky_ctrl_Rt_OFF[0], locator_Finger_HeadSpace_IK_Pinky_ctrl_Rt_OFF[0], locator_Finger_HipSpace_IK_Pinky_ctrl_Rt_OFF[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Pinky_Loc_Space_IK_temp_Rt)
            cmds.select(deselect=True)

        #apres ça on supprime le grp scale -1 des locators 
        cmds.delete(group_miror_locators_PinkySpace)


        #parenter les crv guides 

        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'
        cmds.parent(curve_pv_Pinky_ctrl_Rt, grp_DNT_Hand_Lt)



         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Pinky}.visibility' )  


        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Rt = "DRV_Palm_IK_Rt"
        if cmds.objExists(DRV_Palm_IK_Rt):
            cmds.parentConstraint(DRV_Palm_IK_Rt, joint_DRV_Pinky_1_Rt, mo=True)     


        #couleurs des controllers 
        jnt_color_Red = [ctrl_finger_1_Pinky, ctrl_finger_2_Pinky, ctrl_finger_3_Pinky, ctrl_finger_4_Pinky, ctrl_Ik_Finger_Pinky]
        jnt_color_DarkBlue = [ctrl_finger_3_Pinky, ctrl_finger_4_Pinky]
        jnt_color_beige= [curve_pole_Vector_Pinky]
        

        for objcolor_Red in jnt_color_Red : 
            cmds.setAttr(objcolor_Red + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Red + '.overrideColor', 13)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 18)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def pinky_rig_Suppr(*args): 
        
        pinky_finger_to_suppr = ['Grp_Ctrls_Pinky_Lt', 'Grp_Sk_Pinky_Lt','Guide_PV_Pinky_Lt', 'Grp_LOC_Space_Ik_Finger_Pinky_A_PARENTER_Lt', 'Grp_Ctrls_Pinky_Rt', 'Grp_Sk_Pinky_Rt','Guide_PV_Pinky_Rt', 'Grp_LOC_Space_Ik_Finger_Pinky_A_PARENTER_Rt']
        identify_pinky_finger_to_suppr = cmds.listRelatives(pinky_finger_to_suppr, ad=True)
        list_suppr = [pinky_finger_to_suppr]

        for i in range(100):
            list_suppr.append(identify_pinky_finger_to_suppr)
            identify_pinky_finger_to_suppr = cmds.listConnections(identify_pinky_finger_to_suppr, d=True, s=True)
            
            if not identify_pinky_finger_to_suppr:
                break

        list_suppr_2 = []
        list_Not_Suppr_pinky = ['defaultRenderUtilityList', 'MayaNodeEditorSavedTabsInfo', 'Ctrl_Control_Hand', 'Index', 'Middle', 'Ring', 'Thumb','bindPose','ikRPsolver','ikSCsolver','hikSolver', 'ikSplineSolver','ikSystem','MySetJointSkin']

        for elem in list_suppr:
            for node in elem:
                skip_node = False

                for pinky_name in list_Not_Suppr_pinky:
                    if pinky_name in node:
                        skip_node = True
                        break

                if not skip_node:
                    list_suppr_2.append(node)

        cmds.delete(list_suppr_2)
###   

    def thumb_rig_Part_1(*args):
        
        global joint_DRV_Thumb_1_Lt
        global joint_DRV_Thumb_2_Lt
        global joint_DRV_Thumb_3_Lt
        global joint_DRV_Thumb_4_Lt
        global joint_DRV_Thumb_T_Lt
        global curve_MP_Thumb_Lt
        global joint_DRV_Thumb_3_OFF_Lt
        global joint_DRV_Thumb_4_OFF_Lt
        
        global joint_Thumb_Tendon_1_Lt
        global joint_Thumb_Tendon_2_Lt
        global joint_Thumb_Tendon_3_Lt
        global joint_Thumb_Tendon_4_Lt
        global curve_MP_Thumb_Tendon_Lt
        global joint_Thumb_Tendon_OFF_1_Lt
        global joint_Thumb_Tendon_OFF_2_Lt
        global joint_Thumb_Tendon_OFF_3_Lt
        global joint_Thumb_Tendon_OFF_4_Lt
        global loc_Thumb_orientaton_joints_Lt
        global loc_Thumb_orientaton_joints_Lt_grp
        
        


        cmds.select(deselect=True)
        joint_DRV_Thumb_1_Lt = cmds.joint(n='DRV_Thumb_1_Lt', p=(54, 104.5, -3.5))
        joint_DRV_Thumb_2_Lt = cmds.joint(n='DRV_Thumb_2_Lt', p=(54.5, 103, -2.5))
        joint_DRV_Thumb_3_Lt = cmds.joint(n='DRV_Thumb_3_Lt', p=(5, 0, 5))
        joint_DRV_Thumb_4_Lt = cmds.joint(n='DRV_Thumb_4_Lt', p=(10, 0, 5))
        joint_DRV_Thumb_T_Lt = cmds.joint(n='DRV_Thumb_T_Lt', p=(59.5, 97, 4), rad=0.5)

        cmds.parent(joint_DRV_Thumb_T_Lt, world=True)
        cmds.parent(joint_DRV_Thumb_4_Lt, world=True)
        cmds.parent(joint_DRV_Thumb_3_Lt, world=True)
        cmds.parent(joint_DRV_Thumb_2_Lt, world=True)
        

        jnt_finger_Thumb = [joint_DRV_Thumb_3_Lt,joint_DRV_Thumb_4_Lt]
        for offset in jnt_finger_Thumb :
            cmds.select(offset)
            OFF()


        joint_DRV_Thumb_3_OFF_Lt = cmds.listRelatives(joint_DRV_Thumb_3_Lt, parent=True, fullPath=True)        
        joint_DRV_Thumb_4_OFF_Lt = cmds.listRelatives(joint_DRV_Thumb_4_Lt, parent=True, fullPath=True)



        jnt_0_Crv_Position_Thumb = cmds.xform(joint_DRV_Thumb_1_Lt, query=True, worldSpace=True, translation=True)
        jnt_1_Crv_Position_Thumb = cmds.xform(joint_DRV_Thumb_2_Lt, query=True, worldSpace=True, translation=True)
        jnt_2_Crv_Position_Thumb = cmds.xform(joint_DRV_Thumb_T_Lt, query=True, worldSpace=True, translation=True)
        joint_Skin_Crv_Thumb_1_Lt = [joint_DRV_Thumb_2_Lt , joint_DRV_Thumb_T_Lt]
        joint_Skin_Crv_Thumb_2_Lt = [joint_DRV_Thumb_1_Lt ,joint_DRV_Thumb_2_Lt]

        curve_MP_Thumb_Lt = cmds.curve(d=1, p=[jnt_1_Crv_Position_Thumb, jnt_2_Crv_Position_Thumb], n='Crv_MP_Thumb_Lt_Temp')
        curve_MP_Thumb_Tendon_Lt = cmds.curve(d=1, p=[jnt_0_Crv_Position_Thumb, jnt_1_Crv_Position_Thumb], n='Crv_MP_Thumb_Tendon_Lt_Temp')

        bind_skin_cluster_Thumb = cmds.skinCluster(joint_Skin_Crv_Thumb_1_Lt, curve_MP_Thumb_Lt, tsb=True)
        bind_skin_cluster_tendon_Thumb = cmds.skinCluster(joint_Skin_Crv_Thumb_2_Lt, curve_MP_Thumb_Tendon_Lt, tsb=True)



        cmds.pathAnimation( joint_DRV_Thumb_3_OFF_Lt, c=curve_MP_Thumb_Lt, su=0.3333, follow=True)
        cmds.pathAnimation( joint_DRV_Thumb_4_OFF_Lt, c=curve_MP_Thumb_Lt, su=0.6666, follow=True)


        attributes_to_lock_Thumb = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Thumb:
            cmds.setAttr(joint_DRV_Thumb_3_Lt + "." + attr, lock=True)
            cmds.setAttr(joint_DRV_Thumb_4_Lt + "." + attr, lock=True)


        cmds.select(deselect=True)
        list_grp_placement_jnt = [joint_DRV_Thumb_1_Lt, joint_DRV_Thumb_2_Lt, joint_DRV_Thumb_T_Lt]
        grp_name = "Grp_Deplacement_Groupe_Main_Temp"
        if cmds.objExists(grp_name):
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)
        
        else:
            cmds.group(em=True, n=grp_name)
            
            for joints in list_grp_placement_jnt : 
                cmds.parent(joints, grp_name)



        #loc orientation du doigt
        loc_Thumb_orientaton_joints_Lt = cmds.spaceLocator(n='LOC_Guide_Orient_Thumb_Lt_TEMP', p=(0, 0, 0), )
        
        
        cmds.select(loc_Thumb_orientaton_joints_Lt)
        loc_Thumb_orientaton_joints_Lt_grp = cmds.group(loc_Thumb_orientaton_joints_Lt[0], n= 'temp_loc')
        loc_Thumb_orientaton_joints_Lt_grp = cmds.listRelatives(loc_Thumb_orientaton_joints_Lt, parent=True, fullPath=True)
        cmds.pathAnimation( loc_Thumb_orientaton_joints_Lt_grp, c=curve_MP_Thumb_Lt, su=0.5, follow=True)
        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + '.rotateX', -65)
        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + '.rotateY', 180)
        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + '.rotateZ', -90)



        attributes_to_lock_Orientation_Thumb = ["rotateY","rotateZ","translateX","translateY", "translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Orientation_Thumb:
             cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + "." + attr, lock=True)


        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + ".localScaleX" ,0.25)
        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + ".localScaleY" ,2.25)
        cmds.setAttr(loc_Thumb_orientaton_joints_Lt[0] + ".localScaleZ" ,0.25)




#color
        jnt_color_green = [joint_DRV_Thumb_1_Lt,joint_DRV_Thumb_2_Lt, joint_DRV_Thumb_T_Lt, loc_Thumb_orientaton_joints_Lt[0]]
        jnt_color_yellow= [ joint_DRV_Thumb_3_Lt, joint_DRV_Thumb_4_Lt ]

        for objcolorgreen in jnt_color_green : 
            cmds.setAttr(objcolorgreen + '.overrideEnabled', 1)
            cmds.setAttr(objcolorgreen + '.overrideColor', 14)

        for objcoloryelllow in jnt_color_yellow : 
            cmds.setAttr(objcoloryelllow + '.overrideEnabled', 1)
            cmds.setAttr(objcoloryelllow + '.overrideColor', 17)  
       
    def thumb_rig_Part_2(*args):

        global group_ctrls_Thumb_Lt
        global group_joints_Thumb_Lt
        global new_Effector_name_Inde
        global group_miror_Thumb_Loc_Space_IK_temp_Lt
        global locator_Finger_HipSpace_IK_Thumb_ctrl
        global locator_Finger_HeadSpace_IK_Thumb_ctrl
        global locator_Finger_HandSpace_IK_Thumb_ctrl

        global locator_Finger_Space_PV_Thumb_ctrl


        controler_hand_control = 'Ctrl_Control_Hand_Lt'

        cmds.delete(curve_MP_Thumb_Lt,curve_MP_Thumb_Tendon_Lt)

        attributes_to_lock_Thumb = ["rotateX","rotateY","rotateZ","translateX","translateZ","scaleX","scaleY","scaleZ"]
        for attr in attributes_to_lock_Thumb:
            cmds.setAttr(joint_DRV_Thumb_3_Lt + "." + attr, lock=False)
            cmds.setAttr(joint_DRV_Thumb_4_Lt + "." + attr, lock=False)

        
        #joint du doigt


        cmds.matchTransform(joint_DRV_Thumb_2_Lt,loc_Thumb_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Thumb_3_Lt,loc_Thumb_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Thumb_4_Lt,loc_Thumb_orientaton_joints_Lt, rot=True)
        cmds.matchTransform(joint_DRV_Thumb_T_Lt,loc_Thumb_orientaton_joints_Lt, rot=True)
        cmds.setAttr(joint_DRV_Thumb_1_Lt + '.rotateY', -90)
        
        cmds.parent(joint_DRV_Thumb_T_Lt, joint_DRV_Thumb_4_Lt)
        cmds.parent(joint_DRV_Thumb_4_Lt, joint_DRV_Thumb_3_Lt)
        cmds.parent(joint_DRV_Thumb_3_Lt, joint_DRV_Thumb_2_Lt)
        cmds.parent(joint_DRV_Thumb_2_Lt, joint_DRV_Thumb_1_Lt)
        cmds.delete (joint_DRV_Thumb_3_OFF_Lt,joint_DRV_Thumb_4_OFF_Lt)



        cmds.select(deselect=True)
        joint_Thumb_1_Lt = cmds.joint(  n='Sk_Thumb_1_Lt', rad=0.25 )
        cmds.matchTransform(joint_Thumb_1_Lt,joint_DRV_Thumb_1_Lt)
        cmds.select(deselect=True)
        joint_Thumb_2_Lt = cmds.joint( n='Sk_Thumb_2_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Thumb_2_Lt,joint_DRV_Thumb_2_Lt)
        joint_Thumb_3_Lt = cmds.joint(  n='Sk_Thumb_3_Lt', rad=0.25  )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Thumb_3_Lt,joint_DRV_Thumb_3_Lt)
        joint_Thumb_4_Lt = cmds.joint(n='Sk_Thumb_4_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Thumb_4_Lt,joint_DRV_Thumb_4_Lt)
        joint_Thumb_T_Lt = cmds.joint(n='Sk_Thumb_T_Lt', rad=0.25 )
        cmds.select(deselect=True)
        cmds.matchTransform(joint_Thumb_T_Lt,joint_DRV_Thumb_T_Lt)



        cmds.parent(joint_Thumb_T_Lt, joint_Thumb_4_Lt)
        cmds.parent(joint_Thumb_4_Lt, joint_Thumb_3_Lt)
        cmds.parent(joint_Thumb_3_Lt, joint_Thumb_2_Lt)
        cmds.parent(joint_Thumb_2_Lt, joint_Thumb_1_Lt)



        #freeze transform jnts avant d'orient
        cmds.select(deselect=True)
        cmds.select(joint_DRV_Thumb_1_Lt,joint_DRV_Thumb_2_Lt,joint_DRV_Thumb_3_Lt,joint_DRV_Thumb_4_Lt,joint_DRV_Thumb_T_Lt,joint_Thumb_1_Lt,joint_Thumb_2_Lt,joint_Thumb_3_Lt,joint_Thumb_4_Lt,joint_Thumb_T_Lt)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        #delete le loc orientation 
        cmds.delete(loc_Thumb_orientaton_joints_Lt_grp)

        position_joint_DRV_Thumb_2_Lt = cmds.xform(joint_DRV_Thumb_2_Lt, query=True, worldSpace=True, translation=True)


        #creation ctrls
        ctrl_finger_1_Thumb = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_1_Thumb_Lt')[0]
        cmds.select(ctrl_finger_1_Thumb + '.cv[1]', ctrl_finger_1_Thumb + '.cv[5]')
        cmds.scale(1, 1, 0.194499, relative=True, pivot=(0, 0, 0))
        cmds.select(ctrl_finger_1_Thumb + '.cv[0]', ctrl_finger_1_Thumb + '.cv[6]')
        cmds.scale(1, 1, 0.0840956, relative=True, pivot=(0.783612, 0, 0))

        cmds.matchTransform(ctrl_finger_1_Thumb,joint_Thumb_1_Lt)
        cmds.select(ctrl_finger_1_Thumb+'.cv[0:7]')
        #cmds.rotate(-90, 0, 0, relative=True, os=True)
        cmds.move(0, 5, 0, relative=True, ws=True)
        
        #cmds.rotate(-90, 0, 0, relative=True, os=True)


        ctrl_finger_2_Thumb = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n='Ctrl_Finger_2_Thumb_Lt')[0]
        cmds.select(ctrl_finger_2_Thumb + '.cv[1]', ctrl_finger_2_Thumb + '.cv[5]')
        cmds.scale(1, 1, 0.2, relative=True, pivot=(0, 0, 0))

        cmds.matchTransform(ctrl_finger_2_Thumb,joint_Thumb_2_Lt)
        cmds.select(ctrl_finger_2_Thumb+'.cv[0:7]')
        cmds.move(0, 1.5, 0, relative=True)
        cmds.move(0, 3, 0, relative=True, os=True)


        ctrl_finger_3_Thumb = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_3_Thumb_Lt')[0]
        cmds.matchTransform(ctrl_finger_3_Thumb,joint_Thumb_3_Lt)
        cmds.select(ctrl_finger_3_Thumb+'.cv[0:7]')
        cmds.scale(2.5, 2.5, 2.5, relative=True)


        ctrl_finger_4_Thumb = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), n='Ctrl_Finger_4_Thumb_Lt')[0]
        cmds.matchTransform(ctrl_finger_4_Thumb,joint_Thumb_4_Lt)
        cmds.select(ctrl_finger_4_Thumb+'.cv[0:7]')
        cmds.scale(1.4, 1.4, 1.4, relative=True)

        ctrl_Ik_Finger_Thumb = cmds.curve(n='Ctrl_IK_Thumb_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                point = [(0, 1, 0),\
                         (0, 0.92388000000000003, 0.382683),\
                         (0, 0.70710700000000004, 0.70710700000000004),\
                         (0, 0.382683, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0, -0.382683, 0.92388000000000003),\
                         (0, -0.70710700000000004, 0.70710700000000004),\
                         (0, -0.92388000000000003, 0.382683),\
                         (0, -1, 0),\
                         (0, -0.92388000000000003, -0.382683),\
                         (0, -0.70710700000000004, -0.70710700000000004),\
                         (0, -0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 1, 0),\
                         (0.382683, 0.92388000000000003, 0),\
                         (0.70710700000000004, 0.70710700000000004, 0),\
                         (0.92388000000000003, 0.382683, 0),\
                         (1, 0, 0),\
                         (0.92388000000000003, -0.382683, 0),\
                         (0.70710700000000004, -0.70710700000000004, 0),\
                         (0.382683, -0.92388000000000003, 0),\
                         (0, -1, 0),\
                         (-0.382683, -0.92388000000000003, 0),\
                         (-0.70710700000000004, -0.70710700000000004, 0),\
                         (-0.92388000000000003, -0.382683, 0),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0.382683, 0),\
                         (-0.70710700000000004, 0.70710700000000004, 0),\
                         (-0.382683, 0.92388000000000003, 0),\
                         (0, 1, 0),\
                         (0, 0.92388000000000003, -0.382683),\
                         (0, 0.70710700000000004, -0.70710700000000004),\
                         (0, 0.382683, -0.92388000000000003),\
                         (0, 0, -1),\
                         (-0.382683, 0, -0.92388000000000003),\
                         (-0.70710700000000004, 0, -0.70710700000000004),\
                         (-0.92388000000000003, 0, -0.382683),\
                         (-1, 0, 0),\
                         (-0.92388000000000003, 0, 0.382683),\
                         (-0.70710700000000004, 0, 0.70710700000000004),\
                         (-0.382683, 0, 0.92388000000000003),\
                         (0, 0, 1),\
                         (0.382683, 0, 0.92388000000000003),\
                         (0.70710700000000004, 0, 0.70710700000000004),\
                         (0.92388000000000003, 0, 0.382683),\
                         (1, 0, 0),\
                         (0.92388000000000003, 0, -0.382683),\
                         (0.70710700000000004, 0, -0.70710700000000004),\
                         (0.382683, 0, -0.92388000000000003),\
                         (0, 0, -1)]\
              )
        cmds.addAttr(ctrl_Ik_Finger_Thumb, longName='Space', attributeType='enum', enumName="World:Hand:Head:Hip", k=True )
        cmds.setAttr(ctrl_Ik_Finger_Thumb + ".Space", 1)
        cmds.matchTransform(ctrl_Ik_Finger_Thumb,joint_Thumb_T_Lt)
        cmds.select(ctrl_Ik_Finger_Thumb+'.cv[0:52]')
        cmds.scale(0.5, 0.5, 0.5, relative=True)
        cmds.move(0, 0, 0, relative=True)
        


        curve_pole_Vector_Thumb = cmds.curve(n='Crv_PV_Thumb_Lt', degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                point = [(-2, 0, 0),\
                         (1, 0, 1),\
                         (1, 0, -1),\
                         (-2, 0, 0),\
                         (1, 1, 0),\
                         (1, 0, 0),\
                         (1, -1, 0),\
                         (-2, 0, 0)]\
              )

        cmds.addAttr(curve_pole_Vector_Thumb, longName='Guide_Visibility', attributeType='bool', dv=True, k=True )
        cmds.addAttr(curve_pole_Vector_Thumb, longName='Space', attributeType='enum', enumName="World:Hand:Ik_Finger", k=True )
        cmds.setAttr(curve_pole_Vector_Thumb + ".Space", 1)
        cmds.matchTransform(curve_pole_Vector_Thumb,joint_Thumb_3_Lt)
        cmds.select(curve_pole_Vector_Thumb)
        cmds.move(0, 3, 0, relative=True, os=True)
        cmds.select(curve_pole_Vector_Thumb+'.cv[0:7]')
        cmds.rotate(0, 0, 90, relative=True)
        cmds.scale(0.5, 0.5, 0.5, relative=True)

        





        ctrl_finger_Thumb = [ctrl_finger_1_Thumb,ctrl_finger_2_Thumb,ctrl_finger_3_Thumb,ctrl_finger_4_Thumb,ctrl_Ik_Finger_Thumb,curve_pole_Vector_Thumb]
        for offset in ctrl_finger_Thumb :
            cmds.select(offset)
            OFF()

        
        ctrl_finger_1_Thumb_OFF = cmds.listRelatives(ctrl_finger_1_Thumb, parent=True, fullPath=True)
        ctrl_finger_2_Thumb_OFF = cmds.listRelatives(ctrl_finger_2_Thumb, parent=True, fullPath=True)
        ctrl_finger_3_Thumb_OFF = cmds.listRelatives(ctrl_finger_3_Thumb, parent=True, fullPath=True)
        ctrl_finger_4_Thumb_OFF = cmds.listRelatives(ctrl_finger_4_Thumb, parent=True, fullPath=True)
        
        
        
        cmds.parent(ctrl_finger_4_Thumb_OFF, ctrl_finger_3_Thumb)
        cmds.parent(ctrl_finger_3_Thumb_OFF, ctrl_finger_2_Thumb)
        cmds.parent(ctrl_finger_2_Thumb_OFF, ctrl_finger_1_Thumb)

        cmds.parentConstraint( ctrl_finger_1_Thumb, joint_Thumb_1_Lt )
        cmds.parentConstraint( ctrl_finger_2_Thumb, joint_Thumb_2_Lt )
        cmds.parentConstraint( ctrl_finger_3_Thumb, joint_Thumb_3_Lt )
        cmds.parentConstraint( ctrl_finger_4_Thumb, joint_Thumb_4_Lt )
        


        cmds.setAttr(joint_DRV_Thumb_3_Lt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Thumb_4_Lt + '.preferredAngleZ', -10.0)

        ik_Handle_Thumb_Lt = cmds.ikHandle(n='IKRP_Thumb_Lt',  sj=joint_DRV_Thumb_2_Lt, ee=joint_DRV_Thumb_T_Lt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Thumb_Lt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Thumb_Lt[0], ctrl_Ik_Finger_Thumb)
        cmds.poleVectorConstraint( curve_pole_Vector_Thumb, ik_Handle_Thumb_Lt[0] )
        


        new_Effector_name_Thumb = 'EFF_IKRP_Thumb_Lt'
        List_Input_Ik_Handle_Thumb = cmds.listConnections('IKRP_Thumb_Lt',s=True)
        for node in List_Input_Ik_Handle_Thumb:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Thumb)
                break
        
        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Thumb_OFF = cmds.listRelatives(ctrl_finger_1_Thumb, parent=True, fullPath=True)
        ctrl_finger_2_Thumb_OFF = cmds.listRelatives(ctrl_finger_2_Thumb, parent=True, fullPath=True)
        ctrl_finger_3_Thumb_OFF = cmds.listRelatives(ctrl_finger_3_Thumb, parent=True, fullPath=True)
        ctrl_finger_4_Thumb_OFF = cmds.listRelatives(ctrl_finger_4_Thumb, parent=True, fullPath=True)
        curve_pole_Vector_Thumb_OFF = cmds.listRelatives(curve_pole_Vector_Thumb, parent=True, fullPath=True)
        ctrl_Ik_Finger_Thumb_OFF = cmds.listRelatives(ctrl_Ik_Finger_Thumb, parent=True, fullPath=True)
        
        decompose_M_DRV_Thumb_1_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_1_Lt')
        decompose_M_DRV_Thumb_2_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_2_Lt')
        decompose_M_DRV_Thumb_3_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_3_Lt')
        decompose_M_DRV_Thumb_4_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_4_Lt')

        cmds.connectAttr( f'{joint_DRV_Thumb_1_Lt}.xformMatrix', f'{decompose_M_DRV_Thumb_1_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_2_Lt}.xformMatrix', f'{decompose_M_DRV_Thumb_2_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_3_Lt}.xformMatrix', f'{decompose_M_DRV_Thumb_3_Lt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_4_Lt}.xformMatrix', f'{decompose_M_DRV_Thumb_4_Lt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Thumb_1_Lt}.outputTranslate', f'{ctrl_finger_1_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_2_Lt}.outputTranslate', f'{ctrl_finger_2_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_3_Lt}.outputTranslate', f'{ctrl_finger_3_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_4_Lt}.outputTranslate', f'{ctrl_finger_4_Thumb_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Thumb_1_Lt}.outputRotate', f'{ctrl_finger_1_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_2_Lt}.outputRotate', f'{ctrl_finger_2_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_3_Lt}.outputRotate', f'{ctrl_finger_3_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_4_Lt}.outputRotate', f'{ctrl_finger_4_Thumb_OFF[0]}.rotate' )


        cmds.select(deselect=True)
        joint_Thumb_knuckle = cmds.joint(  n='Sk_Thumb_Knuckle_Lt' , rad=0.75)
        cmds.matchTransform(joint_Thumb_knuckle,joint_Thumb_2_Lt)
        cmds.parent(joint_Thumb_knuckle, joint_Thumb_2_Lt )
        

        multiply_divide_value_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Thumb_Lt')
        multiply_divide_lower_intensity_knuckle_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Thumb_Lt')
        multiply_divide_intensity_knuckle_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Thumb_Lt')
        condition_positive_tendon_Thumb = cmds.createNode( 'condition', n='condition_positive_tendon_Thumb_Lt')

        cmds.setAttr(multiply_divide_value_tendon_Thumb + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Thumb + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Thumb + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Thumb + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Thumb + '.operation', 2)

        cmds.connectAttr( f'{joint_Thumb_2_Lt}.rotateZ', f'{condition_positive_tendon_Thumb}.firstTerm' )
        cmds.connectAttr( f'{joint_Thumb_2_Lt}.rotateZ', f'{multiply_divide_value_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{joint_Thumb_2_Lt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Thumb}.outColorR', f'{multiply_divide_value_tendon_Thumb}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Thumb}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Thumb}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Thumb}.outputY', f'{joint_Thumb_knuckle}.translateY' )

    
        cmds.connectAttr( f'{controler_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input2Y' )

        cmds.select(deselect=True)
        ctrls_Thumb_to_goup = [ctrl_Ik_Finger_Thumb_OFF[0], curve_pole_Vector_Thumb_OFF[0], ctrl_finger_1_Thumb_OFF[0]]
        group_ctrls_Thumb_Lt = cmds.group(em=True, name='Grp_Ctrls_Thumb_Lt')
        cmds.parent(ctrls_Thumb_to_goup, group_ctrls_Thumb_Lt)

        
        joint_Thumb_to_goup = [joint_Thumb_1_Lt, joint_DRV_Thumb_1_Lt ]
        group_joints_Thumb_Lt = cmds.group(em=True, name='Grp_Sk_Thumb_Lt')
        cmds.parent(joint_Thumb_to_goup, group_joints_Thumb_Lt)







        #guide visual pv 
        locator_pv_start_Thumb_ctrl_Lt = cmds.spaceLocator(n='LOC_Start_Guide_PV_Thumb_Lt', p=(0, 0, 0), )
        cmds.matchTransform(locator_pv_start_Thumb_ctrl_Lt, joint_Thumb_3_Lt)
        cmds.setAttr(locator_pv_start_Thumb_ctrl_Lt[0] + '.visibility', 0 )
        locator_pv_end_Thumb_ctrl_Lt = cmds.spaceLocator( n='LOC_End_Guide_PV_Thumb_Lt', p=(0, 0, 0)  )
        cmds.matchTransform(locator_pv_end_Thumb_ctrl_Lt, curve_pole_Vector_Thumb)
        cmds.setAttr(locator_pv_end_Thumb_ctrl_Lt[0] + '.visibility', 0 )

        locator_pv_start_Thumb_ctrl_Lt_position = cmds.xform(locator_pv_start_Thumb_ctrl_Lt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Thumb_ctrl_Lt_position = cmds.xform(locator_pv_end_Thumb_ctrl_Lt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Thumb_ctrl_Lt = cmds.curve(d=1, p=[locator_pv_start_Thumb_ctrl_Lt_position, locator_pv_end_Thumb_ctrl_Lt_position], n='Guide_PV_Thumb_Lt')

        decompose_M_curve_start_Thumb_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Thumb_Lt')
        decompose_M_curve_end_Thumb_Lt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Thumb_Lt')


           
        cmds.connectAttr( f'{locator_pv_start_Thumb_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_start_Thumb_Lt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Thumb_ctrl_Lt[0]}.worldMatrix[0]', f'{decompose_M_curve_end_Thumb_Lt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Thumb_Lt}.outputTranslate', f'{curve_pv_Thumb_ctrl_Lt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Thumb_Lt}.outputTranslate', f'{curve_pv_Thumb_ctrl_Lt}.controlPoints[1]' )

        cmds.parent(locator_pv_end_Thumb_ctrl_Lt, curve_pole_Vector_Thumb)
        cmds.parent(locator_pv_start_Thumb_ctrl_Lt, joint_Thumb_3_Lt)

        cmds.setAttr(curve_pv_Thumb_ctrl_Lt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Guide_Visibility', f'{curve_pv_Thumb_ctrl_Lt}.visibility' )
        


        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Thumb_Lt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Thumb_ctrl_Lt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Thumb_Lt', p=(0, 0, 0), )
        print(locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Thumb_ctrl_Lt[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt, curve_pole_Vector_Thumb)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Thumb_ctrl_Lt, curve_pole_Vector_Thumb)

        hold_matrix_Thumb_PV_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Thumb_Lt')
        mult_Finger_FingerSpace_PV_Thumb_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Thumb_Lt')
        mult_Finger_HandSpace_PV_Thumb_Lt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Thumb_Lt')
        condition_Finger_Space_PV_Thumb_Lt = cmds.createNode( 'condition', n='Cond_Space_Thumb_PV_Lt')
        condition_Finger_FingerSpace_PV_Thumb_Lt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Thumb_Lt')
        condition_Finger_HandSpace_PV_Thumb_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Thumb_Lt')

        blend_matrix_PV_Thumb_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Thumb_Lt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_PV_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_PV_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Thumb_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Thumb_ctrl_Lt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Thumb_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Thumb_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_PV_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_PV_Thumb_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Thumb_Lt}.matrixSum', f'{blend_matrix_PV_Thumb_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Thumb_Lt}.matrixSum', f'{blend_matrix_PV_Thumb_Lt}.target[0].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_FingerSpace_PV_Thumb_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_HandSpace_PV_Thumb_Lt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_Space_PV_Thumb_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Thumb_Lt}.outColorR', f'{condition_Finger_Space_PV_Thumb_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Thumb_Lt}.outColorR', f'{condition_Finger_Space_PV_Thumb_Lt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Thumb_Lt}.outColorR', f'{blend_matrix_PV_Thumb_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Thumb_Lt}.outColorG', f'{blend_matrix_PV_Thumb_Lt}.target[1].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Thumb_Lt}.outputMatrix', f'{curve_pole_Vector_Thumb}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Thumb_ctrl_Lt, ctrl_Ik_Finger_Thumb) #et on parente direct le locator de l'ik 





        #Space controller IK a 4 choix

        locator_Finger_HandSpace_IK_Thumb_ctrl = cmds.spaceLocator(n='LOC_Finger_HandSpace_IK_Thumb_Lt', p=(0, 0, 0), )
        locator_Finger_HeadSpace_IK_Thumb_ctrl = cmds.spaceLocator(n='LOC_Finger_HeadSpace_IK_Thumb_Lt', p=(0, 0, 0), )
        locator_Finger_HipSpace_IK_Thumb_ctrl = cmds.spaceLocator(n='LOC_Finger_HipSpace_IK_Thumb_Lt', p=(0, 0, 0), )
        cmds.setAttr(locator_Finger_HandSpace_IK_Thumb_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HeadSpace_IK_Thumb_ctrl[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HipSpace_IK_Thumb_ctrl[0] + '.visibility', 0)
        cmds.matchTransform(locator_Finger_HandSpace_IK_Thumb_ctrl,ctrl_Ik_Finger_Thumb)
        cmds.matchTransform(locator_Finger_HeadSpace_IK_Thumb_ctrl,ctrl_Ik_Finger_Thumb)
        cmds.matchTransform(locator_Finger_HipSpace_IK_Thumb_ctrl,ctrl_Ik_Finger_Thumb)

        hold_matrix_Thumb_IK_Ctrl_Lt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Thumb_Lt')
        mult_Finger_HandSpace_IK_Thumb_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Thumb_Lt')
        mult_Finger_HeadSpace_IK_Thumb_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Thumb_Lt')
        mult_Finger_HipSpace_IK_Thumb_Lt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Thumb_Lt')
        condition_Finger_Space_IK_Thumb_Lt = cmds.createNode( 'condition', n='Cond_Space_Thumb_Lt')
        condition_Finger_HandSpace_IK_Thumb_Lt = cmds.createNode( 'condition', n='Cond_HandSpace_Thumb_Lt')
        condition_Finger_HeadSpace_IK_Thumb_Lt = cmds.createNode( 'condition', n='Cond_HeadSpace_Thumb_Lt')
        condition_Finger_HipSpace_IK_Thumb_Lt = cmds.createNode( 'condition', n='Cond_HipSpace_Thumb_Lt')

        blend_matrix_IK_Thumb_Lt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Thumb_Lt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Lt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Lt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Lt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Lt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Lt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Lt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_IK_Ctrl_Lt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_IK_Ctrl_Lt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Thumb_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Thumb_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Thumb_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Thumb_ctrl[0]}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Thumb_Lt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HandSpace_IK_Thumb_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Thumb_Lt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Lt}.outMatrix', f'{mult_Finger_HipSpace_IK_Thumb_Lt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Thumb_Lt}.matrixSum', f'{blend_matrix_IK_Thumb_Lt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Thumb_Lt}.matrixSum', f'{blend_matrix_IK_Thumb_Lt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Thumb_Lt}.matrixSum', f'{blend_matrix_IK_Thumb_Lt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HandSpace_IK_Thumb_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HeadSpace_IK_Thumb_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HipSpace_IK_Thumb_Lt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_Space_IK_Thumb_Lt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Thumb_Lt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Lt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Thumb_Lt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Lt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Thumb_Lt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Lt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Lt}.outColorR', f'{blend_matrix_IK_Thumb_Lt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Lt}.outColorG', f'{blend_matrix_IK_Thumb_Lt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Lt}.outColorB', f'{blend_matrix_IK_Thumb_Lt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Thumb_Lt}.outputMatrix', f'{ctrl_Ik_Finger_Thumb}.offsetParentMatrix' )


            #on range les locator space dans les bon endroit

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Lt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Thumb_ctrl[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Thumb_ctrl[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Thumb_ctrl[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Thumb_ctrl_Lt[0], sk_Hand)
            
            
        else :
            group_miror_Thumb_Loc_Space_IK_temp_Lt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Thumb_A_PARENTER_Lt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Thumb_ctrl[0], locator_Finger_HeadSpace_IK_Thumb_ctrl[0], locator_Finger_HipSpace_IK_Thumb_ctrl[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Thumb_Loc_Space_IK_temp_Lt)


        cmds.select(deselect=True)
        list_set_skin_jnt = [joint_Thumb_1_Lt, joint_Thumb_2_Lt, joint_Thumb_3_Lt, joint_Thumb_4_Lt, joint_Thumb_knuckle]
        set_name = "MySetJointSkin"
        if cmds.objExists(set_name):
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)
        
        else:
            cmds.sets(n=set_name)
            for joints in list_set_skin_jnt : 
                cmds.sets(joints, e=True, forceElement=set_name)



        #rangement dans les groupes


        grp_Controllers = 'Grp_Controllers'
        grp_Skeleton = 'Grp_Skeleton'
        grp_DO_NOT_TOUCH = 'DO_NOT_TOUCH'
        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'


        if not cmds.objExists('Grp_DNT_Hand_Lt'):
            grp_DNT_Hand_Lt = cmds.group(em=True, name='Grp_DNT_Hand_Lt')


        grp_elem_DNT_Thumb = [curve_pv_Thumb_ctrl_Lt]


        cmds.parent(grp_elem_DNT_Thumb, grp_DNT_Hand_Lt )


        if cmds.objExists(grp_Controllers):
            cmds.parent(group_ctrls_Thumb_Lt, grp_Controllers)
        else:
            grp_Controllers = cmds.group(em=True, name='Grp_Controllers')
            cmds.parent(group_ctrls_Thumb_Lt, grp_Controllers)


        if cmds.objExists(grp_Skeleton):
            cmds.parent(group_joints_Thumb_Lt, grp_Skeleton)
        else:
            grp_Skeleton = cmds.group(em=True, name='Grp_Skeleton')
            cmds.parent(group_joints_Thumb_Lt, grp_Skeleton)


        if cmds.objExists(grp_DO_NOT_TOUCH):
            if cmds.objExists('Grp_DNT_Hand_Lt'):
                parent_of_grp_DNT_Hand_Lt = cmds.listRelatives(grp_DNT_Hand_Lt, parent=True)
                if not parent_of_grp_DNT_Hand_Lt:
                    cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)
        else:
            grp_DO_NOT_TOUCH = cmds.group(em=True, name='DO_NOT_TOUCH')
            cmds.parent(grp_DNT_Hand_Lt, grp_DO_NOT_TOUCH)




         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{controler_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Thumb}.visibility' )    


        #on fait la parentée pour que les mains suivent la structure generale

        DRV_Palm_IK_Lt = "DRV_Palm_IK_Lt"
        if cmds.objExists(DRV_Palm_IK_Lt):
            cmds.parentConstraint(DRV_Palm_IK_Lt, joint_DRV_Thumb_1_Lt, mo=True) 


        #couleurs des controllers 
        jnt_color_Blue = [ctrl_finger_1_Thumb, ctrl_finger_2_Thumb, ctrl_finger_3_Thumb, ctrl_finger_4_Thumb, ctrl_Ik_Finger_Thumb]
        jnt_color_DarkBlue = [ctrl_finger_3_Thumb, ctrl_finger_4_Thumb]
        jnt_color_beige= [curve_pole_Vector_Thumb]
        

        for objcolor_Blue in jnt_color_Blue : 
            cmds.setAttr(objcolor_Blue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Blue + '.overrideColor', 6)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 5)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)


        ###

    def thumb_rig_Part_3_Miror(*args):

        duplication_group_ctrls_sk = cmds.duplicate(group_ctrls_Thumb_Lt, group_joints_Thumb_Lt, rc=True)
        

        for Delnode in duplication_group_ctrls_sk: 
            stThumb_del = ['EFF', 'Constraint', 'IKRP_Thumb_Lt', 'LOC_Finger_FingerSpace_PV_Thumb_Lt1']
            for substThumb in stThumb_del:
                if Delnode.find(substThumb) != -1 and cmds.objExists(Delnode):
                    cmds.delete(Delnode)


             
        
        for rename in duplication_group_ctrls_sk:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        group_ctrls_Thumb_Rt = 'Grp_Ctrls_Thumb_Rt'
        group_joints_Thumb_Rt = 'Grp_Sk_Thumb_Rt'
        # group_miror_Thumb_Loc_Space_IK_temp_Rt = 'Grp_LOC_Space_Ik_Finger_Thumb_A_PARENTER_Rt'
        
    
        cmds.setAttr(group_ctrls_Thumb_Rt + '.scaleX', -1 )
        cmds.setAttr(group_joints_Thumb_Rt + '.scaleX', -1 )
        # cmds.setAttr(group_miror_Thumb_Loc_Space_IK_temp_Rt + '.scaleX', -1 )


        #réassignation des varables pour le miror
        ctrl_finger_1_Thumb = 'Ctrl_Finger_1_Thumb_Rt'
        ctrl_finger_2_Thumb = 'Ctrl_Finger_2_Thumb_Rt'
        ctrl_finger_3_Thumb = 'Ctrl_Finger_3_Thumb_Rt'
        ctrl_finger_4_Thumb = 'Ctrl_Finger_4_Thumb_Rt'
        curve_pole_Vector_Thumb = 'Crv_PV_Thumb_Rt'
        ctrl_Ik_Finger_Thumb = 'Ctrl_IK_Thumb_Rt'

        joint_DRV_Thumb_1_Rt = 'DRV_Thumb_1_Rt'
        joint_DRV_Thumb_2_Rt = 'DRV_Thumb_2_Rt'
        joint_DRV_Thumb_3_Rt = 'DRV_Thumb_3_Rt'
        joint_DRV_Thumb_4_Rt = 'DRV_Thumb_4_Rt'
        joint_DRV_Thumb_T_Rt = 'DRV_Thumb_T_Rt'
        joint_Thumb_1_Rt = 'Sk_Thumb_1_Rt'
        joint_Thumb_2_Rt = 'Sk_Thumb_2_Rt'
        joint_Thumb_3_Rt = 'Sk_Thumb_3_Rt'
        joint_Thumb_4_Rt = 'Sk_Thumb_4_Rt'
        joint_Thumb_T_Rt = 'Sk_Thumb_T_Rt'
        joint_Thumb_Tendon_1_Rt = 'Sk_Thumb_Tendon_1_Rt'
        joint_Thumb_Tendon_2_Rt = 'Sk_Thumb_Tendon_2_Rt'
        joint_Thumb_Tendon_3_Rt = 'Sk_Thumb_Tendon_3_Rt'
        joint_Thumb_Tendon_4_Rt = 'Sk_Thumb_Tendon_4_Rt'
        joint_Thumb_knuckle = 'Sk_Thumb_Knuckle_Rt'
  
        duplication_ctrl_hand_control = 'Ctrl_Control_Hand_Rt'
        locator_pv_start_Thumb_ctrl_Rt = 'LOC_Start_Guide_PV_Thumb_Rt'
        locator_pv_end_Thumb_ctrl_Rt = 'LOC_End_Guide_PV_Thumb_Rt'
   


        '''
        duplication du code au dessus qui suit

        '''

        



        cmds.parentConstraint( ctrl_finger_1_Thumb, joint_Thumb_1_Rt )
        cmds.parentConstraint( ctrl_finger_2_Thumb, joint_Thumb_2_Rt )
        cmds.parentConstraint( ctrl_finger_3_Thumb, joint_Thumb_3_Rt )
        cmds.parentConstraint( ctrl_finger_4_Thumb, joint_Thumb_4_Rt )
        


        cmds.setAttr(joint_DRV_Thumb_3_Rt + '.preferredAngleZ', -10.0)
        cmds.setAttr(joint_DRV_Thumb_4_Rt + '.preferredAngleZ', -10.0)

        ik_Handle_Thumb_Rt = cmds.ikHandle(n='IKRP_Thumb_Rt',  sj=joint_DRV_Thumb_2_Rt, ee=joint_DRV_Thumb_T_Rt, sol='ikRPsolver' )
        cmds.setAttr(ik_Handle_Thumb_Rt[0] + '.visibility', 0 )
        cmds.parent(ik_Handle_Thumb_Rt[0], ctrl_Ik_Finger_Thumb)
        cmds.poleVectorConstraint( curve_pole_Vector_Thumb, ik_Handle_Thumb_Rt[0] )


        new_Effector_name_Thumb = 'EFF_IKRP_Thumb_Rt'
        List_Input_Ik_Handle_Thumb = cmds.listConnections('IKRP_Thumb_Rt',s=True)
        for node in List_Input_Ik_Handle_Thumb:
            
            if node.find('effector') != -1:
                cmds.select(node)
                cmds.rename(new_Effector_name_Thumb)
                break
        

        #bien re set les parent des grp si on fait des parentée 
        ctrl_finger_1_Thumb_OFF = cmds.listRelatives(ctrl_finger_1_Thumb, parent=True, fullPath=True)
        ctrl_finger_2_Thumb_OFF = cmds.listRelatives(ctrl_finger_2_Thumb, parent=True, fullPath=True)
        ctrl_finger_3_Thumb_OFF = cmds.listRelatives(ctrl_finger_3_Thumb, parent=True, fullPath=True)
        ctrl_finger_4_Thumb_OFF = cmds.listRelatives(ctrl_finger_4_Thumb, parent=True, fullPath=True)
        curve_pole_Vector_Thumb_OFF = cmds.listRelatives(curve_pole_Vector_Thumb, parent=True, fullPath=True)
        ctrl_Ik_Finger_Thumb_OFF = cmds.listRelatives(ctrl_Ik_Finger_Thumb, parent=True, fullPath=True)
        
        decompose_M_DRV_Thumb_1_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_1_Rt')
        decompose_M_DRV_Thumb_2_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_2_Rt')
        decompose_M_DRV_Thumb_3_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_3_Rt')
        decompose_M_DRV_Thumb_4_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_DRV_Thumb_4_Rt')

        cmds.connectAttr( f'{joint_DRV_Thumb_1_Rt}.xformMatrix', f'{decompose_M_DRV_Thumb_1_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_2_Rt}.xformMatrix', f'{decompose_M_DRV_Thumb_2_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_3_Rt}.xformMatrix', f'{decompose_M_DRV_Thumb_3_Rt}.inputMatrix' )
        cmds.connectAttr( f'{joint_DRV_Thumb_4_Rt}.xformMatrix', f'{decompose_M_DRV_Thumb_4_Rt}.inputMatrix' )

        cmds.connectAttr( f'{decompose_M_DRV_Thumb_1_Rt}.outputTranslate', f'{ctrl_finger_1_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_2_Rt}.outputTranslate', f'{ctrl_finger_2_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_3_Rt}.outputTranslate', f'{ctrl_finger_3_Thumb_OFF[0]}.translate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_4_Rt}.outputTranslate', f'{ctrl_finger_4_Thumb_OFF[0]}.translate' )

        cmds.connectAttr( f'{decompose_M_DRV_Thumb_1_Rt}.outputRotate', f'{ctrl_finger_1_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_2_Rt}.outputRotate', f'{ctrl_finger_2_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_3_Rt}.outputRotate', f'{ctrl_finger_3_Thumb_OFF[0]}.rotate' )
        cmds.connectAttr( f'{decompose_M_DRV_Thumb_4_Rt}.outputRotate', f'{ctrl_finger_4_Thumb_OFF[0]}.rotate' )

 

        multiply_divide_value_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='mD_positive_value_tendon_Thumb_Rt')
        multiply_divide_lower_intensity_knuckle_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='mD_Divide_Intensity_knuckle_tendon_Thumb_Rt')
        multiply_divide_intensity_knuckle_tendon_Thumb = cmds.createNode( 'multiplyDivide', n='Md_Divide_Intensity_knuckle_tendon_Thumb_Rt')
        condition_positive_tendon_Thumb = cmds.createNode( 'condition', n='condition_positive_tendon_Thumb_Rt')

        cmds.setAttr(multiply_divide_value_tendon_Thumb + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.operation', 2)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2X', 100)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2Y', 50)
        cmds.setAttr(multiply_divide_lower_intensity_knuckle_tendon_Thumb + '.input2Z', 100)

        cmds.setAttr(condition_positive_tendon_Thumb + '.secondTerm', 0)
        cmds.setAttr(condition_positive_tendon_Thumb + '.colorIfTrueR', 1)
        cmds.setAttr(condition_positive_tendon_Thumb + '.colorIfFalseR', -1)
        cmds.setAttr(condition_positive_tendon_Thumb + '.operation', 2)

        cmds.connectAttr( f'{joint_Thumb_2_Rt}.rotateZ', f'{condition_positive_tendon_Thumb}.firstTerm' )
        cmds.connectAttr( f'{joint_Thumb_2_Rt}.rotateZ', f'{multiply_divide_value_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{joint_Thumb_2_Rt}.rotateY', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1Z' )

        cmds.connectAttr( f'{condition_positive_tendon_Thumb}.outColorR', f'{multiply_divide_value_tendon_Thumb}.input2X' )

        cmds.connectAttr( f'{multiply_divide_value_tendon_Thumb}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{multiply_divide_value_tendon_Thumb}.outputX', f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.input1Y' )

        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputX', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1X' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputY', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1Y' )
        cmds.connectAttr( f'{multiply_divide_lower_intensity_knuckle_tendon_Thumb}.outputZ', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input1Z' )

        cmds.connectAttr( f'{multiply_divide_intensity_knuckle_tendon_Thumb}.outputY', f'{joint_Thumb_knuckle}.translateY' )
   
    
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.Power_Knuckle', f'{multiply_divide_intensity_knuckle_tendon_Thumb}.input2Y' )
  
        cmds.select(deselect=True)

        

        #miror
        locator_pv_start_Thumb_ctrl_Rt_position = cmds.xform(locator_pv_start_Thumb_ctrl_Rt, query=True, worldSpace=True, translation=True)
        locator_pv_end_Thumb_ctrl_Rt_position = cmds.xform(locator_pv_end_Thumb_ctrl_Rt, query=True, worldSpace=True, translation=True)
        #creation crv
        curve_pv_Thumb_ctrl_Rt = cmds.curve(d=1, p=[locator_pv_start_Thumb_ctrl_Rt_position, locator_pv_end_Thumb_ctrl_Rt_position], n='Guide_PV_Thumb_Rt')

        decompose_M_curve_start_Thumb_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_start_Thumb_Rt')
        decompose_M_curve_end_Thumb_Rt = cmds.createNode( 'decomposeMatrix', n='Decompose_M_curve_end_Thumb_Rt')


           
        cmds.connectAttr( f'{locator_pv_start_Thumb_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_start_Thumb_Rt}.inputMatrix' )
        cmds.connectAttr( f'{locator_pv_end_Thumb_ctrl_Rt}.worldMatrix[0]', f'{decompose_M_curve_end_Thumb_Rt}.inputMatrix' )
        cmds.connectAttr( f'{decompose_M_curve_start_Thumb_Rt}.outputTranslate', f'{curve_pv_Thumb_ctrl_Rt}.controlPoints[0]' )
        cmds.connectAttr( f'{decompose_M_curve_end_Thumb_Rt}.outputTranslate', f'{curve_pv_Thumb_ctrl_Rt}.controlPoints[1]' )

        

        cmds.setAttr(curve_pv_Thumb_ctrl_Rt + '.template', True )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Guide_Visibility', f'{curve_pv_Thumb_ctrl_Rt}.visibility' )




        #Space controller IK a 3 choix rework par ce que il y avait un probleme et manquais de controle

        locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_FingerSpace_PV_Thumb_Rt', p=(0, 0, 0), )
        locator_Finger_HandSpace_PV_Thumb_ctrl_Rt = cmds.spaceLocator(n='LOC_Finger_HandSpace_PV_Thumb_Rt', p=(0, 0, 0))
        cmds.parent(locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt, curve_pole_Vector_Thumb )
        cmds.parent(locator_Finger_HandSpace_PV_Thumb_ctrl_Rt, curve_pole_Vector_Thumb )
        cmds.matchTransform(locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt, curve_pole_Vector_Thumb)
        cmds.matchTransform(locator_Finger_HandSpace_PV_Thumb_ctrl_Rt, curve_pole_Vector_Thumb)
        cmds.setAttr(locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt[0] + '.visibility', 0)
        cmds.setAttr(locator_Finger_HandSpace_PV_Thumb_ctrl_Rt[0] + '.visibility', 0)
        

        hold_matrix_Thumb_PV_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_PV_Thumb_Rt')
        mult_Finger_FingerSpace_PV_Thumb_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_FingerSpace_PV_Thumb_Rt')
        mult_Finger_HandSpace_PV_Thumb_Rt = cmds.createNode( 'multMatrix', n='mM_P_PV_HandSpace_PV_Thumb_Rt')
        condition_Finger_Space_PV_Thumb_Rt = cmds.createNode( 'condition', n='Cond_Space_Thumb_PV_Rt')
        condition_Finger_FingerSpace_PV_Thumb_Rt = cmds.createNode( 'condition', n='Cond_FingerSpace_PV_Thumb_Rt')
        condition_Finger_HandSpace_PV_Thumb_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_PV_Thumb_Rt')

        blend_matrix_PV_Thumb_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_PV_Thumb_Rt')

        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_FingerSpace_PV_Thumb_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HandSpace_PV_Thumb_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_PV_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt[0]}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_PV_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_FingerSpace_PV_Thumb_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HandSpace_PV_Thumb_ctrl_Rt[0]}.worldMatrix[0]', f'{mult_Finger_HandSpace_PV_Thumb_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_FingerSpace_PV_Thumb_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_PV_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_PV_Thumb_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_FingerSpace_PV_Thumb_Rt}.matrixSum', f'{blend_matrix_PV_Thumb_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HandSpace_PV_Thumb_Rt}.matrixSum', f'{blend_matrix_PV_Thumb_Rt}.target[1].targetMatrix' )

        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_FingerSpace_PV_Thumb_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_HandSpace_PV_Thumb_Rt}.firstTerm' )
        cmds.connectAttr( f'{curve_pole_Vector_Thumb}.Space', f'{condition_Finger_Space_PV_Thumb_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_FingerSpace_PV_Thumb_Rt}.outColorR', f'{condition_Finger_Space_PV_Thumb_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HandSpace_PV_Thumb_Rt}.outColorR', f'{condition_Finger_Space_PV_Thumb_Rt}.colorIfFalseG' )

        cmds.connectAttr( f'{condition_Finger_Space_PV_Thumb_Rt}.outColorR', f'{blend_matrix_PV_Thumb_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_PV_Thumb_Rt}.outColorG', f'{blend_matrix_PV_Thumb_Rt}.target[0].weight' )

        cmds.connectAttr( f'{blend_matrix_PV_Thumb_Rt}.outputMatrix', f'{curve_pole_Vector_Thumb}.offsetParentMatrix' )

        cmds.parent(locator_Finger_FingerSpace_PV_Thumb_ctrl_Rt, ctrl_Ik_Finger_Thumb) #et on parente direct le locator de l'ik 




                #Space controller IK a 4 choix MIROR    
        

        # le coté rt ne marche pas avec ça donc il faut venir faire une duplication des anciens locators
            #on vient recuperer les anciens locators
        list_locator_ThumbSpace_dup = [locator_Finger_HipSpace_IK_Thumb_ctrl  , locator_Finger_HeadSpace_IK_Thumb_ctrl ,   locator_Finger_HandSpace_IK_Thumb_ctrl ]

            #on cree une nouvelle liste qui va aceuillir nos nouveaux locators
        new_list_locator_ThumbSpace_dup = []
        for elem in list_locator_ThumbSpace_dup:
            duplication_group_loc_space = cmds.duplicate(elem,  rc=True)
            new_list_locator_ThumbSpace_dup.append(duplication_group_loc_space)

            #on cree le grp temporaire qui va scale -1
        group_miror_locators_ThumbSpace = cmds.group(empty=True, n='Grp_Temp_miror_Loc_Thumb_Rt')

            

            #on parente les nouveaux elements de la nouvelle liste au grp  et ensuite on scale le groupe pour miror
        for elem in new_list_locator_ThumbSpace_dup :
            cmds.parent(elem, group_miror_locators_ThumbSpace)

        cmds.setAttr(group_miror_locators_ThumbSpace + ".scaleX", -1)

            #on vient faire une list relative pour identifier les enfants et pas que ça poe de probleme pour le rename 
        group_miror_locators_ThumbSpace_children = cmds.listRelatives(group_miror_locators_ThumbSpace, c=True)

            #on vient les renommer en rt
        for rename in group_miror_locators_ThumbSpace_children:
            new_name = rename.replace("_Lt1", "_Rt")
            if new_name != rename and cmds.objExists(rename):
                cmds.rename(rename, new_name)

        locator_Finger_HandSpace_IK_Thumb_ctrl_Rt = 'LOC_Finger_HandSpace_IK_Thumb_Rt'
        locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt = 'LOC_Finger_HeadSpace_IK_Thumb_Rt'
        locator_Finger_HipSpace_IK_Thumb_ctrl_Rt = 'LOC_Finger_HipSpace_IK_Thumb_Rt'

        
        cmds.select(locator_Finger_HandSpace_IK_Thumb_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt)
        OFF()
        cmds.select(locator_Finger_HipSpace_IK_Thumb_ctrl_Rt)                
        OFF()
        

        

        locator_Finger_HandSpace_IK_Thumb_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HandSpace_IK_Thumb_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt, parent=True, fullPath=True)
        locator_Finger_HipSpace_IK_Thumb_ctrl_Rt_OFF = cmds.listRelatives(locator_Finger_HipSpace_IK_Thumb_ctrl_Rt, parent=True, fullPath=True)
        

        

        hold_matrix_Thumb_IK_Ctrl_Rt = cmds.createNode( 'holdMatrix', n='hM_Inv_W_P_IK_Thumb_Rt')
        mult_Finger_HandSpace_IK_Thumb_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HandSpace_Thumb_Rt')
        mult_Finger_HeadSpace_IK_Thumb_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HeadSpace_Thumb_Rt')
        mult_Finger_HipSpace_IK_Thumb_Rt = cmds.createNode( 'multMatrix', n='mM_P_IK_HipSpace_Thumb_Rt')
        condition_Finger_Space_IK_Thumb_Rt = cmds.createNode( 'condition', n='Cond_Space_Thumb_Rt')
        condition_Finger_HandSpace_IK_Thumb_Rt = cmds.createNode( 'condition', n='Cond_HandSpace_Thumb_Rt')
        condition_Finger_HeadSpace_IK_Thumb_Rt = cmds.createNode( 'condition', n='Cond_HeadSpace_Thumb_Rt')
        condition_Finger_HipSpace_IK_Thumb_Rt = cmds.createNode( 'condition', n='Cond_HipSpace_Thumb_Rt')

        blend_matrix_IK_Thumb_Rt = cmds.createNode( 'blendMatrix', n='bM_P_Space_IK_Thumb_Rt')

        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Rt + '.secondTerm', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Rt + '.secondTerm', 2)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Rt + '.secondTerm', 3)
        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Rt + '.colorIfTrueR', 1)
        cmds.setAttr(condition_Finger_HandSpace_IK_Thumb_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HeadSpace_IK_Thumb_Rt + '.colorIfFalseR', 0)
        cmds.setAttr(condition_Finger_HipSpace_IK_Thumb_Rt + '.colorIfFalseR', 0)
        


        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_IK_Ctrl_Rt}.inMatrix' )
        cmds.disconnectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl_Rt}.worldInverseMatrix[0]', f'{hold_matrix_Thumb_IK_Ctrl_Rt}.inMatrix' )

        cmds.connectAttr( f'{locator_Finger_HandSpace_IK_Thumb_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HandSpace_IK_Thumb_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HeadSpace_IK_Thumb_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{locator_Finger_HipSpace_IK_Thumb_ctrl_Rt}.worldMatrix[0]', f'{mult_Finger_HipSpace_IK_Thumb_Rt}.matrixIn[0]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HandSpace_IK_Thumb_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HeadSpace_IK_Thumb_Rt}.matrixIn[1]' )
        cmds.connectAttr( f'{hold_matrix_Thumb_IK_Ctrl_Rt}.outMatrix', f'{mult_Finger_HipSpace_IK_Thumb_Rt}.matrixIn[1]' )

        cmds.connectAttr( f'{mult_Finger_HandSpace_IK_Thumb_Rt}.matrixSum', f'{blend_matrix_IK_Thumb_Rt}.target[0].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HeadSpace_IK_Thumb_Rt}.matrixSum', f'{blend_matrix_IK_Thumb_Rt}.target[1].targetMatrix' )
        cmds.connectAttr( f'{mult_Finger_HipSpace_IK_Thumb_Rt}.matrixSum', f'{blend_matrix_IK_Thumb_Rt}.target[2].targetMatrix' )

        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HandSpace_IK_Thumb_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HeadSpace_IK_Thumb_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_HipSpace_IK_Thumb_Rt}.firstTerm' )
        cmds.connectAttr( f'{ctrl_Ik_Finger_Thumb}.Space', f'{condition_Finger_Space_IK_Thumb_Rt}.firstTerm' )

        cmds.connectAttr( f'{condition_Finger_HandSpace_IK_Thumb_Rt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Rt}.colorIfFalseR' )
        cmds.connectAttr( f'{condition_Finger_HeadSpace_IK_Thumb_Rt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Rt}.colorIfFalseG' )
        cmds.connectAttr( f'{condition_Finger_HipSpace_IK_Thumb_Rt}.outColorR', f'{condition_Finger_Space_IK_Thumb_Rt}.colorIfFalseB' )

        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Rt}.outColorR', f'{blend_matrix_IK_Thumb_Rt}.target[0].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Rt}.outColorG', f'{blend_matrix_IK_Thumb_Rt}.target[1].weight' )
        cmds.connectAttr( f'{condition_Finger_Space_IK_Thumb_Rt}.outColorB', f'{blend_matrix_IK_Thumb_Rt}.target[2].weight' )

        cmds.connectAttr( f'{blend_matrix_IK_Thumb_Rt}.outputMatrix', f'{ctrl_Ik_Finger_Thumb}.offsetParentMatrix' )  


            #on parente les locators

        sk_Pelvis = "Sk_Pelvis"
        sk_Head = "Sk_Head"
        sk_Hand = "DRV_Palm_IK_Rt"
        


            #Spaces hand
        if cmds.objExists(sk_Pelvis):
            cmds.parent(locator_Finger_HipSpace_IK_Thumb_ctrl_Rt_OFF[0], sk_Pelvis)

        if cmds.objExists(sk_Head):
            cmds.parent(locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt_OFF[0], sk_Head)

        if cmds.objExists(sk_Hand):
            cmds.parent(locator_Finger_HandSpace_IK_Thumb_ctrl_Rt_OFF[0], sk_Hand)
            cmds.parent(locator_Finger_HandSpace_PV_Thumb_ctrl_Rt[0], sk_Hand)
            
            
        else :
            group_miror_Thumb_Loc_Space_IK_temp_Rt = cmds.group(empty=True , n='Grp_LOC_Space_Ik_Finger_Thumb_A_PARENTER_Rt')
            grp_loc_space_IK = [locator_Finger_HandSpace_IK_Thumb_ctrl_Rt_OFF[0], locator_Finger_HeadSpace_IK_Thumb_ctrl_Rt_OFF[0], locator_Finger_HipSpace_IK_Thumb_ctrl_Rt_OFF[0] ]
            cmds.parent(grp_loc_space_IK,group_miror_Thumb_Loc_Space_IK_temp_Rt)
            cmds.select(deselect=True)

        #apres ça on supprime le grp scale -1 des locators 
        cmds.delete(group_miror_locators_ThumbSpace)


        #parenter les crv guides 

        grp_DNT_Hand_Lt = 'Grp_DNT_Hand_Lt'
        cmds.parent(curve_pv_Thumb_ctrl_Rt, grp_DNT_Hand_Lt)


         # ajout de visibility des ctrls FK
        cmds.connectAttr( f'{duplication_ctrl_hand_control}.FK_Finger_Visibility', f'{ctrl_finger_3_Thumb}.visibility' )     


        #on fait la parentée pour que les mains suivent la structure generale
        DRV_Palm_IK_Rt = "DRV_Palm_IK_Rt"
        if cmds.objExists(DRV_Palm_IK_Rt):
            cmds.parentConstraint(DRV_Palm_IK_Rt, joint_DRV_Thumb_1_Rt, mo=True)  

        #couleurs des controllers 
        jnt_color_Red = [ctrl_finger_1_Thumb, ctrl_finger_2_Thumb, ctrl_finger_3_Thumb, ctrl_finger_4_Thumb, ctrl_Ik_Finger_Thumb]
        jnt_color_DarkBlue = [ctrl_finger_3_Thumb, ctrl_finger_4_Thumb]
        jnt_color_beige= [curve_pole_Vector_Thumb]
        

        for objcolor_Red in jnt_color_Red : 
            cmds.setAttr(objcolor_Red + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_Red + '.overrideColor', 13)

        for objcolor_darkblue in jnt_color_DarkBlue : 
            cmds.setAttr(objcolor_darkblue + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_darkblue + '.overrideColor', 18)  #18 bleu clair

        for objcolor_beige in jnt_color_beige : 
            cmds.setAttr(objcolor_beige + '.overrideEnabled', 1)
            cmds.setAttr(objcolor_beige + '.overrideColor', 21)

    def thumb_rig_Suppr(*args): 
        
        thumb_finger_to_suppr = ['Grp_Ctrls_Thumb_Lt', 'Grp_Sk_Thumb_Lt','Guide_PV_Thumb_Lt', 'Grp_LOC_Space_Ik_Finger_Thumb_A_PARENTER_Lt', 'Grp_Ctrls_Thumb_Rt', 'Grp_Sk_Thumb_Rt','Guide_PV_Thumb_Rt', 'Grp_LOC_Space_Ik_Finger_Thumb_A_PARENTER_Rt']
        identify_thumb_finger_to_suppr = cmds.listRelatives(thumb_finger_to_suppr, ad=True)
        list_suppr = [thumb_finger_to_suppr]

        for i in range(100):
            list_suppr.append(identify_thumb_finger_to_suppr)
            identify_thumb_finger_to_suppr = cmds.listConnections(identify_thumb_finger_to_suppr, d=True, s=True)
            
            if not identify_thumb_finger_to_suppr:
                break

        list_suppr_2 = []
        list_Not_Suppr_thumb = ['defaultRenderUtilityList', 'MayaNodeEditorSavedTabsInfo', 'Ctrl_Control_Hand', 'Index', 'Middle', 'Ring', 'Pinky','bindPose','ikRPsolver','ikSCsolver','hikSolver', 'ikSplineSolver','ikSystem','MySetJointSkin']

        for elem in list_suppr:
            for node in elem:
                skip_node = False

                for thumb_name in list_Not_Suppr_thumb:
                    if thumb_name in node:
                        skip_node = True
                        break

                if not skip_node:
                    list_suppr_2.append(node)

        
        cmds.delete(list_suppr_2, hi='none')          
###


    def finger_rig_part_1(*args):
        selected_index = cmds.iconTextScrollList(textScrollRig, query=True, sii=True)
        print(selected_index)
        print('pose')
        if 1 in selected_index :
            thumb_rig_Part_1()

        if 2 in selected_index :
            index_rig_Part_1()

        if 3 in selected_index :
            middle_rig_Part_1()

        if 4 in selected_index :
            ring_rig_Part_1()  

        if 5 in selected_index :
            pinky_rig_Part_1()
    
    def finger_rig_part_2(*args):
        selected_index = cmds.iconTextScrollList(textScrollRig, query=True, sii=True)
        print(selected_index)
        print('pose')
        if 1 in selected_index :
            thumb_rig_Part_2()

        if 2 in selected_index :
            index_rig_Part_2()

        if 3 in selected_index :
            middle_rig_Part_2()

        if 4 in selected_index :
            ring_rig_Part_2()  

        if 5 in selected_index :
            pinky_rig_Part_2()
    
    def finger_rig_part_3_Miror(*args):
        selected_index = cmds.iconTextScrollList(textScrollRig, query=True, sii=True)
        print(selected_index)
        print('pose')
        if 1 in selected_index :
            thumb_rig_Part_3_Miror()

        if 2 in selected_index :
            index_rig_Part_3_Miror()

        if 3 in selected_index :
            middle_rig_Part_3_Miror()

        if 4 in selected_index :
            ring_rig_Part_3_Miror()  

        if 5 in selected_index :
            pinky_rig_Part_3_Miror()
    
    def finger_rig_Suppr(*args):
        selected_index = cmds.iconTextScrollList(textScrollRig, query=True, sii=True)
        print(selected_index)
        print('pose')
        if 1 in selected_index :
            thumb_rig_Suppr()

        if 2 in selected_index :
            index_rig_Suppr()

        if 3 in selected_index :
            middle_rig_Suppr()

        if 4 in selected_index :
            ring_rig_Suppr()  

        if 5 in selected_index :
            pinky_rig_Suppr()
    
    def index_rig_UI(*args):

        global textScrollRig

        window = cmds.window( title="Reine Rig Importer", iconName='Short Name', widthHeight=(450, 375) )
        cmds.columnLayout( adjustableColumn=True )
        

        #
        

        cmds.separator(height=10)
        cmds.columnLayout()
        cmds.columnLayout()
        cmds.button( label='Creation_ctrl_hand_gen' , command=spawn_hand_control_Lt, width=150,  align='center')
        # cmds.button(label='Miror_ctrl_hand_gen' , command=Miror_hand_control_Lt_Rt, width=150,  align='center')
        #####
        cmds.separator(height=20)
        cmds.text( label='Select Finger :' )
        cmds.separator(height=3)
        textScrollRig = cmds.iconTextScrollList(h= 100, ams=True, selectIndexedItem=True, append=('Thumb', 'Index', 'Middle', 'Ring', 'Pinky') ) #1 2 3  4 [5]       
        #    
        cmds.separator(height=10)
        
        cmds.rowLayout( numberOfColumns=5 , columnWidth4=( 30, 75, 75, 75 ),
                            columnAttach=[( 2, 'both', 0 ),( 2, 'both', 0 )] )
        cmds.text( label='RIG' )
        rig1Btn = cmds.button( label='Placement SK Finger',  align='center', command = finger_rig_part_1)
        rig2Btn = cmds.button( label='Execute Auto Rig',   align='center', command = finger_rig_part_2)
        rig3Btn = cmds.button( label='Miror Auto Rig',   align='center', command = finger_rig_part_3_Miror)
        rig4Btn = cmds.button( label='Suppr Rig Finger',   align='center',bgc=[0.5, 0.0, 0.0], command = finger_rig_Suppr)
        cmds.setParent( '..' )
        
        


        cmds.showWindow( window )


    index_rig_UI()

 
    
    
index_rig_lt()

