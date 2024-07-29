import unicodedata

def fmt(input_s = "", max_size = 40, fill_char = " "):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l += 2
        else: 
            l += 1
    return input_s + fill_char * (max_size - l)
# import unicodedata와 def fmt는 곡 목록을 출력할 때 한글이 2비트를 차지하면서 발생하게 되는 행렬 깨짐 현상을 방지하기 위해 가져온 코드입니다.
# 이 함수를 통해 테이블을 출력할 때 일정한 간격으로 단정하게 곡 목록을 출력할 수 있게 되었습니다.

song_list = []          # song_list는 CRUD 기능과 Print 기능을 수행할 때 주로 쓰이는 곡 목록입니다. 초기의 빈 리스트 형태를 정의해주었습니다.
reservation_queue = []  # reservation_queue는 예약 기능을 수행할 때 곡 목록과 따로 예약곡 목록을 관리하기 위해 만든 리스트입니다.
global num              # 나중에 곡 번호를 저장할 때 쓰이는 변수를 global 변수로 정의하였습니다. 그래서 자동적으로 번호의 숫자가 증가할 수 있게 하였습니다.
num = 0

class song_info:                                       # 곡의 정보를 받을 때 사용할 클래스를 정의하였습니다. 
    def __init__(self, number, title, artist, genre):  # def __init__ 으로 곡 정보를 객체의 형태로 받았습니다.
        self.number = number
        self.title = title
        self.artist = artist
        self.genre = genre

    def print_info(self):  # def print_info 함수를 호출했을 때 곡의 목록을 테이블 형태로 출력하도록 포맷을 만들었습니다.
        print(fmt(str(self.number), max_size = 10), fmt(self.title, max_size = 50), fmt(self.artist, max_size = 50), fmt(self.genre, max_size = 20))
        
def print_menu():  # 프로그램을 시행하거나 다시 초기 화면으로 돌아갔을 때 출력될 코드를 작성하였습니다.
    print("<노래방 곡 관리 프로그램>\n\n>> 어떤 작업을 수행하시겠습니까?\n")
    print("1. 곡 추가하기\n2. 곡 검색하기\n3. 곡 정보 수정하기\n4. 곡 삭제하기\n5. 곡 전체 정보 출력하기\n6. 곡 예약하기\n7. 예약 확인\n8. 시작\n9. 예약 취소\n0. 종료하기\n")
    select = input("▷ 수행할 작업의 번호를 입력해주세요: ")
    return select

def create():       # 곡을 추가하고자 할 때 실행될 함수를 정의하였습니다. 제목, 가수, 장르를 입력받아 위에서 정의한 song_info 클래스를 호출해 그 객체에 입력된 정보를 저장하여 return하게 만들었습니다.
    print(">> 어떤 곡을 추가하시겠습니까? (제목, 가수, 장르 순으로 입력해주세요): ")
    global num
    num = num + 1   # 여기서 각 곡들의 고유번호의 경우 곡 하나를 추가할 때마다 숫자가 1씩 늘어나도록 설정했습니다.
    title = input("▷ 제목: ")
    artist = input("▷ 가수: ")
    genre = input("▷ 장르 (발라드, 알앤비, 댄스, 힙합, 트로트, 기타): ")
    print("추가되었습니다.\n")
    Song_Info = song_info(num, title, artist, genre)
    return Song_Info

def retrieve():                                       # 곡을 검색하려고 할 때 실행될 함수를 정의하였습니다. 무엇을 검색할지 선택한 것과 검색어 두 가지를 입력받는 함수를 마지막에 호출하였습니다.
    while 1:
        print("\n>> 무엇을 검색하시겠습니까?\n")
        print("A. 번호 검색\nB. 제목 검색\nC. 가수 검색\nD. 장르 검색\n")
        search = input("▷ 선택해주세요: ").upper()   # 검색 기준을 선택할 때 알파벳을 입력하는데, 알파벳을 대소문자 구분 없이 입력이 가능하게 했습니다.
        if search == 'A' or search == 'B' or search == 'C' or search == 'D':
            keyword = input("\n▷ 검색어를 입력해주세요: ")
            break
        else:                                         # 사용자가 A, B, C, D가 아닌 다른 문자를 입력했을 때 다시 고르라는 예외 처리를 해주었습니다.
            print('\n해당 번호에 속하는 메뉴가 없습니다. 다시 선택해주세요.\n')
            continue
    return search_songs(search, keyword)
    


