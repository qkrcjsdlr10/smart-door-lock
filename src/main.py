import os
import Sensor.SensorController as sensorController
import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk


def main(name):

    window=tk.Tk()

    window.title("Face Recognize Door")
    window.geometry("800x480")
    window.resizable(False, False)

    window.config(background="#202124")
    global regFrame
    global button
    global cancelButton
    global nameId
    global password
    global isFrameOpend
    isFrameOpend = False
    
    global resultLabel
   



    # 실시간 영상 출력 Frame
    frm = tk.Frame(window, bg="black", width=800, height=480) # 프레임 너비, 높이 설정
    # 개인 사진 대신 중립적인 미리보기 영역을 표시합니다.
    frm.pack_propagate(False)
    label = tk.Label(frm, text="Camera preview", bg="black", fg="white")
    label.pack(fill="both", expand=True)

    regFrame = tk.Frame(window, bg="gray", width=80, height=480)
    nameLabel = tk.Label(regFrame,text="Name", bg="#35363a", fg="white", width=10)
    resultLabel = tk.Label(regFrame, text="", bg="#35363a", fg="white", width=10)
    nameId = tk.Entry(regFrame)
    pwdLabel = tk.Label(regFrame,text="PassWord", bg="#35363a", fg="white", width=10)
    password = tk.Entry(regFrame, show="*")

    def register():
        #얼굴 인식 확인
        global resultLabel
        if os.environ.get("SMARTDOOR_ADMIN_PASSWORD") and password.get() == os.environ["SMARTDOOR_ADMIN_PASSWORD"]:
            # 파일명 name
            # 얼굴 데이터 저장
            resultLabel.config(text="Save Success")
        else:
            resultLabel.config(text="Save Fail")
            # 얼굴 temp 삭제

    def cancelFrame():  
        global isFrameOpend
        isFrameOpend = False
        global regFrame
        global nameId
        global password

        nameId.delete(0,100)
        password.delete(0,100)

        resultLabel.config(text="")

        nameLabel.pack_forget()
        nameId.pack_forget()
        pwdLabel.pack_forget()
        password.pack_forget()
        button.pack_forget()
        cancelButton.pack_forget()
        resultLabel.pack_forget()
        regFrame.pack_forget()
        frm.configure(width=800, height=480)
        # 얼굴 temp 삭제


    button = tk.Button(regFrame, overrelief="solid",width=10,command=register , repeatdelay=1000, repeatinterval=100,text="등록", bg="#35363a", fg="white")
    cancelButton = tk.Button(regFrame, overrelief="solid",width=10,command=cancelFrame, repeatdelay=1000, repeatinterval=100,text="취소", bg="#35363a", fg="white")

    regFrame.pack_forget()

    def reg(event):
        #이미지 등록
        global isFrameOpend

        if isFrameOpend:
            return

        global regFrame

        isFrameOpend = True
        frm.configure(width=720, height=480)
        regFrame.pack(side="right")
        nameLabel.pack(side="top")
        nameId.pack(side="top")
        pwdLabel.pack(side="top")
        password.pack(side="top")
        resultLabel.pack(side="top")
        button.pack(side="top")
        cancelButton.pack(side="top")

   
    frm.pack(side="left")

    # camView = tk.Label(frm)
    # camView.grid()

    window.bind("<Button>", reg)

    window.mainloop()
    # 초음파 탐지

    # 화면 켜짐
    # 화면 터치
        # 얼굴 등록 버튼
            # 비밀번호 입력
                # 얼굴 저장 (image file)      
    
    # 얼굴 인식
    # 성공 시
        # 도어 on , 부저 on (success)
        # 5초 뒤 도어 off , 부저 on(success)
    # 실패 시
        # 부저 on (fail)

    # sensorController.MainHandler.init(name)


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    main('PyCharm')

