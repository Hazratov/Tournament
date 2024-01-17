# Manba Xazratov Behro'z
class TournamentScoringSystem:
    def __init__(self):
        self.teams = {}
        self.scores = {}
        self.players = {}
        self.messages = []
    

    def start(self):
        print("♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦")
        print("♦  ⚠️  Turnir bo'limlari                                 ♦")
        print("♦  1️⃣  Ishtirokchilarni kiritish                         ♦")
        print("♦  2️⃣  Jamoalarni kiritish                               ♦")
        print("♦  3️⃣  Shartlar va ballarni kiritish                     ♦")
        print("♦  4️⃣  Turnirni boshlash                                 ♦")
        print("♦  5️⃣  Ishtirokchi/Jamoa ning balini o'zgartirish        ♦")
        print("♦  6️⃣  Jamoalarni ballarini bilish                       ♦")
        print("♦  7️⃣  Ishtirokchilarni ballarini bilish                 ♦")
        print("♦  8️⃣  Xat yo'llash                                      ♦")
        print("♦  9️⃣  Chiqish                                           ♦")
        print("♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦")

# ishtirokchi qo'shish 
    def player(self):
        for num in range(1,20+1):
            player_name = input(f"{num} chi ishtirokchi ismini kiriting: ")
            if player_name.lower() in self.players:
                print(f"{player_name} ismli ishtirokchi allaqachon ishtirok etyabdi!")
                break
            else:
                self.players[player_name] = 0
        print(f"ishtirokchilar ro'yxati: ")
        for x_player,y_player in self.players.items():
            print(x_player,y_player)

# jamoa qo'shish
    def team(self):
        for num in range(1,4+1):
            team_name = input(f"{num} chi jamoani kiriting: ")
            if team_name.lower() in self.teams:
                print(f"{team_name} jamoasi allaqachon ishtirok etyabdi!")
                break
            else:
                self.teams[team_name] = 0
        print(f"jamoa ro'yxati: ")
        for x_team,y_team in self.teams.items():
            print(x_team,y_team)


# shartlar qo'shish
    def AddMission(self):
        try:
            print("Saloom, siz istalgan turdagi shartlarni qo'shishingiz mumkin(urinishlar 5 ta)")
            for num2 in range(1,5+1):
                shart = input(f"{num2} chi shartni kiriting: ")
                if shart.lower() in self.scores:
                    print(f"{shart} allaqachon bor!")
                    break
                else:
                    ball = int(input(f"{shart} ga Nechchi ball qo'shmoqchisiz: "))
                    self.scores[shart]=ball
            # print(f"Umumiy shartlar va berilgan ballar {self.scores}")
            for x_ball,y_ball in self.scores.items():
                print(f"{x_ball} ga {y_ball} ball beriladi")
        except ValueError:
            print("Xurmatli ishtirokchi, faqat sonlar qabul qilinadi!")


# turnirni boshlash
    def StartGame(self):
        try:
            print("O'yin boshlandi !")
            print("ishtirokchilar shartlarni bajarishga tayyor")
            for num4 in self.players.keys():
                print("--------------")
                for num5,num5_ball in self.scores.items():
                    print(f"{num4} {num5} ni bajarishga ketdi")
                    options = int(input(f"{num4} {num5} ni bajardimi?\n1.xa\n2.yo'q\n(1/2):"))
                    # print(num5_ball)
                    if options == 1:
                        self.players[num4]+=num5_ball
                        print(f"{num4} ga {num5_ball} ball berildi !")
                    else:
                        print(f"{num4} shartni bajarmadi va ball berilmadi!")
            print("--------------------------")
            print("Jamoalar shartlarni bajarishga tayyor !")
            for team_num in self.teams.keys():
                print("---------------")
                for team_num5,team_ball5 in self.scores.items():
                    print(f"{team_num} {team_num5} ni bajarishga ketdi")
                    options_team = int(input(f"{team_num} {team_num5} ni bajardimi?\n1.xa\n2.yo'q\n(1/2):"))
                    if options_team == 1:
                        self.teams[team_num]+=team_ball5
                        print(f"{team_num} ga {team_ball5} ball berildi !")
                    else:
                        print(f"{team_num} shartni bajarmadi va ball berilmadi!")
            print("--------------------------")
            print("Ishtirokchilar Reytingi:")
            sorted_top_ishtirokchilar = dict(sorted(self.players.items(), key=lambda item: item[1], reverse=True))
            for reyting_x,reyting_y in sorted_top_ishtirokchilar.items():
                print(f"{reyting_x} {reyting_y} ball")
            print("--------------------------")
            print("Jamoalar Reytingi:")
            sorted_top_team = dict(sorted(self.teams.items(), key=lambda item: item[1], reverse=True))
            for reyting_x_team,reyting_y_team in sorted_top_team.items():
                print(f"{reyting_x_team} {reyting_y_team} ball")
        except ValueError:
            print("Xurmatli ishtirokchi, Faqat sonlar kiritiladi!")

    # def player(self):
    #     try:
    #         for num in range(1,20+1):
    #             players_name = input(f"{num} chi ishtirokchi ismingizni kiriting: ")
    #             how_much = int(input("Shartlar nechta bo'lishini xoxlaysiz? "))
    #             if players_name in self.players:
    #                 print("✔ ishtirokchi allaqachon ishtirok etyabdi")
    #                 break
    #             else:
    #                 self.players[players_name] = 0
    #                 for num2 in range(1,how_much+1):
    #                     shart = input(f"{num2} chi shartni kiriting: ")
    #                     ball = int(input(f"{num2} shartga nechi ball qo'yasiz: "))
    #                     self.scores[shart] = ball
    #                     print(f"{shart} ga {ball} ball qo'yiladi")
    #                     print(f"{players_name} shartni bajarishga ketdi")
    #                     option = int(input(f"{players_name} shartni bajardimi?\n1. xa\n2. yo'q\n(1/2): "))  
    #                     if option == 1:
    #                         self.players[players_name]+=ball
    #                     else:
    #                         print(f"{players_name} shartni bajarmadi va ball olmadi 🤷‍♀️")
    #     except ValueError:
    #         print("faqat raqam kiritish mumkin")
    #     print(f"ishtirokchi ballari: {self.players} ")