def search_songs(search_menu, key_word):                                          # 무엇을 검색할지 선택한 것에 따라 조건을 부여하고, 검색어와 일치하는 인덱스의 곡 정보를 호출해주는 함수를 정의했습니다.
    search_list = []
    if search_menu == 'A':
        for song in song_list:
            if song.number == int(key_word):
                search_list.append(song)

    elif search_menu == 'B':
        for song in song_list:
            if song.title.replace(' ', '').find(key_word.replace(' ','')) != -1:  # 입력한 검색어에 따라 검색을 할 때에도, 찾고자 하는 정보의 일부만 포함해서 입력하기만 해도 검색이 될 수 있게 구현하였습니다. 띄어쓰기의 경우에도 그 유무 상관없이 띄어쓰기를 제외하고 부분 포함으로 검색하게 했습니다.
                search_list.append(song)
                
    elif search_menu == 'C':
        for song in song_list:
            if song.artist.replace(' ','').find(key_word.replace(' ','')) != -1:
                search_list.append(song)

    elif search_menu == 'D':
        for song in song_list:
            if song.genre == key_word:
                search_list.append(song)
    
    return search_list

def update_song():                                                                        # 곡 정보를 수정하고 싶을 때 실행될 함수를 정의하였습니다. 수정할 곡의 번호와 수정할 카테고리, 그리고 수정할 사항을 입력받아 일치하는 인덱스에 해당 수정 사항을 적용할 수 있게 만들었습니다.
    song_num = int(input("\n▷ 수정할 곡의 번호를 입력해주세요 : "))
    C = 0                                                                                 # 원활한 예외 처리를 위해 수정과 관련된 코드가 수행될지 말지 판단해주는 기준이 되는 하나의 변수를 정의해주었습니다.
    for song in song_list:
        if song.number == song_num:                                                       # 수정하고 싶은 곡의 번호를 입력했을 때, 곡 목록에 일치하는 번호가 있으면 위에서 정의한 변수 C에 1을 더해줘서, 아래의 while문이 실행되도록 했습니다.
            C = C + 1
            while 1:
                print("\nA. 곡 제목 수정\nB. 가수 수정\nC. 장르 수정\n")
                update_menu = input("\n▷ 수정하고 싶은 사항을 선택해주세요 : ").upper()  # 알파벳을 대소문자 구분 없이 입력이 가능하게 했습니다.
                if (update_menu != 'A' and update_menu != 'B' and update_menu != 'C'):    # 사용자가 A, B, C, D와 일치하지 않는 문자를 입력했을 경우, 다시 선택해달라는 예외 처리를 만들었습니다.
                    print('\n해당 번호에 속하는 메뉴가 없습니다. 다시 선택해주세요.\n')
                    continue
                    
                if update_menu == 'A':
                    update_to = input("\n▷ 수정할 내용을 입력해주세요 : ")
                    song.title = update_to
                    break
                elif update_menu == 'B':
                    update_to = input("\n▷ 수정할 내용을 입력해주세요 : ")
                    song.artist = update_to
                    break
                elif update_menu == 'C':
                    update_to = input("\n▷ 수정할 내용을 (발라드, 알앤비, 댄스, 힙합, 트로트, 기타) 중에서 입력해주세요 : ")
                    song.genre = update_to
                    break
                  
    if C == 0:                                                                            # 수정하고 싶은 곡이 목록에 없을 경우, 변수 C는 그대로 0의 값을 가지고 있을 것입니다. 이때 해당 곡 번호가 없다는 예외 처리를 해주었습니다.
        print("\n해당 곡 번호 없음\n")                            
    else:
        print("\n수정 완료\n")
        
def delete_song():                        #곡 목록에서 곡을 삭제하고 싶을 때 실행할 함수를 정의하였습니다. 삭제할 곡의 번호를 입력받아 일치하는 인덱스를 삭제하게 만들었습니다.
    song_num = int(input("\n▷삭제할 곡의 번호를 입력하세요 : "))
    for i, song in enumerate(song_list):  # enumerate 함수를 활용해서 인덱스와 원소를 차례대로 접근해, 곡 번호가 입력한 숫자와 일치하는 경우에 그 원소를 삭제할 수 있게 작업하였습니다.
        if song.number == song_num:
            del song_list[i]
            print(f"\n{song_num}번 삭제 완료\n")
    
def print_songs(SONGLIST):      # 전체 곡 목록을 출력하고자 할 때 실행할 함수를 정의했습니다.
    print("\n목록")
    print("-----------------------------------------")
    print(fmt("번호", max_size=10),fmt("제목", max_size=50),fmt("가수", max_size=50),fmt("장르", max_size=20))
    for song in SONGLIST:       # 정해둔 포맷에 따라 위에 song_info 클래스에서 정의해준 print_info 함수를 호출해 테이블 형태로 곡 목록이 출력되게 하였습니다.
        song.print_info()
    print("-----------------------------------------\n")
    
def reserve():                              # 예약 기능을 사용하고자 할 때 실행할 함수를 정의했습니다.
    song_num = int(input("\n▷ 예약할 곡의 번호를 입력하세요 : "))
    c = 0                                   # 여기서도 원활한 예외 처리를 위해 변수 c를 정의해주었습니다.
    for song in song_list:
        if song_num == song.number:         # 예약할 곡이 목록에 있을 시, c에 1을 더해주고 예약이 완료되었다는 내용을 출력해줍니다.
            c = c + 1
            print(f"\n{song_num}번 예약 완료!\n")
            reservation_queue.append(song)  # 위에 예약곡 목록을 위해 따로 만들어두었던 리스트에 예약한 곡의 정보를 추가해줍니다.
    if c == 0:                              # 일치하는 곡 번호가 없을 경우 c의 값은 그대로 0일 것이고, 이때 곡 번호가 없다는 예외 처리를 해주었습니다.
        print("\n해당 곡 번호 없음\n")
            
