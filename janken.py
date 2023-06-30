import random


def play():
    a = input("\n入力 : ")
    HANDS = ("g", "c", "p")
    if a in HANDS:
        b = random.randint(1,3)
        print("\nーーー試合結果ーーー\n")
        # 1=g,2=c,3=p

        match b:
            case 1:
                match a:
                    case "g":
                        print(
                            "あなた : グー\n"
                            "相手 : グー\n"
                            "\n"
                            ">>>あいこ\n"
                            "\n"
                            "ーーーあいこーーー\n"
                            "> グー : g\n"
                            "> チョキ : c\n"
                            "> パー : p\n"
                            "のいずれかを入力してください\n"
                        )
                        play()
                    case "c":
                        print("あなた : チョキ\n"
                        "相手 : グー\n"
                        "\n"
                        ">>>敗北")
                    case "p":
                        print("あなた : パー\n"
                        "相手 : グー\n"
                        "\n"
                        ">>>勝利")
            case 2:
                match a:
                    case "g":
                        print("あなた : グー\n"
                        "相手 : チョキ\n"
                        "\n"
                        ">>>勝利")
                    case "c":
                        print("あなた : チョキ\n"
                        "相手 : チョキ\n"
                        "\n"
                        ">>>あいこ\n"
                        "\n"
                        "ーーーあいこーーー\n"
                        "> グー : g\n"
                        "> チョキ : c\n"
                        "> パー : p\n"
                        "のいずれかを入力さいさい")
                        play()
                    case "p":
                        print("あなた : パー\n"
                        "相手 : チョキ\n"
                        "\n"
                        ">>>敗北")
            case 3:
                match a:
                    case "g":
                        print("あなた : グー\n"
                        "相手 : パー\n"
                        "\n"
                        ">>>敗北")
                    case "c":
                        print("あなた : チョキ\n"
                        "相手 : パー\n"
                        "\n"
                        ">>>勝利")
                    case "p":
                        print("あなた : パー\n"
                        "相手 : パー\n"
                        "\n"
                        ">>>あいこ\n"
                        "\n"
                        "ーーーあいこーーー\n"
                        "> グー : g\n"
                        "> チョキ : c\n"
                        "> パー : p\n"
                        "のいずれかを入力さいさい")
                        play()
    else:
        print("\n"
        "ーーーエラーーーー\n"
        "> グー : g\n"
        "> チョキ : c\n"
        "> パー : p\n"
        "のいずれかを入力さいさい")
        play()

print("\n"
"ーーー新規ゲームーーー\n"
"> グー : g\n"
"> チョキ : c\n"
"> パー : p\n"
"のいずれかを入力さいさい")
play()
                

