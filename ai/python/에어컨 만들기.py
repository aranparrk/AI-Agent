# 에어컨 만들기
# 전원 ON/OFF
# 현재 온도 표시 기능 : 기본값은 20도로 설정
# 온도 조절 기능 : 원하는 온도 설정
# 바람 세기 조절 기능 (1단계, 2단계, 3단계)

class AirCon:
    # 전원, 설정 온도, 바람 세기를 전달받는 생성자
    def __init__(self, power, temp, wind_speed):
        self.power = power
        self.current_temp = 20  # 현재 온도 기본값
        self.temp = temp        # 설정 온도
        self.wind_speed = 1     # 바람 세기 기본값
        self.set_wind_speed(wind_speed)

    # 에어컨 ON/OFF
    def set_power(self, power):
        self.power = power

    # 설정 온도 변경
    def set_temp(self, temp):
        self.temp = temp

    # 바람 세기 변경
    def set_wind_speed(self, wind_speed):
        if 1 <= wind_speed <= 3:
            self.wind_speed = wind_speed
        else:
            print('1단계에서 3단계까지 지정할 수 있습니다.')

    def get_power(self):
        return self.power

    def get_current_temp(self):
        return self.current_temp

    def get_temp(self):
        return self.temp

    def get_wind_speed(self):
        return self.wind_speed

    # 에어컨 정보 표시
    def view_aircon(self):
        power = ('OFF', 'ON')

        print(f'전원 : {power[self.power]}')
        print(f'현재 온도 : {self.current_temp}도')
        print(f'설정 온도 : {self.temp}도')
        print(f'바람 세기 : {self.wind_speed}단계')


# 에어컨 객체 생성
aircon = AirCon(True, 24, 3)

aircon.view_aircon()