def reserve_check():  # 위에 print_songs 함수에 예약곡 목록 리스트를 삽입하여 예약곡의 전체 목록을 테이블 형태로 출력할 수 있게 만들었습니다.
    print_songs(reservation_queue)
    
def isEmpty(L):  # 예약곡 목록이 비어있는 경우의 예외 처리를 위해 함수를 정의했습니다. 함수가 비어있는 경우 1(True)을 return하고 비어있지 않을 경우 0(False)을 return해줍니다.
    if L == []:  # 값이 1(True)이 될 경우 함수가 실행이 됩니다.
        return 1
    else:
        return 0
    

def start():                        # 예약한 곡을 시작하고자 할 때 실행될 함수를 정의했습니다. 
    if isEmpty(reservation_queue):  # isEmpty 함수를 활용해서 리스트가 비어있을 경우, 예약곡 목록이 비어있다는 예외 처리를 할 수 있게 만들었습니다.
        print("\n예약 목록이 비어있습니다!\n")
    else:                           # 리스트가 비어있지 않을 경우, 리스트의 가장 처음에 있는 곡 정보를 출력해주면서 동시에 제거해줍니다. 출력해줄 때는 노래를 재생한다고 말해줍니다.
        a = reservation_queue[0]
        del reservation_queue[0]
        print(f"\n♬♬ '{a.title}' 재생 ♬♬\n")

def revserve_cancel():              # 예약한 곡을 취소하고자 할 때 실행될 함수를 정의했습니다. 
    if isEmpty(reservation_queue):  # start 함수 때처럼 리스트가 비어있을 경우, 예약곡 목록이 비어있다는 예외 처리를 해주었습니다.
        print("\n예약 목록이 비어있습니다!\n")
    else:                           # 리스트가 비어있지 않을 경우, 리스트의 가장 마지막에 있는 곡 정보를 출력해주면서 동시에 제거해줍니다. 출력해줄 때는 노래를 취소했다고 말해줍니다.
        a = reservation_queue[-1]
        del reservation_queue[-1]
        print(f"\n'{a.title}' 예약 취소\n")

if __name__ == "__main__":
    while 1:
        menu = print_menu()    # 가장 초기 화면에서 print_menu를 호출하여 프로그램을 이용할 수 있게 만들었습니다.
        if menu == '1':        # 1번 메뉴 '곡 추가하기'를 선택하면 create 함수를 호출하여 정보를 입력 받고, 이를 생성되어 있는 class의 객체에 삽입합니다. 그리고 이를 하나의 변수로 받아 배열에 저장합니다.
            song = create()
            song_list.append(song)
        elif menu == '2':      # 2번 메뉴 '곡 검색하기'를 선택하면 retrieve 함수를 호출하여 정보를 입력 받고 결과를 출력해줍니다.
            result = retrieve()
            print_songs(result)
        elif menu == '3':      # 3번 메뉴 '곡 수정하기'를 선택하면 update_song 함수를 호출하여 작업을 수행해줍니다.
            update_song()
        elif menu == '4':      # 4번 메뉴 '곡 삭제하기'를 선택하면 delete_song 함수를 호출하여 작업을 수행해줍니다.
            delete_song()
        elif menu == '5':      # 5번 메뉴 '곡 전체 정보 출력하기'를 선택하면 print_songs 함수에 곡 목록인 song_list를 삽입하여 테이블 형태로 출력해줍니다.
            print_songs(song_list)
        elif menu == '6':      # 6번 메뉴 '곡 예약하기'를 선택하면 reserve 함수를 호출하여 작업을 수행하고, reserve_check 함수로 작업의 결과를 확인해줍니다.
            reserve()
            reserve_check()
        elif menu == '7':      # 7번 메뉴 '예약 확인'을 선택하면 reserve_check 함수를 호출해 전체 예약곡 목록을 출력해줍니다.
            reserve_check()
        elif menu == '8':      # 8번 메뉴 '시작'을 선택하면 start 함수를 호출해 작업을 수행해줍니다.
            start()
        elif menu == '9':      # 9번 메뉴 '예약 취소'를 선택하면 revserve_cancel 함수를 호출해 작업을 수행해줍니다.
            revserve_cancel()
        elif menu == '0':      # 0번 메뉴 '종료하기'를 선택하면 프로그램 자체가 끝나게 됩니다.
            break
        else:                  # 0~9 사이의 번호와 다른 번호를 넣을 경우 해당하는 메뉴가 없다는 예외 처리를 해주었습니다.
            print('\n해당 번호에 속하는 메뉴가 없습니다. 다시 선택해주세요.\n')
            continue
