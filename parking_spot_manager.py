"""
version #3
parking_spot_manager.py
주차장 정보를 관리하는 모듈

parking_spot class는 주차장 정보 item(name, city, district, ptype, longitude, latitude)를 갖고 있으며,
생성자로 item 필드를 생성/설정 합니다.
get(keyword) 메소드로 해당 keyword 키에 해당하는 item을 반환합니다.

str_list_to_class_list(str_list) 함수는 주차장 정보 문자열 리스트를 parking_spot 객체 리스트로 변환합니다.

print_spots(spots) 함수는 주차장 정보를 출력합니다.

filter_by_name, filter_by_city, filter_by_district, filter_by_ptype 함수는 주차장 정보를 각 keyword 기준으로 필터링합니다.
filter_by_location 함수는 주차장 정보를 경도/위도 범위로 필터링합니다.
"""

class parking_spot:
    """parking spot 정보 클래스
    
    Attributes:
        __item (dict): parking spot 정보를 담고 있는 dictionary

    Methods:
        get(self) : parking spot dictionary 내 key에 해당하는 item을 반환합니다.
        __str__(self) : parking spot dictionary 내 key와 item을 문자열로 변환 후 문자열을 반환합니다.
    """
    __item = None
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """__init__
        parking spot 생성자

        Args:
            name (string): 자원명
            city (string): 시도
            district (string): 시군구
            ptype (string): 주차장 유형
            longitude (float): 경도
            latitude (float): 위도
        """
        self.__item = {
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': float(longitude),
            'latitude': float(latitude),
        }
        
    def get(self, keyword='name'):
        """get
        parking spot dictionary 내 key에 해당하는 item을 반환합니다.

        Args:
            keyword (str, optional): parking spot dictionary 내 key. 기본인수는 name

        Returns:
            string or float: parking spot dictionary 내 key에 해당하는 item 값
        """
        return self.__item.get(keyword)
        
    def __str__(self):
        """__str__
        parking spot 객체의 값을 출력하기 위해 문자열로 변환하는 메소드입니다.

        Returns:
            string: parking spot dictionary 내 key와 item을 값을 문자열 형태로 변환한 문자열
        """
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    """str_list_to_class_list
    주차장 정보 문자열 리스트를 parking_spot 객체 리스트로 변환합니다.

    Args:
        str_list (list): 주차장 정보 문자열 리스트

    Returns:
        list: parking spot 객체 리스트
    """
    spots = []
    for str in str_list:
        spot = str.split(',')
        spots.append(parking_spot(spot[1], spot[2], spot[3], spot[4], spot[5], spot[6]))
    return spots

def print_spots(spots):
    """print_spots
    parking_spot 객체 리스트를 출력합니다.

    Args:
        list : parking_spot 객체 리스트
    """
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)


# version #3 추가 내용
def filter_by_name(spots, name) :
    """filter_by_name
    이름으로 parking_spot 객체 리스트를 필터링합니다.

    Args:
        spots (list): parking_spot 객체 리스트
        name (string): 이름
        
    Returns:
        list: 필터링된 parking_spot 객체 리스트
    """
    return [spot for spot in spots if name in spot.get('name')]


def filter_by_city(spots, city) :
    """filter_by_city
    시도로 parking_spot 객체 리스트를 필터링합니다.

    Args:
        spots (list): parking_spot 객체 리스트
        city (string): 시도
        
    Returns:
        list: 필터링된 parking_spot 객체 리스트
    """
    return [spot for spot in spots if city in spot.get('city')]


def filter_by_district(spots, district) :
    """filter_by_district
    시군구로 parking_spot 객체 리스트를 필터링합니다.

    Args:
        spots (list): parking_spot 객체 리스트
        district (string): 시군구

    Returns:
        list: 필터링된 parking_spot 객체 리스트
    """
    return [spot for spot in spots if district in spot.get('district')]


def filter_by_ptype(spots, ptype) :
    """filter_by_ptype
    주차장유형으로 parking_spot 객체 리스트를 필터링합니다.

    Args:
        spots (list): parking_spot 객체 리스트
        ptype (string): 주차장유형

    Returns:
        list: 필터링된 parking_spot 객체 리스트
    """
    return [spot for spot in spots if ptype in spot.get('ptype')]


def filter_by_location(spots, locations) :
    """filter_by_location
    위도, 경도 범위로 parking_spot 객체 리스트를 필터링합니다.

    Args:
        spots (list): parking_spot 객체 리스트
        locations (tuple): 위도, 경도 범위 (각 최소, 최대 값)
        
    Returns:
        list: 필터링된 parking_spot 객체 리스트
    """
    min_lat, max_lat, min_lon, max_lon = locations
    return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_lon < spot.get('longitude') < max_lon]


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)