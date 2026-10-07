import Sensor.SensorController as sensorController
import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

import imutils

def video_play():
    ret, frame = cap.read() # 프레임이 올바르게 읽히면 ret은 True
    frame = cv2.resize(frame,(800,480))
    if not ret:
        cap.release() # 작업 완료 후 해제
        return
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame) # Image 객체로 변환
    global imgtk
    imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, video_play)
    
    '''
    regFrame = tk.Frame(window, bg="white", width=80, height=480)
    nameLabel = tk.Label(regFrame,text="Name", bg="white")
    name = tk.Entry(regFrame)
    pwdLabel = tk.Label(regFrame,text="PassWord", bg="white")
    password = tk.Entry(regFrame, show="*")
    button = tk.Button(regFrame, overrelief="solid",width=10,command=register , repeatdelay=1000, repeatinterval=100,text="등록")
    cancelButton = tk.Button(regFrame, overrelief="solid",width=10,command=cancelFrame, repeatdelay=1000, repeatinterval=100,text="취소")

    regFrame.pack_forget()
    '''
    
    
    
def main(name):

    window=tk.Tk()

    window.title("Face Recognize Door")
    window.geometry("800x480")
    window.resizable(False, False)

    global regFrame
    global button
    global cancelButton
    
    global isFrameOpend
    isFrameOpend = False
    
    def cancelFrame():  
        global isFrameOpend
        isFrameOpend = False
        global regFrame
        nameLabel.pack_forget()
        name.pack_forget()
        pwdLabel.pack_forget()
        password.pack_forget()
        button.pack_forget()
        cancelButton.pack_forget()
        regFrame.pack_forget()
        frm.configure(width=800, height=480)
        lbl1.configure(width=800, height=480)

    def register():
        #얼굴 인식 확인
        password
        #얼굴 데이터 저장 확인

        #file 형태로 저장

    # 실시간 영상 출력 Frame
    frm = tk.Frame(window, bg="black", width=800, height=480) # 프레임 너비, 높이 설정
    global lbl1
    lbl1 = tk.Label(frm)
    lbl1.grid()
    #src = cv2.imread('./Image/1.png')
    #src = cv2.resize(src,(800,480))
    global cap
    cap = cv2.VideoCapture(0)
    
    video_play()
    #label = tk.Label(frm,width=800,height=480,image=imgtk)    

    #label.pack()
    
    
    regFrame = tk.Frame(window, bg="white", width=80, height=480)
    nameLabel = tk.Label(regFrame,text="Name", bg="white")
    name = tk.Entry(regFrame)
    pwdLabel = tk.Label(regFrame,text="PassWord", bg="white")
    password = tk.Entry(regFrame, show="*")
    button = tk.Button(regFrame, overrelief="solid",width=10,command=register , repeatdelay=1000, repeatinterval=100,text="등록")
    cancelButton = tk.Button(regFrame, overrelief="solid",width=10,command=cancelFrame, repeatdelay=1000, repeatinterval=100,text="취소")

    regFrame.pack_forget()
    
    
    def reg(event):
        #이미지 등록
        global isFrameOpend

        if isFrameOpend:
            return

        global regFrame

        isFrameOpend = True
        lbl1.configure(width=720,height=480)
        frm.configure(width=720, height=480)

        regFrame.pack(side="right")
        nameLabel.pack(side="top")
        name.pack(side="top")
        pwdLabel.pack(side="top")
        password.pack(side="top")
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


