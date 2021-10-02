import logx
import pybullet as p
import os
import tkinter as tk


class Pybullet:
    def __init__(self, filename):
        p.connect(p.GUI)
        try:
            if os.path.splitext(filename)[-1] == ".urdf":
                self.robot_id = p.loadURDF(filename)
            elif os.path.splitext(filename)[-1] == ".sdf":
                self.robot_id = p.loadSDF(filename)[0]
            elif os.path.splitext(filename)[-1] == ".mjcf":
                self.robot_id = p.loadMJCF(filename)
            else:
                tk.messagebox.showerror(title='类型错误', message='不能打开此类文件')

        except:
            tk.messagebox.showerror(title="导入模型失败",
                                    message="导入模型失败，请检查模型是否依赖了其他文件 (如urdf中import了其他stl文件)，urdf文件及其依赖文件应该放在同一个文件夹中。")
            p.disconnect()

        p.resetDebugVisualizerCamera(cameraDistance=1.5,
                                     cameraYaw=0,
                                     cameraPitch=-40,
                                     cameraTargetPosition=[0, -0.35, 0.2])

    def view_model(self):
        try:
            while True:
                p.stepSimulation()
        except:
            pass

    def add_slidebar(self):
        slide_bars = SlideBars(self.robot_id)
        motor_indices = slide_bars.add_slidebars()
        try:
            while True:
                p.stepSimulation()
                slide_values = slide_bars.get_slidebars_values()
                p.setJointMotorControlArray(self.robot_id, motor_indices, p.POSITION_CONTROL,
                                            targetPositions=slide_values)
        except:
            pass


class SlideBars():
    def __init__(self, Id):
        self.Id = Id
        self.motorNames = []
        self.motorIndices = []
        self.motorLowerLimits = []
        self.motorUpperLimits = []
        self.slideIds = []

        self.numJoints = p.getNumJoints(self.Id)

    def add_slidebars(self):
        for i in range(self.numJoints):
            jointInfo = p.getJointInfo(self.Id, i)
            jointName = jointInfo[1].decode('ascii')
            qIndex = jointInfo[3]
            lowerLimits = jointInfo[8]
            upperLimits = jointInfo[9]
            if qIndex > -1:
                self.motorNames.append(jointName)
                self.motorIndices.append(i)
                self.motorLowerLimits.append(lowerLimits)
                self.motorUpperLimits.append(upperLimits)

        for i in range(len(self.motorIndices)):
            if self.motorLowerLimits[i] <= self.motorUpperLimits[i]:
                slideId = p.addUserDebugParameter(self.motorNames[i], self.motorLowerLimits[i],
                                                  self.motorUpperLimits[i], 0)
            else:
                slideId = p.addUserDebugParameter(self.motorNames[i], self.motorUpperLimits[i],
                                                  self.motorLowerLimits[i], 0)
            self.slideIds.append(slideId)

        return self.motorIndices

    def get_slidebars_values(self):
        slidesValues = []
        for i in self.slideIds:
            value = p.readUserDebugParameter(i)
            slidesValues.append(value)
        return slidesValues
