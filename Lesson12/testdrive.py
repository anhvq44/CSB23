from mp3player import MP3player

def test_drive():
    mp3 = MP3player()
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    
    print(f'{GREEN}------Trình phát nhạc------{RESET}')
    song_list_len = 0
    while song_list_len==0:
        try:
            song_list_len = int(input("Số lượng bài hát: "))
        except Exception as e:
            print(f"{RED}Lỗi: {str(e)}{RESET}")
            song_list_len = 0
            
    for i in range(song_list_len):
        song = ""
        while len(song) == 0:
            song = input("Nhập tên bài hát {}: ".format(i + 1)).strip()
        mp3.add_song(song)
        
    print(BLUE + "----------- Danh sách bài hát -----------" + RESET)
    for index, value in enumerate(mp3.music_queue):
        print("{}. {}".format(index + 1, value))
        
    choice_menu = """LỰA CHỌN:
        1. Phát nhạc
        2. Bỏ qua bài hát
        3. Exit
    """
    
    choose = 0
    while choose != 3 or mp3.music_queue != []:
        print(BLUE + choice_menu + RESET)
        try:
            choose = int(input())
        except Exception as e:
            print(RED + "Lỗi: " + str(e) + RESET)
            choose = 0

        # kiem tra tung hanh dong
        match choose:
            case 1:
                # phat nhac
                mp3.play_song()
            case 2:
                # bo qua bai hat
                mp3.skip_song()
            case 3:
                # exit
                print(
                    BLUE
                    + "----------- Cảm ơn bạn đã sử dụng chương trình! -----------"
                    + RESET
                )
                break
            
            case _:
                print(RED + "Lỗi: Lựa chọn không hợp lệ!" + RESET)

test_drive()