# jamoa qo'shish               

    # def team(self):
    #     try:
    #         for num_2 in range(1,4+1):
    #             teams_name = input(f"{num_2} chi Jamoa nomini kiriting: ")
    #             how_much = int(input("Shartlar nechta bo'lishini xoxlaysiz? "))
    #             if teams_name in self.teams:
    #                 print("✔ Jamoa allaqachon ishtirok etyabdi")
    #                 break
    #             else:
    #                 self.teams[teams_name] = 0
    #                 for num3 in range(1,how_much+1):
    #                     shart = input(f"{num3} chi shartni kiriting: ")
    #                     ball = int(input(f"{num3} shartga nechi ball qo'yasiz: "))
    #                     self.scores[shart] = ball
    #                     print(f"{shart} ga {ball} ball qo'yiladi")
    #                     print(f"{teams_name} shartni bajarishga ketdi")
    #                     option = int(input(f"{teams_name} shartni bajardimi?\n1. xa\n2. yo'q: "))  
    #                     if option == 1:
    #                         self.teams[teams_name]+=ball
    #                     else:
    #                         print(f"{teams_name} shartni bajarmadi va ball olmadi")
    #     except ValueError:
    #         print("faqat raqam kiritilsin")
    #     print(f"Jamoa ballari: {self.teams} ")
        



# ishtirokchining balini o'zgartirish
    def updateBall(self):
        try:
            choose_options = int(input("Saloom!, Ishtirokchilarni ballarini o'zgartiramizmi yoki jamoalar?\n1.Ishtirokchilarni\n2.Jamoalarni\n(1/2): "))    
            if choose_options == 1:
                update__player = input("Balini o'zgartirmoqchi bo'lgan ishtirokchi ismini kiriting: ")
                if update__player.lower() in self.players:
                    current__ball = int(input("ishtirokchining yangi balini kiriting: "))
                    self.players[update__player] = current__ball
                    print(f"{update__player} ishtirokchini bali {current__ball} ga o'zgartirildi!")
                
                else:
                    print("bunday ishtirokchi mavjud emas!")
            else:
                update__teams = input("Balini o'zgartirmoqchi bo'lgan jamoani kiriting: ")
                if update__teams.lower() in self.teams:
                    current__ball_team = int(input("jamoaning yangi balini kiriting: "))
                    self.teams[update__teams] = current__ball_team
                    print(f"{update__teams} jamoaning bali {current__ball_team} ga o'zgartirildi!")
                
                else:
                    print("bunday Jamoa mavjud emas!")
        except ValueError:
            print("faqat son kiriting!")

# jamoa umumiy ballari 
    def overallOfteam(self):
        print("Jamoalar umumiy ballari:")
        sorted_top_team = dict(sorted(self.teams.items(), key=lambda item: item[1], reverse=True))
        for reyting_x_team,reyting_y_team in sorted_top_team.items():
            print(f"{reyting_x_team} {reyting_y_team} ball")
        
# ishtirokchi umumiy ballari    
    def overallOfplayer(self):
        print("Ishtirokchilar umumiy ballari:")
        sorted_top_ishtirokchilar = dict(sorted(self.players.items(), key=lambda item: item[1], reverse=True))
        for reyting_x,reyting_y in sorted_top_ishtirokchilar.items():
            print(f"{reyting_x} {reyting_y} ball")

# Shartlar va berilgan ballar
#     def overall(self):
#         print(f"Shartlar va berilgan ballar: {self.scores}")

# xat yo'llash
    def message(self):
        from_user = input("ishtirokchi ismingizni kiriting: ")
        message_user = input("Dastur haqida fikr mulohazalaringizni yozishingiz mumkin: ") 
        overall__message = message_user+f" {from_user} dan kelgan xabar!"
        self.messages.append(overall__message)
        print(f"foydalanuvchi habari: {self.messages}")

def main():
    system = TournamentScoringSystem()
    while True:
        system.start()
        choice = input("Variantni tanlang: ")

        if choice == "1":
            system.player()
        elif choice == "2":
            system.team()
        elif choice == "3":
            system.AddMission()
        elif choice == "4":
            system.StartGame()
        elif choice == "5":
            system.updateBall()
        elif choice == "6":
            system.overallOfteam()
        elif choice == "7":
            system.overallOfplayer()
        elif choice == "8":
            system.message()
        elif choice == "9":
            print("tizimdan chiqildi. xayr!")
            break
        else:
            print("Notog'ri variant. qayta urinib ko'ring")


if __name__ == "__main__":
    main()
