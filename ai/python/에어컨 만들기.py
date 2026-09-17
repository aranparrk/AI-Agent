# 에어컨 만들기
# 전원 ON/OFF
# 현재 온도 표시 기능 : 기본값은 20도로 설정
# 바람 세기 조절 기능 (1단계, 2단계, 3단계)

class AirCon:
    # 전원, 온도, 바람세기를 매개변수로 전달 받은 생성자 만들기
    def __init__(self, power, wind_speed, temp=20):
        self.power = power
        self.temp = temp
        self.wind_speed = 1
        self.set_wind_speed(wind_speed)

    # 에어컨 ON/OFF
    def set_power(self, power):
        self.power = power

    # 온도 설정
    def set_temp(self, temp):
        self.temp = temp

    # 바람 세기
    def set_wind_speed(self, wind_speed):
        if 1 <= wind_speed <= 3:
            self.wind_speed = wind_speed
        else:
            print('1단계에서 3단계 까지 지정할 수 있습니다.')

    def get_power(self):
        return self.power

    def get_temp(self):
        return self.temp

    def get_wind_speed(self):
        return self.wind_speed

    # 에어컨 정보 표시
    def view_aircon(self):
        power = ('OFF', 'ON')
        print(f'전원 : {power[self.power]}')
        print(f'온도 : {self.temp}')
        print(f'바람세기 : {self.wind_speed}단계')

# 에어컨 객체 생성
aircon = AirCon(True, 3)

aircon.view_aircon()

