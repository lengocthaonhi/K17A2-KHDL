#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.2: Chọn đội trưởng của đội tệ nhất
team1=['Steven','Neena','Lex','Alexander','Bruce']
team2=['David','Jack','Bill','Tom','Mike','Daniel']
team3=['Alexander','Adam','Payam','Kevin','Sigal','Mike']
teams=[team1,team2,team3]           # Đội tệ nhất là đội cuối cùng trong ds (có index = -1)
the_worst_team=teams[-1]
print("Đội trưởng của đội tệ nhất là:",the_worst_team[1])  # đội trưởng là người thứ 2 trong đội tệ nhất (có index = 1)