# 상속 : 부모클래스에서 만든 변수와 메서드를 물려 받아 사용할 수 있음
# 오버라이딩 : 부모 클래스의 메서드를 상속 받아 재정의 하는 것

class ProtoTV: # 상속을 주기 위한 부모 클래스
    # 전원, 채널, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = 1
        self.volume = 0
        self.set_channel(channel)
        self.set_volume(volume)

    # 전원을 켜고 끄는 메서드
    def set_power(self, power):
        self.power = power

    # 채널 설정 메서드
    def set_channel(self, channel):
        if 1 <= channel <= 1000:
            self.channel = channel
            print(f'현재 채널 {channel}')
        else:
            print('채널은 1 ~ 1000까지 설정 가능합니다.')

    # 볼륨 설정 메서드
    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f'현재 볼륨 {volume}')
        else:
            print('볼륨은 0 ~ 100까지 조절 가능합니다.')

    def get_power(self):
        return self.power

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

class ProductTV(ProtoTV):
    def set_channel(self, channel): # 오버라이딩
        if 1 <= channel <= 2000:
            self.channel = channel
            print(f'채널을 {channel}로 변경하였습니다.')
        else:
            print(f'채널 설정 범위가 아닙니다.')

    # 정보를 출력하는 메서드 만들기
    def show_tv(self):
        on_off = ['OFF', 'ON']
        print(f'전원 상태 : {on_off[self.power]}')
        print(f'현재 채널 : {self.channel}')
        print(f'현재 볼륨 : {self.volume}')


product = ProductTV(True, 20, 20)
product.set_power(True)
product.set_channel(1200)
product.set_volume(45)
product.show_tv()
